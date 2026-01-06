# Constitutional AI - API Documentation

## Base URL
```
Development: http://localhost:8000/api/v1
Production: https://api.constitutional-ai.com/api/v1
```

## Authentication

Most endpoints require authentication via JWT token:
```http
Authorization: Bearer <your-token>
```

## Endpoints

### Query Endpoints

#### POST /query/legal
Submit a legal query for processing.

**Request:**
```json
{
  "query": "What is Article 19 of the Constitution?",
  "jurisdiction": "delhi",
  "filters": {
    "document_type": "constitution",
    "year_range": [1950, 2024]
  }
}
```

**Response:**
```json
{
  "query_id": "uuid-here",
  "query": "What is Article 19 of the Constitution?",
  "answer": "Article 19 of the Constitution of India guarantees six fundamental rights...",
  "confidence": 0.95,
  "confidence_level": "high",
  "sources": [
    {
      "document_name": "Constitution of India",
      "document_type": "constitution",
      "section": "Article 19",
      "content": "Full text of Article 19...",
      "relevance_score": 0.98,
      "metadata": {}
    }
  ],
  "citations": [
    {
      "id": "citation-1",
      "text": "Article 19(1)(a), Constitution of India",
      "source": "Constitution of India",
      "section": "Article 19(1)(a)",
      "status": "active",
      "confidence": 0.99
    }
  ],
  "warnings": [],
  "processing_time": 1.5,
  "timestamp": "2026-01-06T10:00:00Z"
}
```

#### GET /query/{query_id}
Retrieve previous query results.

**Response:** Same as POST /query/legal

#### GET /suggestions
Get query suggestions.

**Query Parameters:**
- `partial_query` (string): Partial query text

**Response:**
```json
{
  "suggestions": [
    "What is Article 14?",
    "Explain Section 420 IPC",
    "Can I file a case under Article 32?"
  ]
}
```

### Citation Endpoints

#### GET /citations/{citation_id}
Get detailed information about a citation.

**Response:**
```json
{
  "citation_id": "citation-1",
  "full_text": "Full text of the cited provision...",
  "source_document": "Constitution of India",
  "section": "Article 19(1)(a)",
  "status": "active",
  "effective_date": "1950-01-26",
  "amendment_history": [
    {
      "amendment": "44th Amendment",
      "date": "1978-06-20",
      "changes": "Modified text..."
    }
  ],
  "related_cases": [
    "Maneka Gandhi v. Union of India (1978)"
  ],
  "context": "Surrounding sections and context..."
}
```

#### POST /citations/verify
Verify multiple citations.

**Request:**
```json
{
  "citations": [
    "Article 19(1)(a)",
    "Section 420 IPC",
    "Article 32"
  ]
}
```

**Response:**
```json
[
  {
    "citation": "Article 19(1)(a)",
    "status": "active",
    "valid": true,
    "confidence": 0.99,
    "last_updated": "2024-01-01",
    "amendments": ["44th Amendment - 1978"],
    "warning": null
  },
  {
    "citation": "Section 420 IPC",
    "status": "amended",
    "valid": true,
    "confidence": 0.95,
    "last_updated": "2023-12-01",
    "amendments": ["BNS 2023 - Now Section 318"],
    "warning": "This section has been renumbered in BNS 2023"
  }
]
```

#### GET /citations/status/{section}
Quick status check for a legal section.

**Response:**
```json
{
  "section": "Article 19(1)(a)",
  "status": "active",
  "last_verified": "2024-01-01"
}
```

### Devil's Advocate Endpoint

#### POST /devils-advocate
Generate opposing arguments.

**Request:**
```json
{
  "answer": "The original answer text...",
  "query": "Original query (optional)"
}
```

**Response:**
```json
{
  "original_answer": "The original answer...",
  "counter_arguments": [
    "Counter-argument 1 with citation",
    "Counter-argument 2 with citation"
  ],
  "weak_points": [
    "Weak point 1 in the argument",
    "Weak point 2 in the argument"
  ],
  "contradictory_precedents": [
    {
      "document_name": "Opposing Case Name",
      "relevance_score": 0.85,
      "content": "Relevant excerpt..."
    }
  ],
  "alternative_interpretations": [
    "Alternative interpretation 1",
    "Alternative interpretation 2"
  ]
}
```

### Memorandum Endpoints

#### POST /memorandum/generate
Generate a legal memorandum.

**Request:**
```json
{
  "issue": "Whether the petitioner can claim relief under Article 226?",
  "facts": "Optional facts of the case..."
}
```

**Response:**
```json
{
  "memorandum_id": "memo-uuid",
  "issue": "Whether the petitioner can claim relief under Article 226?",
  "rule": "Article 226 of the Constitution grants High Courts the power...",
  "application": "In the present case, applying Article 226...",
  "conclusion": "Based on the above analysis, the petitioner can claim relief...",
  "citations": [
    {
      "id": "citation-1",
      "text": "Article 226, Constitution of India",
      "source": "Constitution of India",
      "status": "active",
      "confidence": 0.99
    }
  ],
  "full_text": "LEGAL MEMORANDUM\n\nISSUE:\n...\n\nRULE:\n...",
  "generated_at": "2026-01-06T10:00:00Z"
}
```

### Analytics Endpoints

#### GET /analytics/dashboard
Get user dashboard analytics.

**Response:**
```json
{
  "total_queries": 150,
  "citations_verified": 450,
  "time_saved_hours": 75,
  "accuracy_rate": 0.98,
  "recent_queries": [...]
}
```

#### GET /analytics/efficiency-report
Get efficiency report.

**Response:**
```json
{
  "traditional_research_time": 120,
  "ai_research_time": 25,
  "time_saved": 95,
  "efficiency_gain": "79%",
  "cost_savings": "$950"
}
```

## Error Responses

All endpoints return errors in this format:

```json
{
  "detail": "Error message describing what went wrong"
}
```

### HTTP Status Codes
- `200 OK` - Success
- `201 Created` - Resource created
- `400 Bad Request` - Invalid input
- `401 Unauthorized` - Authentication required
- `403 Forbidden` - Insufficient permissions
- `404 Not Found` - Resource not found
- `422 Unprocessable Entity` - Validation error
- `429 Too Many Requests` - Rate limit exceeded
- `500 Internal Server Error` - Server error

## Rate Limiting

- **Unauthenticated**: 10 requests/minute
- **Authenticated**: 100 requests/minute
- **Premium**: 1000 requests/minute

Rate limit headers:
```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1641024000
```

## Pagination

Endpoints that return lists support pagination:

**Query Parameters:**
- `page` (integer): Page number (default: 1)
- `page_size` (integer): Items per page (default: 20, max: 100)

**Response includes:**
```json
{
  "total": 150,
  "page": 1,
  "page_size": 20,
  "pages": 8,
  "results": [...]
}
```

## Webhooks

Subscribe to events (future feature):
- `query.completed`
- `citation.updated`
- `verification.failed`

## SDKs

Official SDKs available for:
- Python
- JavaScript/TypeScript
- Java (planned)

---

**API Version:** 1.0.0  
**Last Updated:** January 2026  
**Interactive Docs:** http://localhost:8000/api/docs
