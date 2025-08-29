@echo off
echo 🚀 Starting BFHL API...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo 💡 Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

echo ✅ Python found
echo.

REM Check if requirements.txt exists
if not exist requirements.txt (
    echo ❌ requirements.txt not found
    pause
    exit /b 1
)

REM Install dependencies
echo 📦 Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

echo ✅ Dependencies installed
echo.

REM Start the server
echo 🚀 Starting server...
echo 📡 API will be available at: http://localhost:8000
echo 📚 Documentation: http://localhost:8000/docs
echo 🏥 Health check: http://localhost:8000/health
echo ⏹️  Press Ctrl+C to stop
echo.

python main.py

pause
