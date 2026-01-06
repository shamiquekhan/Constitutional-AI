# Constitutional AI - Zero-Hallucination Legal Research Assistant

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Status](https://img.shields.io/badge/status-development-yellow.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🎯 Vision

Build a zero-hallucination legal research assistant using RAG (Retrieval-Augmented Generation) that serves lawyers, judges, law students, and legal researchers with verified sources and precise citations.

### Core Promise

> **"In law, creativity is dangerous. Constitutional AI ensures that AI speaks only when it has proof."**

## 🚀 Features

### Core Features
- ✅ **Verified-Source-Only Generation** - AI only responds using verified legal documents
- 🔗 **Clickable Citation System** - Every claim is backed by clickable citations
- ⚖️ **Devil's Advocate Mode** - Generates opposing arguments automatically
- 📊 **Source Chain Transparency** - Visual proof chain from query to answer
- 📝 **Legal Memorandum Generator** - Generates structured legal memos with verified citations
- ✔️ **Real-time Citation Verification** - Checks if laws are active, amended, or repealed

### Target Users
- 👨‍⚖️ Practicing Lawyers & Advocates
- 👨‍⚖️ Judges & Court Staff
- 📚 Law Students & Researchers
- 🏢 Law Firms & Legal Departments

## 🏗️ Tech Stack

### Frontend
- **Framework**: React 18+ with TypeScript
- **Styling**: Tailwind CSS
- **State Management**: Zustand
- **UI Components**: Radix UI, Headless UI
- **Charts**: Recharts, D3.js

### Backend
- **Framework**: FastAPI (Python 3.11+)
- **Database**: PostgreSQL + Redis
- **Search**: Elasticsearch
- **Vector DB**: Pinecone / Weaviate
- **LLM**: OpenAI GPT-4 / Claude 3

### Infrastructure
- **Containerization**: Docker + Docker Compose
- **Cloud**: AWS / GCP / Azure
- **CI/CD**: GitHub Actions

## 📦 Installation

### Prerequisites
- Node.js 18+
- Python 3.11+
- Docker & Docker Compose
- PostgreSQL 15+
- Redis 7+
- Elasticsearch 8+

### Quick Start with Docker

1. **Clone the repository**
```bash
git clone <repository-url>
cd "Constituional Ai"
```

2. **Set up environment variables**
```bash
# Frontend
cp frontend/.env.example frontend/.env

# Backend
cp backend/.env.example backend/.env
# Edit backend/.env and add your API keys
```

3. **Start all services**
```bash
cd docker
docker-compose up -d
```

4. **Access the application**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/api/docs

### Manual Setup

#### Frontend Setup
```bash
cd frontend
npm install
npm start
```

#### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 📁 Project Structure

```
constitutional-ai/
├── frontend/          # React TypeScript frontend
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── pages/        # Page components
│   │   ├── hooks/        # Custom hooks
│   │   ├── store/        # State management
│   │   ├── utils/        # Utility functions
│   │   └── styles/       # CSS and design system
│   └── public/           # Static assets
├── backend/           # FastAPI backend
│   ├── app/
│   │   ├── api/          # API routes
│   │   ├── core/         # Core configuration
│   │   ├── models/       # Data models
│   │   ├── rag/          # RAG pipeline
│   │   ├── services/     # Business logic
│   │   └── database/     # Database models
│   ├── tests/            # Test files
│   └── scripts/          # Utility scripts
├── docker/            # Docker configuration
├── docs/              # Documentation
└── scripts/           # Setup scripts
```

## 🔧 Configuration

### Environment Variables

#### Frontend (.env)
```env
REACT_APP_API_URL=http://localhost:8000
REACT_APP_ENVIRONMENT=development
```

#### Backend (.env)
```env
OPENAI_API_KEY=your-api-key
PINECONE_API_KEY=your-pinecone-key
DATABASE_URL=postgresql://user:pass@localhost:5432/constitutional_ai
REDIS_URL=redis://localhost:6379
```

## 📖 API Documentation

Once the backend is running, visit:
- Swagger UI: http://localhost:8000/api/docs
- ReDoc: http://localhost:8000/api/redoc

### Key Endpoints

- `POST /api/v1/query/legal` - Submit legal query
- `GET /api/v1/citations/{citation_id}` - Get citation details
- `POST /api/v1/citations/verify` - Verify citations
- `POST /api/v1/devils-advocate` - Generate opposing arguments
- `POST /api/v1/memorandum/generate` - Generate legal memorandum

## 🧪 Testing

### Frontend Tests
```bash
cd frontend
npm test
npm run test:coverage
```

### Backend Tests
```bash
cd backend
pytest
pytest --cov=app tests/
```

## 🚢 Deployment

### Production Build

```bash
# Build frontend
cd frontend
npm run build

# Build Docker images
cd docker
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up -d
```

## 📊 Project Roadmap

### Phase 1: Foundation (Weeks 1-2) ✅
- [x] Project structure setup
- [x] Frontend configuration
- [x] Backend configuration
- [x] Docker setup
- [x] Design system

### Phase 2: Core RAG Pipeline (Weeks 2-4)
- [ ] Document ingestion pipeline
- [ ] Vector database setup
- [ ] RAG retrieval implementation
- [ ] Citation verification system

### Phase 3: Features (Weeks 4-6)
- [ ] Query interface
- [ ] Citation viewer
- [ ] Devil's Advocate mode
- [ ] Memorandum generator

### Phase 4: Testing & Deployment (Weeks 7-8)
- [ ] Unit tests
- [ ] Integration tests
- [ ] Legal validation
- [ ] Production deployment

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For questions or support:
- Email: support@constitutional-ai.com
- GitHub Issues: [Create an issue](../../issues)
- Documentation: [View docs](docs/)

## 🙏 Acknowledgments

- Legal database sources
- OpenAI for LLM capabilities
- Open source community

---

**Status**: Development  
**Version**: 1.0.0  
**Last Updated**: January 2026

**Built with ⚖️ for the legal community**
