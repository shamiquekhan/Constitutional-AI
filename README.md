# Constitutional AI - Zero-Hallucination Legal Research

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/shamiquekhan/Constitutional-AI)

## Overview

Constitutional AI is a comprehensive legal research assistant that provides verified answers backed by the Constitution of India, IPC, CrPC, and Supreme Court judgments.

### Key Features

- **Zero-Hallucination Guarantee**: All answers backed by verified legal sources
- **5-Layer Validation Architecture**: Intent analysis, source retrieval, answer generation, validation, safety checks
- **Comprehensive Legal Database**: Constitution, IPC sections, Supreme Court judgments
- **Modern UI**: Professional Scandinavian design with gradient animations
- **Educational Intent Recognition**: Distinguishes educational questions from harmful intent

## Tech Stack

### Frontend
- React 18.2.0 + TypeScript
- Tailwind CSS
- Modern responsive design
- Professional UI with animations

### Backend
- FastAPI (Python 3.14)
- Comprehensive legal database
- 5-layer validation system
- Intent analysis engine

## Deployment

### Vercel Deployment (Frontend)

1. **Fork this repository**

2. **Deploy to Vercel**:
   ```bash
   # Install Vercel CLI
   npm i -g vercel
   
   # Deploy frontend
   cd frontend
   vercel
   ```

3. **Set Environment Variables** in Vercel Dashboard:
   - `REACT_APP_API_URL`: Your backend API URL

### Backend Deployment Options

#### Option 1: Railway.app
```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Deploy
cd backend
railway up
```

#### Option 2: Render.com
1. Create new Web Service
2. Connect GitHub repository
3. Set build command: `pip install -r requirements-minimal.txt`
4. Set start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

#### Option 3: Heroku
```bash
# Create Procfile in backend/
echo "web: uvicorn app.main:app --host 0.0.0.0 --port \$PORT" > backend/Procfile

# Deploy
heroku create constitutional-ai-backend
git subtree push --prefix backend heroku main
```

## Local Development

### Prerequisites
- Node.js 16+
- Python 3.10+

### Setup

1. **Clone repository**:
   ```bash
   git clone https://github.com/shamiquekhan/Constitutional-AI.git
   cd Constitutional-AI
   ```

2. **Backend setup**:
   ```bash
   cd backend
   pip install -r requirements-minimal.txt
   python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

3. **Frontend setup**:
   ```bash
   cd frontend
   npm install
   npm start
   ```

4. **Access the application**:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

## Project Structure

```
Constitutional-AI/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   │       └── query.py          # Main API endpoints
│   │   ├── core/
│   │   │   ├── legal_database.py     # Legal sources database
│   │   │   ├── legal_answer_generator.py
│   │   │   └── query_intent_analyzer.py
│   │   └── main.py                   # FastAPI application
│   └── requirements-minimal.txt
├── frontend/
│   ├── public/
│   │   ├── ui idea/                  # Design assets
│   │   └── ui style/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   │   └── Dashboard.tsx         # Main UI
│   │   └── App.tsx
│   └── package.json
└── README.md
```

## Features

### Educational Legal Research
- Article 19 (Freedom of Speech)
- Article 21 (Right to Life)
- Section 302 IPC (Murder)
- Section 304 IPC (Culpable Homicide)
- Section 307 IPC (Attempt to Murder)
- Supreme Court judgments with citations

### Safety Features
- Intent analysis (educational vs harmful)
- Comprehensive answer validation
- Citation verification
- Confidence scoring
- Educational disclaimers

## Sample Queries

**Constitutional Law**:
- "What does Article 19 guarantee?"
- "What does Article 21 protect?"

**Criminal Law**:
- "What will happen if I kill a person?"
- "What is the punishment for murder under IPC?"

**Case Law**:
- "What did the Supreme Court decide in Bachan Singh case?"

## API Documentation

### POST /api/v1/query/legal

**Request**:
```json
{
  "query": "What does Article 19 guarantee?"
}
```

**Response**:
```json
{
  "query": "What does Article 19 guarantee?",
  "answer": "[Comprehensive answer with citations]",
  "sources": [
    {
      "source": "Article 19 Constitution",
      "type": "constitution",
      "title": "Freedom of Speech and Expression"
    }
  ],
  "confidence": 0.90,
  "safety_check_passed": true,
  "processing_time_ms": 45.2
}
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Disclaimer

This application is for educational purposes only. For specific legal advice, please consult a qualified lawyer admitted to practice in India.

## Support

For issues and questions, please open an issue on GitHub.

## Acknowledgments

- Constitution of India
- Indian Penal Code
- Supreme Court of India judgments
- All contributors to this project
