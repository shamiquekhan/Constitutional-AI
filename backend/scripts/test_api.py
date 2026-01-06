"""
Test API Endpoints
Quick test script to verify API functionality
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    print("\n=== Testing Health Endpoint ===")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def test_legal_query():
    """Test legal query endpoint"""
    print("\n=== Testing Legal Query ===")
    
    query_data = {
        "query": "What are fundamental rights under Article 19?",
        "jurisdiction": "all",
        "codeType": "constitution",
        "yearRange": "all",
        "include_devil_advocate": False
    }
    
    response = requests.post(
        f"{BASE_URL}/api/v1/query/legal",
        json=query_data
    )
    
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Query ID: {result['id']}")
        print(f"Answer: {result['answer'][:200]}...")
        print(f"Confidence: {result['confidence']}")
        print(f"Sources: {len(result['sources'])}")
        print(f"Citations: {len(result['citations'])}")
        print(f"Processing Time: {result['processing_time']}ms")
    else:
        print(f"Error: {response.text}")

def test_suggestions():
    """Test query suggestions"""
    print("\n=== Testing Query Suggestions ===")
    response = requests.get(f"{BASE_URL}/api/v1/query/suggestions")
    print(f"Status: {response.status_code}")
    print(f"Suggestions: {json.dumps(response.json(), indent=2)}")

if __name__ == "__main__":
    print("Constitutional AI - API Test Suite")
    print("=" * 50)
    
    try:
        test_health()
        test_legal_query()
        test_suggestions()
        
        print("\n" + "=" * 50)
        print("✓ All tests completed")
    
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Cannot connect to API server")
        print("Make sure the server is running: uvicorn app.main:app --reload")
    except Exception as e:
        print(f"\n❌ Error: {e}")
