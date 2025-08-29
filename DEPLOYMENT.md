# Deployment Guide

This guide provides step-by-step instructions for deploying the BFHL API to various platforms.

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AryanChakravarty/bajaj.git
   cd bajaj
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Test locally:**
   ```bash
   python main.py
   ```

4. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Initial commit: BFHL API implementation"
   git push origin main
   ```

## 🌐 Deployment Options

### Option 1: Vercel (Recommended - Free & Easy)

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Deploy:**
   ```bash
   vercel
   ```

3. **Follow the prompts:**
   - Link to existing project or create new
   - Set project name
   - Deploy

4. **Your API will be available at:**
   `https://your-project-name.vercel.app`

### Option 2: Railway (Free Tier Available)

1. **Go to [Railway.app](https://railway.app)**
2. **Sign in with GitHub**
3. **Click "New Project"**
4. **Select "Deploy from GitHub repo"**
5. **Choose your `bajaj` repository**
6. **Railway will automatically:**
   - Detect Python
   - Install dependencies from `requirements.txt`
   - Deploy your API

### Option 3: Render (Free Tier Available)

1. **Go to [Render.com](https://render.com)**
2. **Sign in with GitHub**
3. **Click "New +" → "Web Service"**
4. **Connect your `bajaj` repository**
5. **Configure:**
   - **Name:** `bfhl-api`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. **Click "Create Web Service"**

### Option 4: Heroku (Paid)

1. **Install Heroku CLI:**
   ```bash
   # macOS
   brew install heroku/brew/heroku
   
   # Windows
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login:**
   ```bash
   heroku login
   ```

3. **Create app:**
   ```bash
   heroku create your-app-name
   ```

4. **Deploy:**
   ```bash
   git push heroku main
   ```

5. **Open:**
   ```bash
   heroku open
   ```

## 🔧 Environment Variables

Most platforms will automatically set `PORT`. If you need to set custom variables:

### Vercel
```bash
vercel env add PORT 8000
```

### Railway
- Go to your project → Variables tab
- Add `PORT=8000`

### Render
- Go to your service → Environment tab
- Add `PORT=8000`

### Heroku
```bash
heroku config:set PORT=8000
```

## 📱 Testing Your Deployed API

### 1. Test the main endpoint:
```bash
curl -X POST "https://your-deployed-url.vercel.app/bfhl" \
     -H "Content-Type: application/json" \
     -d '{"data": ["2", "a", "y", "4", "&", "-", "*", "5", "92", "b"]}'
```

### 2. Test health check:
```bash
curl "https://your-deployed-url.vercel.app/health"
```

### 3. View API docs:
- Open `https://your-deployed-url.vercel.app/docs` in your browser

## 🐛 Troubleshooting

### Common Issues:

1. **Port binding error:**
   - Make sure you're using `$PORT` environment variable
   - Update `main.py` if needed

2. **Dependencies not found:**
   - Check `requirements.txt` is in root directory
   - Ensure all imports are in `requirements.txt`

3. **API not responding:**
   - Check deployment logs
   - Verify environment variables
   - Test locally first

### Debug Commands:

```bash
# Check if API is running locally
curl http://localhost:8000/health

# Check Python version
python --version

# Check installed packages
pip list

# Test with Python
python test_api.py
```

## 📊 Monitoring

### Vercel:
- Dashboard shows deployment status
- Function logs available in dashboard

### Railway:
- Real-time logs in dashboard
- Performance metrics available

### Render:
- Logs tab shows real-time output
- Metrics dashboard available

### Heroku:
```bash
# View logs
heroku logs --tail

# Check app status
heroku ps
```

## 🔄 Continuous Deployment

All platforms support automatic deployment:

1. **Push to GitHub main branch**
2. **Platform automatically detects changes**
3. **Runs build and deployment**
4. **Your API updates automatically**

## 🎯 Next Steps

After successful deployment:

1. **Test all endpoints**
2. **Share your API URL**
3. **Monitor performance**
4. **Set up custom domain (optional)**
5. **Add authentication (if needed)**

## 📞 Support

- **Vercel:** [vercel.com/support](https://vercel.com/support)
- **Railway:** [railway.app/docs](https://railway.app/docs)
- **Render:** [render.com/docs](https://render.com/docs)
- **Heroku:** [devcenter.heroku.com](https://devcenter.heroku.com)

---

**🎉 Congratulations! Your BFHL API is now deployed and accessible worldwide!**
