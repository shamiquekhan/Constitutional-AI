# 🎬 Constitutional AI - Complete Startup Guide

## ✅ BACKEND IMPLEMENTATION COMPLETE

---

## 📋 Pre-Flight Checklist

### System Requirements
- [ ] Windows 10/11 OR Linux/macOS
- [ ] Python 3.11+
- [ ] Node.js 18+ (for frontend)
- [ ] PostgreSQL 15+ (optional for production)
- [ ] Redis (optional for caching)
- [ ] Git

### API Keys Required
- [ ] OpenAI API Key (for LLM)
- [ ] Pinecone API Key (for vector DB)

---

## 🚀 Complete Startup Procedure

### Step 1: Backend Setup (5 minutes)

```powershell
# 1. Navigate to backend directory
cd "c:\Project\Constituional Ai\backend"

# 2. Create Python virtual environment (recommended)
python -m venv venv

# 3. Activate virtual environment
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create environment file
cp .env.example .env
```

**Edit `.env` file:**
```env
# Required (for production)
OPENAI_API_KEY=sk-your-openai-key
PINECONE_API_KEY=your-pinecone-key

# Optional (defaults work for development)
DATABASE_URL=postgresql://user:password@localhost:5432/constitutional_ai
REDIS_URL=redis://localhost:6379
ELASTICSEARCH_URL=http://localhost:9200
ENVIRONMENT=development
DEBUG=true
```

```powershell
# 6. Initialize database (optional for mock testing)
python scripts\init_db.py

# 7. Start backend server
uvicorn app.main:app --reload
```

**✅ Backend Running:** http://localhost:8000

---

### Step 2: Frontend Setup (3 minutes)

```powershell
# 1. Open NEW terminal
# 2. Navigate to frontend directory
cd "c:\Project\Constituional Ai\frontend"

# 3. Install dependencies (if not done)
npm install

# 4. Start development server
npm run dev
```

**✅ Frontend Running:** http://localhost:3000

---

### Step 3: Verify Everything Works (2 minutes)

#### Test Backend
```powershell
# Open NEW terminal
cd "c:\Project\Constituional Ai\backend"
python scripts\test_api.py
```

**Expected output:**
```
=== Testing Health Endpoint ===
Status: 200
Response: {
  "status": "healthy",
  "version": "1.0.0",
  ...
}

=== Testing Legal Query ===
Status: 200
Query ID: ...
Answer: Based on the legal provisions...
Confidence: 0.95
✓ All tests completed
```

#### Test Frontend
1. Open browser: http://localhost:3000
2. Type query: "What are fundamental rights under Article 19?"
3. Click "Ask Question"
4. Should see response with citations

---

## 🎯 Quick Reference

### Backend Endpoints

| Endpoint | URL | Purpose |
|----------|-----|---------|
| API Docs | http://localhost:8000/api/docs | Interactive API testing |
| Health Check | http://localhost:8000/health | Server status |
| Root | http://localhost:8000/ | API info |
| Legal Query | POST /api/v1/query/legal | Main query endpoint |
| Suggestions | GET /api/v1/query/suggestions | Query suggestions |

### Frontend Pages

| Page | URL | Purpose |
|------|-----|---------|
| Dashboard | http://localhost:3000/ | Main interface |
| Research | http://localhost:3000/research | Research workspace |
| Tools | http://localhost:3000/tools | Legal tools |
| Settings | http://localhost:3000/settings | User settings |

---

## 🧪 Testing Workflow

### Method 1: Browser (Recommended)
1. **Frontend**: http://localhost:3000
2. Type question in search box
3. Click "Ask Question"
4. View results with citations

### Method 2: API Docs
1. Visit: http://localhost:8000/api/docs
2. Expand `/api/v1/query/legal`
3. Click "Try it out"
4. Enter test query
5. Click "Execute"

### Method 3: Python Script
```python
import requests

response = requests.post(
    "http://localhost:8000/api/v1/query/legal",
    json={
        "query": "What is Article 21?",
        "jurisdiction": "all",
        "codeType": "all",
        "yearRange": "all"
    }
)

print(response.json())
```

### Method 4: curl
```bash
curl -X POST http://localhost:8000/api/v1/query/legal \
  -H "Content-Type: application/json" \
  -d '{"query":"What is Article 21?"}'
```

---

## 📊 System Status Check

### Is Backend Running?
```powershell
# Check if port 8000 is listening
netstat -ano | findstr :8000

# Or try
curl http://localhost:8000/health
```

### Is Frontend Running?
```powershell
# Check if port 3000 is listening
netstat -ano | findstr :3000

# Or visit
# http://localhost:3000
```

### Check Logs
**Backend logs:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete
```

**Frontend logs:**
```
  VITE ready in 1234 ms
  ➜  Local:   http://localhost:3000/
```

---

## 🐛 Troubleshooting

### Backend Won't Start

**Error: "Address already in use"**
```powershell
# Kill process on port 8000
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Or use different port
uvicorn app.main:app --reload --port 8001
```

**Error: "Module not found"**
```powershell
# Reinstall dependencies
pip install -r requirements.txt

# Check Python version
python --version  # Should be 3.11+
```

**Error: "Cannot connect to database"**
```powershell
# For development, database is optional
# Mock responses work without database
# Update .env if needed
```

### Frontend Won't Start

**Error: "Port 3000 already in use"**
```powershell
# Kill process on port 3000
netstat -ano | findstr :3000
taskkill /PID <PID> /F

