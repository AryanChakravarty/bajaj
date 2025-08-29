#!/bin/bash

echo "🚀 Starting BFHL API..."
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    echo "💡 Please install Python 3.8+ from https://python.org"
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo

# Check if requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo "❌ requirements.txt not found"
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
if ! python3 -m pip install -r requirements.txt; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo "✅ Dependencies installed"
echo

# Start the server
echo "🚀 Starting server..."
echo "📡 API will be available at: http://localhost:8000"
echo "📚 Documentation: http://localhost:8000/docs"
echo "🏥 Health check: http://localhost:8000/health"
echo "⏹️  Press Ctrl+C to stop"
echo

python3 main.py
