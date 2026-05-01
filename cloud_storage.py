"""
Cloud Storage Module for Vercel-Safe Image Uploads
Uses Cloudinary for serverless image hosting (no local file writes)
"""
import os
import cloudinary
import cloudinary.uploader
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

load_dotenv()

# Cloudinary Configuration (set these in Vercel environment variables)
CLOUDINARY_CLOUD_NAME = os.getenv('CLOUDINARY_CLOUD_NAME')
CLOUDINARY_API_KEY = os.getenv('CLOUDINARY_API_KEY')
CLOUDINARY_API_SECRET = os.getenv('CLOUDINARY_API_SECRET')

# Initialize Cloudinary
if CLOUDINARY_CLOUD_NAME and CLOUDINARY_API_KEY and CLOUDINARY_API_SECRET:
    cloudinary.config(
        cloud_name=CLOUDINARY_CLOUD_NAME,
        api_key=CLOUDINARY_API_KEY,
        api_secret=CLOUDINARY_API_SECRET
    )


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif', 'webp'}


def upload_profile_image(file_obj, user_id):
    """
    Upload profile image to Cloudinary (cloud storage)
    
    Args:
        file_obj: Flask FileStorage object from request.files
        user_id: User's ID for organizing uploads
        
    Returns:
        dict with 'success' (bool), 'url' (str), and 'error' (str if failed)
    """
    try:
        # Validate file
        if not file_obj or not file_obj.filename:
            return {'success': False, 'error': 'No file provided'}
        
        if not allowed_file(file_obj.filename):
            return {'success': False, 'error': 'File type not allowed. Use PNG, JPG, JPEG, GIF, or WEBP'}
        
        # Secure filename
        filename = secure_filename(file_obj.filename)
        
        # Upload to Cloudinary
        # folder: organize by feature (profile_pictures)
        # public_id: use user_id to overwrite old profile pics
        response = cloudinary.uploader.upload(
            file_obj,
            folder='spoms/profile_pictures',
            public_id=f'user_{user_id}',
            overwrite=True,  # Replace old profile pic with new one
            resource_type='auto',
            quality='auto',  # Optimize quality
            max_file_size=5242880  # 5MB max
        )
        
        # Return the secure CDN URL
        return {
            'success': True,
            'url': response['secure_url']
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': f'Upload failed: {str(e)}'
        }


def delete_profile_image(user_id):
    """
    Delete old profile image from Cloudinary
    
    Args:
        user_id: User's ID
        
    Returns:
        dict with 'success' (bool)
    """
    try:
        cloudinary.uploader.destroy(f'spoms/profile_pictures/user_{user_id}')
        return {'success': True}
    except Exception as e:
        # Don't fail if image doesn't exist
        return {'success': True}


def upload_logo_image(file_obj):
    """
    Upload system logo to Cloudinary
    
    Args:
        file_obj: Flask FileStorage object
        
    Returns:
        dict with 'success' (bool), 'url' (str), and 'error' (str if failed)
    """
    try:
        if not file_obj or not file_obj.filename:
            return {'success': False, 'error': 'No file provided'}
        
        if not allowed_file(file_obj.filename):
            return {'success': False, 'error': 'File type not allowed'}
        
        response = cloudinary.uploader.upload(
            file_obj,
            folder='spoms/system',
            public_id='logo',
            overwrite=True,
            resource_type='auto'
        )
        
        return {
            'success': True,
            'url': response['secure_url']
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': f'Upload failed: {str(e)}'
        }


def upload_background_image(file_obj):
    """
    Upload homepage background to Cloudinary
    
    Args:
        file_obj: Flask FileStorage object
        
    Returns:
        dict with 'success' (bool), 'url' (str), and 'error' (str if failed)
    """
    try:
        if not file_obj or not file_obj.filename:
            return {'success': False, 'error': 'No file provided'}
        
        if not allowed_file(file_obj.filename):
            return {'success': False, 'error': 'File type not allowed'}
        
        response = cloudinary.uploader.upload(
            file_obj,
            folder='spoms/system',
            public_id='background',
            overwrite=True,
            resource_type='auto'
        )
        
        return {
            'success': True,
            'url': response['secure_url']
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': f'Upload failed: {str(e)}'
        }