# Or use different port in vite.config.ts
```

**Error: "Cannot GET /"**
- Clear browser cache
- Check if dev server is running
- Restart frontend: Ctrl+C → npm run dev

### API Returns Errors

**422 Validation Error**
- Check request body format
- Ensure required fields present
- See /api/docs for schema

**500 Internal Server Error**
- Check backend logs
- Verify environment variables
- Check OPENAI_API_KEY if using real LLM

### Frontend Shows No Results

**Check:**
1. Backend is running (http://localhost:8000/health)
2. CORS is configured (should be by default)
3. Browser console for errors (F12)
4. Network tab shows 200 response

---

## 🔄 Development Workflow

### Making Changes

**Backend Code Changes:**
1. Edit files in `backend/app/`
2. Server auto-reloads (--reload flag)
3. Test with: http://localhost:8000/api/docs

**Frontend Code Changes:**
1. Edit files in `frontend/src/`
2. Vite auto-reloads
3. See changes at: http://localhost:3000

### Adding New API Endpoint

1. Create route in `backend/app/api/routes/`
2. Add to router in `main.py`
3. Test at `/api/docs`
4. Update frontend API calls

### Database Changes

```powershell
# Create migration
alembic revision --autogenerate -m "description"

# Apply migration
alembic upgrade head

# Or just recreate
python scripts\init_db.py
```

---

## 🎨 Demo Queries

Try these questions:

### Constitutional Law
- "What does Article 19 guarantee?"
- "Can I file a writ petition under Article 32?"
- "What is the right to equality under Article 14?"

### Criminal Law
- "What is Section 302 IPC?"
- "Can police arrest without warrant?"
- "What is sedition law in India?"

### Civil Rights
- "What are fundamental rights?"
- "Can government restrict my speech?"
- "How does habeas corpus work?"

---

## 📈 Performance Monitoring

### Response Time
```python
import time
start = time.time()
response = requests.post(...)
elapsed = (time.time() - start) * 1000
print(f"Response time: {elapsed:.0f}ms")
```

### Target Metrics
- Query response: <2000ms
- Confidence: >0.6 (60%)
- Citations: 1-5 per answer
- Sources: 2-10 per query

---

## 🎓 Understanding the Response

### Sample Response Structure
```json
{
  "id": "unique-query-id",
  "query": "Your question",
  "answer": "Legal answer with [CITATION: id] tags",
  "sources": [
    {
      "document_name": "Constitution of India",
      "section": "Article 19",
      "relevance_score": 0.95
    }
  ],
  "citations": [
    {
      "id": "cit-1",
      "text": "Article 19(1)(a)",
      "status": "active",
      "confidence": 0.99
    }
  ],
  "confidence": 0.95,
  "processing_time": 1847
}
```

### Interpreting Confidence
- **0.9-0.99**: High confidence (strong sources)
- **0.7-0.89**: Good confidence (multiple sources)
- **0.6-0.69**: Acceptable (minimum threshold)
- **<0.6**: Low confidence (insufficient sources)

---

## 🚦 Production Deployment

### Before Going Live

#### 1. Security
- [ ] Change SECRET_KEY in .env
- [ ] Set DEBUG=false
- [ ] Configure production CORS origins
- [ ] Enable HTTPS
- [ ] Set up rate limiting

#### 2. Infrastructure
- [ ] Deploy PostgreSQL database
- [ ] Set up Redis cache
- [ ] Configure Elasticsearch
- [ ] Create Pinecone index
- [ ] Set up monitoring

#### 3. Data
- [ ] Ingest legal documents
- [ ] Generate embeddings
- [ ] Index in vector DB
- [ ] Populate citation database

#### 4. Testing
- [ ] Run all unit tests
- [ ] Integration testing
- [ ] Load testing
- [ ] Security audit

---

## 📞 Support & Resources

### Documentation
- **Main README**: ../README.md
- **Backend README**: backend/README.md
- **Implementation Status**: backend/IMPLEMENTATION_STATUS.md
- **API Testing**: backend/API_TESTING.md
- **Complete Summary**: ../COMPLETE_IMPLEMENTATION_SUMMARY.md

### API Documentation
- **Interactive Docs**: http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc

### Logs Location
- **Backend**: Terminal where uvicorn is running
- **Frontend**: Terminal where npm dev is running
- **Browser**: F12 → Console tab

---

## ✅ Success Checklist

### You Know It's Working When:

**Backend:**
- [ ] http://localhost:8000/health returns 200
- [ ] /api/docs shows interactive documentation
- [ ] POST to /api/v1/query/legal returns answer

**Frontend:**
- [ ] http://localhost:3000 loads Dashboard
- [ ] Query interface accepts input
- [ ] Clicking "Ask Question" shows results
- [ ] Citations display correctly

**Integration:**
- [ ] Frontend → Backend communication works
- [ ] Mock responses display in UI
- [ ] No CORS errors in console
- [ ] Response time <3 seconds

---

## 🎉 You're Ready!

### Development Mode Active
```
Backend:  http://localhost:8000 ✅
Frontend: http://localhost:3000 ✅
API Docs: http://localhost:8000/api/docs ✅
```

### Start Building!
- Modify RAG pipeline
- Add new endpoints
- Customize frontend
- Train with real legal documents

---

**Constitutional AI** - Zero-Hallucination Legal Research ⚖️

*"In law, creativity is dangerous. We speak only with proof."*
