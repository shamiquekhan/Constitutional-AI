# Deployment Steps for Constitutional AI

## Quick Start Deployment

### 1. Backend Deployment (Railway.app) - 5 minutes

1. **Sign up** at [Railway.app](https://railway.app)

2. **Create New Project**:
   - Click "New Project" → "Deploy from GitHub repo"
   - Select `shamiquekhan/Constitutional-AI`

3. **Configure Backend**:
   - Set root directory: `backend`
   - Install command: `pip install -r requirements-minimal.txt`
   - Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

4. **Copy Backend URL**:
   - Once deployed, Railway provides a URL like: `https://constitutional-ai-backend.railway.app`
   - Copy this URL for the next step

### 2. Frontend Deployment (Vercel) - 3 minutes

1. **Sign up** at [Vercel.com](https://vercel.com)

2. **Import Project**:
   - Click "Add New Project"
   - Import `shamiquekhan/Constitutional-AI`

3. **Configure Frontend**:
   - Framework Preset: `Create React App`
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `build`

4. **Set Environment Variable**:
   - Add environment variable:
     - Name: `REACT_APP_API_URL`
     - Value: Your Railway backend URL (from step 1)

5. **Deploy**:
   - Click "Deploy"
   - Your app will be live at `https://constitutional-ai.vercel.app`

### 3. Update Backend URL in Code

Update [frontend/src/utils/api.ts](frontend/src/utils/api.ts):

```typescript
const API_BASE_URL = process.env.REACT_APP_API_URL || 'https://constitutional-ai-backend.railway.app';
```

## Alternative Backend Hosting

### Render.com

1. Create Web Service
2. Connect GitHub repo
3. Settings:
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements-minimal.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

### Heroku

```bash
# Create Procfile in backend/
echo "web: uvicorn app.main:app --host 0.0.0.0 --port \$PORT" > backend/Procfile

# Deploy
heroku create constitutional-ai-backend
git subtree push --prefix backend heroku main
```

## Environment Variables

### Backend (.env)
```env
ENVIRONMENT=production
DEBUG=False
ALLOWED_ORIGINS=https://constitutional-ai.vercel.app
```

### Frontend (.env)
```env
REACT_APP_API_URL=https://constitutional-ai-backend.railway.app
```

## Verification Steps

1. **Backend Health Check**:
   ```bash
   curl https://your-backend-url.railway.app/health
   ```

2. **Frontend Test**:
   - Visit https://constitutional-ai.vercel.app
   - Try query: "What does Article 19 guarantee?"
   - Verify response displays with citations

3. **CORS Configuration**:
   - Ensure backend allows frontend domain in CORS settings

## Troubleshooting

### Backend Won't Start
- Check Railway logs: `railway logs`
- Verify Python version: `python --version` (should be 3.10+)
- Check dependencies: `pip list`

### Frontend Can't Connect to Backend
- Verify `REACT_APP_API_URL` in Vercel environment variables
- Check CORS settings in backend [main.py](backend/app/main.py)
- Test backend endpoint directly in browser

### Build Failures
- Clear node_modules: `rm -rf node_modules package-lock.json`
- Reinstall: `npm install`
- Try local build: `npm run build`

## Cost Estimates

- **Railway**: Free tier (500 hours/month) or $5/month
- **Vercel**: Free tier (unlimited deployments) or $20/month Pro
- **Total**: $0-25/month depending on usage

## Next Steps

1. ✅ Push code to GitHub
2. ✅ Deploy backend to Railway
3. ✅ Deploy frontend to Vercel
4. Configure custom domain (optional)
5. Set up monitoring and analytics
6. Add CI/CD with GitHub Actions

## Support

- Issues: https://github.com/shamiquekhan/Constitutional-AI/issues
- Email: [Your support email]
- Documentation: [README.md](README.md)
