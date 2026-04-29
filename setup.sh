#!/bin/bash
# Quick setup script for SPOMS MongoDB Edition

echo "================================"
echo "SPOMS MongoDB Setup Script"
echo "================================"
echo ""

# Check Python
if ! command -v python &> /dev/null; then
    echo "✗ Python not found. Please install Python 3.8+"
    exit 1
fi
echo "✓ Python found"

# Check if requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo "✗ requirements.txt not found"
    exit 1
fi

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed"
else
    echo "✗ Failed to install dependencies"
    exit 1
fi

# Check MongoDB
echo ""
echo "Checking MongoDB connection..."
python -c "from db import db; print('✓ MongoDB connected!' if db else '✗ MongoDB not available')" 2>/dev/null

# Create .env if doesn't exist
if [ ! -f ".env" ]; then
    echo ""
    echo "Creating .env file..."
    if [ ! -f ".env.example" ]; then
        echo "MONGODB_URI=mongodb://localhost:27017" > .env
        echo "MONGODB_DB_NAME=spoms" >> .env
        echo "FLASK_ENV=development" >> .env
        echo "SECRET_KEY=your-secret-key-change-in-production" >> .env
    else
        cp .env.example .env
    fi
    echo "✓ .env file created - please edit with your MongoDB connection details"
fi

echo ""
echo "================================"
echo "Setup Complete!"
echo "================================"
echo ""
echo "To run the application:"
echo "  python app.py"
echo ""
echo "Then open: http://127.0.0.1:5000"
echo ""
echo "Demo accounts:"
echo "  - Admin: dennis / lopez"
echo "  - PO Officer: jani / jani"
echo "  - Finance Officer: angel / angel"
echo "  - Store Owner: jennifer / jennifer"