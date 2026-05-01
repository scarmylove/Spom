from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from functools import wraps
from werkzeug.utils import secure_filename
import os
from datetime import datetime, timedelta
import hashlib
import base64
from db import init_db, get_collection
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'spoms-secret-2026'

os.makedirs('static/images', exist_ok=True)

# Initialize MongoDB on app startup
init_db()

def hash_pwd(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif', 'svg'}


def default_settings():
    return {
        'system_name': 'SPOMS',
        'logo': 'images/spoms.png',
        'homepage_background': 'images/spoms.png'
    }


def load_settings():
    settings_col = get_collection('settings')
    settings = settings_col.find_one({})
    if not settings:
        settings = default_settings()
        settings_col.insert_one(settings)
    # Remove MongoDB's _id field for consistency
    settings.pop('_id', None)
    return settings


def save_settings(settings):
    settings_col = get_collection('settings')
    settings.pop('_id', None)  # Remove _id to avoid conflicts
    settings_col.replace_one({}, settings, upsert=True)


@app.context_processor
def inject_settings():
    return {'settings': load_settings()}


@app.context_processor
def inject_current_user():
    if 'user' in session:
        users_col = get_collection('users')
        user = users_col.find_one({'name': session['user']})
        return {'current_user': user}
    return {'current_user': None}


# ===== DECORATORS =====
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

# ===== FEEDBACK PAGE =====

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


@app.route('/api/feedback', methods=['GET', 'POST'])
def api_feedback():
    feedback_col = get_collection('feedback')
    
    if request.method == 'POST':
        data = request.json
        feedback_col.insert_one({
            "name": data['name'],
            "message": data['message'],
            "rating": data['rating'],
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        return jsonify({"success": True})
    
    feedbacks = list(feedback_col.find({}, {'_id': 0}))
    return jsonify(feedbacks)

def role_check(roles):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if 'user' not in session:
                return redirect(url_for('login'))
            if session['role'] not in roles:
                return render_template('403.html'), 403
            return f(*args, **kwargs)
        return decorated
    return decorator


# ===== MGA ROUTES =====
@app.route('/')
def home():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        users_col = get_collection('users')
        u = users_col.find_one({'username': user})
        if u and u['password'] == hash_pwd(pwd):
            session['user'] = u['name']
            session['role'] = u['role']
            return redirect(url_for('dashboard'))
        return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    suppliers_col = get_collection('suppliers')
    orders_col = get_collection('orders')
    payments_col = get_collection('payments')
    
    suppliers = list(suppliers_col.find({}))
    orders = list(orders_col.find({}))
    payments = list(payments_col.find({}))
    
    stats = {
        'suppliers': len(suppliers),
        'orders': len(orders),
        'pending': len([o for o in orders if o.get('status') == 'Pending']),
        'completed': len([o for o in orders if o.get('status') == 'Delivered']),
        'payments': len(payments)
    }
    return render_template('dashboard.html', stats=stats, role=session['role'])

@app.route('/suppliers')
@login_required
def suppliers():
    if session['role'] not in ['Administrator', 'Purchasing Officer', 'Store Owner']:
        return render_template('403.html'), 403
    suppliers_col = get_collection('suppliers')
    data = list(suppliers_col.find({}, {'_id': 0}))
    return render_template('suppliers.html', suppliers=data, role=session['role'])

@app.route('/api/suppliers', methods=['GET', 'POST'])
@login_required
def api_suppliers():
    suppliers_col = get_collection('suppliers')
    
    if request.method == 'POST':
        if session['role'] not in ['Administrator', 'Store Owner']:
            return jsonify({'success': False, 'error': 'Unauthorized'}), 403
        data = request.json
        suppliers_col.insert_one(data)
        return jsonify({'success': True})
    
    suppliers = list(suppliers_col.find({}, {'_id': 0}))
    return jsonify(suppliers)

@app.route('/api/suppliers/<sid>', methods=['DELETE', 'PUT'])
@login_required
@role_check(['Administrator', 'Store Owner'])
def api_supplier(sid):
    suppliers_col = get_collection('suppliers')
    
    if request.method == 'DELETE':
        suppliers_col.delete_one({'id': sid})
        return jsonify({'success': True})
    elif request.method == 'PUT':
        data = request.json
        suppliers_col.update_one({'id': sid}, {'$set': data})
        return jsonify({'success': True})

@app.route('/orders')
@login_required
def orders():
    if session['role'] not in ['Administrator', 'Purchasing Officer', 'Finance Officer']:
        return render_template('403.html'), 403
    orders_col = get_collection('orders')
    suppliers_col = get_collection('suppliers')
    data = list(orders_col.find({}, {'_id': 0}))
    suppliers = list(suppliers_col.find({}, {'_id': 0}))
    return render_template('purchase_orders.html', orders=data, suppliers=suppliers, role=session['role'])

@app.route('/api/orders', methods=['GET', 'POST'])
@login_required
def api_orders():
    orders_col = get_collection('orders')
    
    if request.method == 'POST':
        data = request.json
        orders_col.insert_one(data)
        return jsonify({'success': True})
    
    orders = list(orders_col.find({}, {'_id': 0}))
    return jsonify(orders)

@app.route('/api/orders/<po_number>', methods=['PUT'])
@login_required
def update_order(po_number):
    if session.get('role') not in ['Administrator', 'Purchasing Officer']:
        return jsonify({'error': 'Unauthorized'}), 403
    
    data = request.json
    orders_col = get_collection('orders')
    result = orders_col.update_one({'po': po_number}, {'$set': data})
    
    if result.matched_count > 0:
        return jsonify({'success': True})
    return jsonify({'error': 'Order not found'}), 404

@app.route('/payments')
@login_required
@role_check(['Finance Officer', 'Administrator'])
def payments():
    payments_col = get_collection('payments')
    orders_col = get_collection('orders')
    data = list(payments_col.find({}, {'_id': 0}))
    orders = list(orders_col.find({}, {'_id': 0}))
    return render_template('payments.html', payments=data, orders=orders, user_role=session.get('role'))

@app.route('/api/payments', methods=['GET', 'POST'])
@login_required
def api_payments():
    payments_col = get_collection('payments')
    
    if request.method == 'POST':
        data = request.json
        payments_col.insert_one(data)
        return jsonify({'success': True})
    
    payments = list(payments_col.find({}, {'_id': 0}))
    return jsonify(payments)

@app.route('/api/payments/<payment_id>', methods=['PUT'])
@login_required
def update_payment(payment_id):
    if session.get('role') not in ['Administrator', 'Finance Officer']:
        return jsonify({'error': 'Unauthorized'}), 403
    
    data = request.json
    payments_col = get_collection('payments')
    result = payments_col.update_one({'id': payment_id}, {'$set': data})
    
    if result.matched_count > 0:
        return jsonify({'success': True})
    return jsonify({'error': 'Payment not found'}), 404

@app.route('/backup')
@login_required
def backup():
    suppliers_col = get_collection('suppliers')
    orders_col = get_collection('orders')
    payments_col = get_collection('payments')
    
    suppliers = list(suppliers_col.find({}))
    orders = list(orders_col.find({}))
    payments = list(payments_col.find({}))
    
    return render_template('backup.html', 
        suppliers_count=len(suppliers),
        orders_count=len(orders),
        orders_value=sum(o.get('total', 0) for o in orders),
        payments_count=len(payments),
        payments_total=sum(p.get('amount', 0) for p in payments)
    )

@app.route('/reports')
@login_required
def reports():
    suppliers_col = get_collection('suppliers')
    orders_col = get_collection('orders')
    payments_col = get_collection('payments')
    feedback_col = get_collection('feedback')
    
    suppliers = list(suppliers_col.find({}))
    orders = list(orders_col.find({}))
    payments = list(payments_col.find({}))
    feedbacks = list(feedback_col.find({}))
    
    return render_template('reports.html', 
        suppliers_count=len(suppliers),
        orders_count=len(orders),
        orders_value=sum(o.get('total', 0) for o in orders),
        payments_count=len(payments),
        payments_total=sum(p.get('amount', 0) for p in payments),
        orders=orders,
        feedbacks=feedbacks
    )

@app.route('/api/chart/orders')
@login_required
def chart_orders():
    orders_col = get_collection('orders')
    orders = list(orders_col.find({}))
    statuses = ['Pending', 'Approved', 'Delivered']
    data = [len([o for o in orders if o.get('status') == s]) for s in statuses]
    return jsonify({'labels': statuses, 'data': data, 'colors': ['#f59e0b', '#3b82f6', '#10b981']})

@app.route('/api/chart/suppliers')
@login_required
def chart_suppliers():
    suppliers_col = get_collection('suppliers')
    orders_col = get_collection('orders')
    suppliers = list(suppliers_col.find({}))
    orders = list(orders_col.find({}))
    labels = [s.get('name', '') for s in suppliers]
    data = [len([o for o in orders if o.get('supplier') == s.get('name', '')]) for s in suppliers]
    return jsonify({'labels': labels, 'data': data, 'colors': ['#2563eb', '#dc2626', '#16a34a']})

@app.route('/users')
@login_required
@role_check(['Administrator'])
def users():
    users_col = get_collection('users')
    data = list(users_col.find({}, {'_id': 0, 'password': 0}))
    return render_template('users.html', users=data)

@app.route('/api/users', methods=['GET', 'POST'])
@login_required
@role_check(['Administrator'])
def api_users():
    users_col = get_collection('users')
    
    if request.method == 'POST':
        data = request.json
        if not data.get('username') or not data.get('password') or not data.get('name') or not data.get('role'):
            return jsonify({'success': False, 'error': 'Missing user data'}), 400
        if users_col.find_one({'username': {'$regex': f'^{data["username"]}$', '$options': 'i'}}):
            return jsonify({'success': False, 'error': 'Username already exists'}), 400
        data['password'] = hash_pwd(data['password'])
        existing_ids = [int(u['user_id'][1:]) for u in users_col.find({}) if u.get('user_id', '').startswith('U') and u['user_id'][1:].isdigit()]
        next_id = max(existing_ids, default=0) + 1
        data['user_id'] = f'U{next_id:02d}'
        data['status'] = data.get('status', 'Active')
        users_col.insert_one(data)
        data.pop('password', None)
        data.pop('_id', None)
        return jsonify({'success': True, 'user': data})
    
    users = list(users_col.find({}, {'_id': 0, 'password': 0}))
    return jsonify(users)

@app.route('/api/users/<uid>', methods=['PUT', 'DELETE'])
@login_required
@role_check(['Administrator'])
def api_user(uid):
    users_col = get_collection('users')
    user = users_col.find_one({'user_id': uid})
    if not user:
        return jsonify({'success': False, 'error': 'User not found'}), 404

    if request.method == 'DELETE':
        users_col.delete_one({'user_id': uid})
        return jsonify({'success': True})

    data = request.json or {}
    update_data = {}
    
    if data.get('username') and data['username'].lower() != user['username'].lower():
        if users_col.find_one({'username': {'$regex': f'^{data["username"]}$', '$options': 'i'}, 'user_id': {'$ne': uid}}):
            return jsonify({'success': False, 'error': 'Username already exists'}), 400
        update_data['username'] = data['username']
    
    if data.get('name'):
        update_data['name'] = data['name']
    if data.get('role'):
        update_data['role'] = data['role']
    if data.get('status'):
        update_data['status'] = data['status']
    if data.get('password'):
        update_data['password'] = hash_pwd(data['password'])

    if update_data:
        users_col.update_one({'user_id': uid}, {'$set': update_data})
    
    updated_user = users_col.find_one({'user_id': uid}, {'_id': 0, 'password': 0})
    return jsonify({'success': True, 'user': updated_user})

@app.route('/settings', methods=['GET', 'POST'])
@login_required
@role_check(['Administrator'])
def settings():
    settings = load_settings()
    message = None
    if request.method == 'POST':
        system_name = request.form.get('system_name', settings['system_name']).strip()
        settings['system_name'] = system_name or settings['system_name']

        if 'logo' in request.files:
            logo_file = request.files['logo']
            if logo_file and allowed_file(logo_file.filename):
                logo_data = base64.b64encode(logo_file.read()).decode('utf-8')
                settings['logo'] = f'data:image/{logo_file.filename.rsplit(".", 1)[1].lower()};base64,{logo_data}'

        if 'background' in request.files:
            bg_file = request.files['background']
            if bg_file and allowed_file(bg_file.filename):
                bg_data = base64.b64encode(bg_file.read()).decode('utf-8')
                settings['homepage_background'] = f'data:image/{bg_file.filename.rsplit(".", 1)[1].lower()};base64,{bg_data}'

        save_settings(settings)
        message = 'Settings saved successfully.'

    return render_template('settings.html', settings=settings, message=message)

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    users_col = get_collection('users')
    user = users_col.find_one({'name': session['user']})
    if not user:
        return redirect(url_for('logout'))
    message = None
    if request.method == 'POST':
        data = request.form
        update_data = {}
        
        if data.get('name'):
            new_name = data['name'].strip()
            update_data['name'] = new_name
            session['user'] = new_name
        
        if data.get('username'):
            if data['username'].lower() != user['username'].lower():
                if users_col.find_one({'username': {'$regex': f'^{data["username"]}$', '$options': 'i'}, '_id': {'$ne': user['_id']}}):
                    message = 'Username already exists'
                else:
                    update_data['username'] = data['username'].strip()
        
        if data.get('password'):
            update_data['password'] = hash_pwd(data['password'])
        
        if 'profile_picture' in request.files:
            pic_file = request.files['profile_picture']
            if pic_file and allowed_file(pic_file.filename):
                pic_data = base64.b64encode(pic_file.read()).decode('utf-8')
                update_data['profile_picture'] = f'data:image/{pic_file.filename.rsplit(".", 1)[1].lower()};base64,{pic_data}'
        
        if update_data:
            users_col.update_one({'_id': user['_id']}, {'$set': update_data})
        
        if not message:
            message = 'Profile updated successfully.'
    
    user.pop('password', None)
    user.pop('_id', None)
    return render_template('profile.html', user=user, message=message)

if __name__ == '__main__':
    # Production: use gunicorn (Vercel)
    # Development: use Flask debug server
    import os
    if os.environ.get('FLASK_ENV') == 'production':
        app.run(debug=False)
    else:
        app.run(debug=True)
