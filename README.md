# 🚀 BFHL REST API

A FastAPI-based REST API that processes data arrays according to specific requirements. Built for the VIT Full Stack Question Paper task.

## ✨ Features

- **POST /bfhl**: Processes JSON data arrays and returns categorized results
- **Data Classification**: Separates numbers (even/odd), alphabets, and special characters
- **String Processing**: Creates alternating case strings from alphabetic input
- **Error Handling**: Graceful error handling with `is_success` flag
- **Input Validation**: Pydantic models for request/response validation

## 🛠️ Tech Stack

- **Python 3.11+**
- **FastAPI** - Modern, fast web framework
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- pip package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AryanChakravarty/bajaj.git
   cd bajaj
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API:**
   ```bash
   python main.py
   ```

4. **Access the API:**
   - **API**: http://localhost:8000
   - **Documentation**: http://localhost:8000/docs
   - **Health Check**: http://localhost:8000/health

## 📡 API Endpoints

### POST /bfhl

**Request Body:**
```json
{
  "data": ["2", "a", "y", "4", "&", "-", "*", "5", "92", "b"]
}
```

**Response:**
```json
{
  "is_success": true,
  "user_id": "aryan_chakravarty_29082025",
  "email": "aryan@xyz.com",
  "roll_number": "ABCD123",
  "odd_numbers": ["5"],
  "even_numbers": ["2", "4", "92"],
  "alphabets": ["A", "Y", "B"],
  "special_characters": ["&", "-", "*"],
  "sum": "103",
  "concat_string": "ByA"
}
```

## 🧪 Testing

Run the test script to verify functionality:
```bash
python test_api.py
```

## 🌐 Deployment

### Option 1: Railway (Recommended)
1. Connect your GitHub account to [Railway](https://railway.app)
2. Select this repository
3. Railway auto-detects Python and deploys

### Option 2: Render
1. Connect GitHub to [Render](https://render.com)
2. Create new Web Service
3. Select this repository
4. Build: `pip install -r requirements.txt`
5. Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Option 3: Vercel
```bash
npm install -g vercel
vercel
```

## 📁 Project Structure

```
bajaj/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── test_api.py         # API testing script
├── README.md           # This file
├── .gitignore          # Git ignore rules
├── vercel.json         # Vercel configuration
├── Procfile            # Heroku configuration
├── runtime.txt         # Python version for Heroku
├── start.py            # Startup script
├── start.bat           # Windows startup script
└── start.sh            # Unix startup script
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Aryan Chakravarty**
- GitHub: [@AryanChakravarty](https://github.com/AryanChakravarty)

---

⭐ **Star this repository if you find it helpful!**
