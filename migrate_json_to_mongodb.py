"""
Migration script to transfer data from JSON files to MongoDB
Run this if you're migrating from the JSON version to MongoDB version
"""

import json
import os
from datetime import datetime
from db import get_collection, db

def migrate_from_json():
    """Migrate existing JSON data to MongoDB"""
    
    if db is None:
        print("✗ MongoDB connection failed. Please check your .env configuration.")
        return
    
    json_files = {
        'users.json': 'users',
        'suppliers.json': 'suppliers',
        'orders.json': 'orders',
        'payments.json': 'payments',
        'feedback.json': 'feedback',
        'settings.json': 'settings'
    }
    
    migrated_count = {}
    
    for json_file, collection_name in json_files.items():
        json_path = os.path.join('data', json_file)
        
        if not os.path.exists(json_path):
            print(f"⊘ {json_file} not found, skipping...")
            continue
        
        try:
            with open(json_path, 'r') as f:
                data = json.load(f)
            
            collection = get_collection(collection_name)
            
            # Skip if collection already has data
            if collection.count_documents({}) > 0:
                print(f"⊘ {collection_name} collection already has data, skipping...")
                continue
            
            # Handle different data structures
            if isinstance(data, list):
                collection.insert_many(data)
                migrated_count[json_file] = len(data)
                print(f"✓ Migrated {len(data)} records from {json_file} to {collection_name}")
            elif isinstance(data, dict):
                collection.insert_one(data)
                migrated_count[json_file] = 1
                print(f"✓ Migrated {json_file} to {collection_name}")
        
        except Exception as e:
            print(f"✗ Error migrating {json_file}: {str(e)}")
    
    # Summary
    print("\n" + "="*50)
    print("Migration Summary")
    print("="*50)
    total_records = sum(migrated_count.values())
    print(f"Total records migrated: {total_records}")
    for file, count in migrated_count.items():
        print(f"  - {file}: {count} record(s)")
    print("\n✓ Migration completed successfully!")
    print("\nNote: Your JSON files remain unchanged. You can safely delete the 'data' folder after verifying the migration.")

def backup_json():
    """Create a backup of JSON files before migration"""
    backup_dir = f'data_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
    
    if not os.path.exists('data'):
        print("No data folder found to backup.")
        return
    
    try:
        os.makedirs(backup_dir)
        for file in os.listdir('data'):
            if file.endswith('.json'):
                src = os.path.join('data', file)
                dst = os.path.join(backup_dir, file)
                with open(src, 'r') as f_src:
                    data = f_src.read()
                with open(dst, 'w') as f_dst:
                    f_dst.write(data)
        print(f"✓ Backup created in {backup_dir}")
        return backup_dir
    except Exception as e:
        print(f"✗ Backup failed: {str(e)}")
        return None

if __name__ == '__main__':
    print("\n" + "="*50)
    print("SPOMS: JSON to MongoDB Migration Tool")
    print("="*50 + "\n")
    
    # Create backup first
    print("Creating backup of JSON files...")
    backup_backup_dir = backup_json()
    
    print("\nStarting migration...")
    migrate_from_json()
    
    if backup_backup_dir:
        print(f"\n📁 Backup location: {backup_backup_dir}")
