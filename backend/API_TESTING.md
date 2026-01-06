# Constitutional AI - Complete API Testing Guide

## 🧪 API Testing Instructions

### Prerequisites
1. Backend server running on http://localhost:8000
2. Python requests library installed
3. Frontend running on http://localhost:3000 (optional)

---

## Quick Test Commands

### Option 1: PowerShell (Windows)
```powershell
# Navigate to backend directory
cd backend

# Test health endpoint
Invoke-RestMethod -Uri "http://localhost:8000/health" -Method GET

# Test legal query
$body = @{
    query = "What are fundamental rights under Article 19?"
    jurisdiction = "all"
    codeType = "constitution"
    yearRange = "all"
    include_devil_advocate = $false
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/query/legal" -Method POST -Body $body -ContentType "application/json"
```

### Option 2: curl (Cross-platform)
```bash
# Health check
curl http://localhost:8000/health

# Legal query
curl -X POST http://localhost:8000/api/v1/query/legal \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What are fundamental rights under Article 19?",
    "jurisdiction": "all",
    "codeType": "constitution",
    "yearRange": "all",
    "include_devil_advocate": false
  }'
```

### Option 3: Python Script
```python
import requests
import json

# Test legal query
response = requests.post(
    "http://localhost:8000/api/v1/query/legal",
    json={
        "query": "What are fundamental rights under Article 19?",
        "jurisdiction": "all",
        "codeType": "constitution",
        "yearRange": "all",
        "include_devil_advocate": False
    }
)

print(json.dumps(response.json(), indent=2))
```

---

## Sample API Responses

### Health Check Response
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "service": "Constitutional AI API",
  "environment": "development"
}
```

### Legal Query Response
```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "query": "What are fundamental rights under Article 19?",
  "answer": "Based on the legal provisions...\n\nArticle 19 of the Constitution of India guarantees six fundamental rights...\n\n[CITATION: Article 19(1)(a)]...",
  "sources": [
    {
      "document_name": "Constitution of India",
      "document_type": "constitution",
      "section": "Article 19",
      "content": "Article 19: Protection of certain rights...",
      "relevance_score": 0.95,
      "metadata": {
        "effective_date": "1950-01-26",
        "authority": "supreme"
      }
    }
  ],
  "citations": [
    {
      "id": "cit-1",
      "text": "Article 19(1)(a), Constitution of India",
      "source": "Constitution of India",
      "section": "Article 19(1)(a)",
      "status": "active",
      "confidence": 0.99,
      "amendments": ["44th Amendment - 1978"]
    }
  ],
  "confidence": 0.95,
  "processing_time": 1847,
  "timestamp": "2024-01-06T10:30:00.000Z"
}
```

---

## Interactive API Documentation

Visit: **http://localhost:8000/api/docs**

Features:
- ✅ Try all endpoints interactively
- ✅ See request/response schemas
- ✅ Test with different parameters
- ✅ View error responses

---

## Test Scenarios

### 1. Basic Query
```json
{
  "query": "What is Article 21?",
  "jurisdiction": "all",
  "codeType": "all",
  "yearRange": "all"
}
```

### 2. Specific Jurisdiction
```json
{
  "query": "Can police arrest without warrant?",
  "jurisdiction": "delhi",
  "codeType": "crpc",
  "yearRange": "last_year"
}
```

### 3. With Devil's Advocate
```json
{
  "query": "Is sedition law constitutional?",
  "jurisdiction": "all",
  "codeType": "ipc",
  "include_devil_advocate": true
}
```

### 4. Complex Legal Question
```json
{
  "query": "Can I file a writ petition directly in Supreme Court under Article 32 for violation of fundamental rights?",
  "jurisdiction": "all_india",
  "codeType": "constitution",
  "yearRange": "all"
}
```

---

## Expected Behavior

### ✅ Successful Response
- Status code: 200
- Contains answer with citations
- Confidence score: 0.6-0.99
- Processing time: <3000ms
- Sources: 1-10 documents

### ⚠️ Low Confidence
- Confidence <0.6
- Answer: "I don't have verified sources..."
- Sources: 0-2 documents

### ❌ Error Response
- Status code: 400/500
- Error message in `detail` field
- No answer generated

---

## Monitoring Response Quality

### Check These Fields:
1. **Confidence** - Should be >0.6 for good answers
2. **Citations** - Every claim should have citation
3. **Sources** - Should have 3+ sources
4. **Processing Time** - Should be <2000ms
5. **Answer Format** - Should include [CITATION: ...] tags

---

## Common Issues

### Issue: "Cannot connect to API"
**Solution:**
```powershell
# Check if server is running
netstat -ano | findstr :8000

# Start server
uvicorn app.main:app --reload
```

### Issue: "422 Validation Error"
**Solution:** Check request body matches schema
```json
{
  "query": "string (required, min 5 chars)",
  "jurisdiction": "string (default: 'all')",
  "codeType": "string (default: 'all')",
  "yearRange": "string (default: 'all')",
  "include_devil_advocate": "boolean (default: false)"
}
```

### Issue: "500 Internal Server Error"
**Solution:** Check server logs for details
```powershell
# Server logs will show error details
# Common causes:
# - Missing environment variables
# - Database connection failed
# - LLM API key invalid
```

---

## Performance Testing

### Load Test with curl
```bash
# Send 10 concurrent requests
for i in {1..10}; do
  curl -X POST http://localhost:8000/api/v1/query/legal \
    -H "Content-Type: application/json" \
    -d '{"query":"What is Article 14?"}' &
done
```

### Monitor Response Times
```python
import requests
import time

times = []
for i in range(10):
    start = time.time()
    response = requests.post(
        "http://localhost:8000/api/v1/query/legal",
        json={"query": f"Test query {i}"}
    )
    elapsed = (time.time() - start) * 1000
    times.append(elapsed)
    print(f"Request {i+1}: {elapsed:.0f}ms")

print(f"\nAverage: {sum(times)/len(times):.0f}ms")
print(f"Max: {max(times):.0f}ms")
print(f"Min: {min(times):.0f}ms")
```

---

## Integration with Frontend

### Frontend Query Function
```javascript
async function queryLegalAPI(query, filters) {
  const response = await axios.post(
    'http://localhost:8000/api/v1/query/legal',
    {
      query,
      jurisdiction: filters.jurisdiction || 'all',
      codeType: filters.codeType || 'all',
      yearRange: filters.yearRange || 'all',
      include_devil_advocate: filters.devilAdvocate || false
    }
  );
  
  return response.data;
}
```

---

**Ready to Test! 🚀**

Start the server and visit http://localhost:8000/api/docs for interactive testing.
