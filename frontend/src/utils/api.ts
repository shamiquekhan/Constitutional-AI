import axios, { AxiosInstance } from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

// Create axios instance with default config
const apiClient: AxiosInstance = axios.create({
  baseURL: `${API_BASE_URL}/api/v1`,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor
apiClient.interceptors.request.use(
  (config) => {
    // Add auth token if exists
    const token = localStorage.getItem('authToken');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Handle unauthorized
      localStorage.removeItem('authToken');
      window.location.href = '/';
    }
    return Promise.reject(error);
  }
);

// API methods
export const api = {
  // Query endpoints
  query: {
    legal: (queryData: { query: string; jurisdiction?: string }) =>
      apiClient.post('/query/legal', queryData),
    get: (queryId: string) => apiClient.get(`/query/${queryId}`),
    suggestions: (partialQuery: string) =>
      apiClient.get('/suggestions', { params: { partial_query: partialQuery } }),
  },

  // Citation endpoints
  citations: {
    get: (citationId: string) => apiClient.get(`/citations/${citationId}`),
    verify: (citations: string[]) => apiClient.post('/citations/verify', { citations }),
    getStatus: (section: string) => apiClient.get(`/citations/status/${section}`),
  },

  // Devil's Advocate endpoint
  devilsAdvocate: (answer: string) => apiClient.post('/devils-advocate', { answer }),

  // Memorandum endpoints
  memorandum: {
    generate: (issue: string) => apiClient.post('/memorandum/generate', { issue }),
  },

  // Analytics endpoints
  analytics: {
    dashboard: () => apiClient.get('/analytics/dashboard'),
    efficiencyReport: () => apiClient.get('/analytics/efficiency-report'),
  },
};

export default apiClient;
