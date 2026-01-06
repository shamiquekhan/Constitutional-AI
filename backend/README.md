# Constitutional AI Backend

Production-ready FastAPI backend with RAG (Retrieval-Augmented Generation) pipeline for legal research.

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Environment Setup
```bash
cp .env.example .env
# Edit .env with your API keys
```

Required environment variables:
- `OPENAI_API_KEY` - OpenAI API key for LLM
- `PINECONE_API_KEY` - Pinecone API key for vector DB
- `DATABASE_URL` - PostgreSQL connection string
- `REDIS_URL` - Redis connection string

### 3. Initialize Database
```bash
python scripts/init_db.py
```

### 4. Start Server
```bash
uvicorn app.main:app --reload
```

Server runs on: http://localhost:8000
API docs: http://localhost:8000/api/docs

## Architecture

### RAG Pipeline

```
Query → Retrieval (Hybrid) → Generation (Grounded) → Verification → Response
```

**Components:**
1. **Retriever** - Hybrid search (BM25 + Vector)
2. **Generator** - Grounded LLM with forced citations
3. **Verifier** - Citation validation & status checking

### API Endpoints

#### Query
- `POST /api/v1/query/legal` - Main legal query endpoint
- `GET /api/v1/query/suggestions` - Query suggestions
- `GET /api/v1/query/{query_id}` - Retrieve previous query

#### Citations
- `GET /api/v1/citations/{citation_id}` - Get citation details
- `POST /api/v1/citations/verify` - Verify citation status

#### Tools
- `POST /api/v1/devils-advocate` - Generate opposing arguments
- `POST /api/v1/memorandum` - Generate legal memo

## Project Structure

```
backend/
├── app/
│   ├── api/
│   │   └── routes/        # API endpoints
│   ├── core/              # Configuration
│   ├── database/          # Database models & session
│   ├── models/            # Pydantic schemas
│   ├── rag/               # RAG pipeline components
│   │   ├── retriever.py   # Hybrid search
│   │   ├── generator.py   # Grounded LLM
│   │   ├── vector_store.py
│   │   └── embeddings.py
│   └── services/          # Business logic
├── scripts/               # Utility scripts
├── tests/                 # Unit & integration tests
└── requirements.txt
```

## RAG Components

### 1. Retriever (`app/rag/retriever.py`)
- **Keyword Search**: BM25 via Elasticsearch
- **Semantic Search**: Vector similarity via Pinecone
- **Hybrid Ranking**: 0.4 keyword + 0.6 semantic
- **Re-ranking**: Authority level weighting
- **Citation Extraction**: Regex + NER

### 2. Generator (`app/rag/generator.py`)
- **Grounded Generation**: Forces LLM to cite sources
- **Temperature**: 0.1 (low for legal accuracy)
- **System Prompt**: Strict no-hallucination rules
- **Confidence Scoring**: Based on source quality

### 3. Verifier (`app/services/verification_service.py`)
- **Status Check**: Active/Amended/Repealed
- **Amendment History**: Track legal changes
- **Precedent Validation**: Check if cases overruled

## Testing

### Run Tests
```bash
pytest tests/ -v
```

### Test API Manually
```bash
python scripts/test_api.py
```

### Test Coverage
```bash
pytest --cov=app tests/
```

## Database

### Models
- `QueryHistory` - Stores all queries
- `CitationStatus` - Citation verification cache
- `LegalDocument` - Legal document metadata
- `User` - User accounts

### Migrations
```bash
# Create migration
alembic revision --autogenerate -m "description"

# Apply migration
alembic upgrade head
```

## Deployment

### Docker
```bash
docker-compose up -d
```

### Manual
```bash
# Production server
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## Development

### Code Style
```bash
# Format code
black app/

# Lint
flake8 app/

# Type check
mypy app/
```

### Debug Mode
```bash
DEBUG=true uvicorn app.main:app --reload --log-level debug
```

## Performance

- **Query Response Time**: <2 seconds average
- **Confidence Threshold**: 0.6 (60%)
- **Retrieval K**: 10 sources
- **Max Tokens**: 2048
- **Rate Limit**: 60 requests/minute

## Zero-Hallucination Promise

> "In law, creativity is dangerous. Constitutional AI ensures that AI speaks only when it has proof."

**Implementation:**
1. All answers MUST cite sources
2. LLM cannot generate without verified legal text
3. Citations verified against database
4. Confidence <60% = "I don't have verified sources"
5. Devil's Advocate mode shows counter-arguments

## Production Checklist

- [ ] Set strong `SECRET_KEY` in environment
- [ ] Configure production database
- [ ] Set up Redis for caching
- [ ] Configure Pinecone index
- [ ] Index legal documents
- [ ] Set up monitoring
- [ ] Configure CORS for production domain
- [ ] Enable HTTPS
- [ ] Set up logging
- [ ] Configure rate limiting

## License

MIT License - See LICENSE file
