from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from functools import wraps
from werkzeug.utils import secure_filename
import os
from datetime import datetime
import hashlib
from db import get_collection   # ✅ removed init_db

app = Flask(__name__)
app.secret_key = 'spoms-secret-2026'

os.makedirs('static/images', exist_ok=True)

# ================= HELPERS =================

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
    settings.pop('_id', None)
    return settings


def save_settings(settings):
    settings_col = get_collection('settings')
    settings.pop('_id', None)
    settings_col.replace_one({}, settings, upsert=True)

# ================= CONTEXT =================

@app.context_processor
def inject_settings():
    return {'settings': load_settings()}


@app.context_processor
def inject_current_user():
    if 'user' in session:
        user = get_collection('users').find_one({'name': session['user']})
        if user:
            user.pop('_id', None)
            user.pop('password', None)
        return {'current_user': user}
    return {'current_user': None}

# ================= DECORATORS =================

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated


def role_check(roles):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if 'user' not in session:
                return redirect(url_for('login'))
            if session.get('role') not in roles:
                return render_template('403.html'), 403
            return f(*args, **kwargs)
        return decorated
    return decorator

# ================= ROUTES =================

@app.route('/')
def home():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        pwd = request.form.get('password')

        u = get_collection('users').find_one({'username': user})

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
    suppliers = list(get_collection('suppliers').find({}))
    orders = list(get_collection('orders').find({}))
    payments = list(get_collection('payments').find({}))

    stats = {
        'suppliers': len(suppliers),
        'orders': len(orders),
        'pending': len([o for o in orders if o.get('status') == 'Pending']),
        'completed': len([o for o in orders if o.get('status') == 'Delivered']),
        'payments': len(payments)
    }

    return render_template('dashboard.html', stats=stats, role=session.get('role'))

# ================= FEEDBACK =================

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


@app.route('/api/feedback', methods=['GET', 'POST'])
def api_feedback():
    col = get_collection('feedback')

    if request.method == 'POST':
        data = request.json or {}
        col.insert_one({
            "name": data.get('name'),
            "message": data.get('message'),
            "rating": data.get('rating'),
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        return jsonify({"success": True})

    return jsonify(list(col.find({}, {'_id': 0})))

# ================= SUPPLIERS =================

@app.route('/suppliers')
@login_required
def suppliers():
    if session.get('role') not in ['Administrator', 'Purchasing Officer', 'Store Owner']:
        return render_template('403.html'), 403

    data = list(get_collection('suppliers').find({}, {'_id': 0}))
    return render_template('suppliers.html', suppliers=data, role=session.get('role'))


@app.route('/api/suppliers', methods=['GET', 'POST'])
@login_required
def api_suppliers():
    col = get_collection('suppliers')

    if request.method == 'POST':
        if session.get('role') not in ['Administrator', 'Store Owner']:
            return jsonify({'error': 'Unauthorized'}), 403

        col.insert_one(request.json)
        return jsonify({'success': True})

    return jsonify(list(col.find({}, {'_id': 0})))


# ================= ORDERS =================

@app.route('/orders')
@login_required
def orders():
    if session.get('role') not in ['Administrator', 'Purchasing Officer', 'Finance Officer']:
        return render_template('403.html'), 403

    orders = list(get_collection('orders').find({}, {'_id': 0}))
    suppliers = list(get_collection('suppliers').find({}, {'_id': 0}))

    return render_template('purchase_orders.html', orders=orders, suppliers=suppliers)

# ================= PAYMENTS =================

@app.route('/payments')
@login_required
@role_check(['Finance Officer', 'Administrator'])
def payments():
    payments = list(get_collection('payments').find({}, {'_id': 0}))
    orders = list(get_collection('orders').find({}, {'_id': 0}))

    return render_template('payments.html', payments=payments, orders=orders)

# ================= SETTINGS =================

@app.route('/settings', methods=['GET', 'POST'])
@login_required
@role_check(['Administrator'])
def settings():
    settings = load_settings()
    message = None

    if request.method == 'POST':
        settings['system_name'] = request.form.get('system_name', settings['system_name'])

        if 'logo' in request.files:
            f = request.files['logo']
            if f and allowed_file(f.filename):
                filename = secure_filename(f.filename)
                path = f'images/logo-{int(datetime.now().timestamp())}.{filename.split(".")[-1]}'
                f.save(os.path.join('static', path))
                settings['logo'] = path

        save_settings(settings)
        message = "Saved successfully"

    return render_template('settings.html', settings=settings, message=message)

# ================= PROFILE =================

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    users = get_collection('users')
    user = users.find_one({'name': session['user']})

    if not user:
        return redirect(url_for('logout'))

    if request.method == 'POST':
        data = request.form
        update = {}

        if data.get('name'):
            update['name'] = data['name']
            session['user'] = data['name']

        if data.get('password'):
            update['password'] = hash_pwd(data['password'])

        if update:
            users.update_one({'_id': user['_id']}, {'$set': update})

    user.pop('_id', None)
    user.pop('password', None)

    return render_template('profile.html', user=user)
