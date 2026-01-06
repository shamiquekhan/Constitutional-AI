import { useState, useCallback } from 'react';

export const useLegalQuery = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<any>(null);

  const query = useCallback(async (legalQuestion: string, options?: any) => {
    setIsLoading(true);
    setError(null);

    try {
      const API_URL = process.env.REACT_APP_API_URL || '';
      const response = await fetch(
        `${API_URL}/api/v1/query/legal`,
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ query: legalQuestion, ...options })
        }
      );

      if (!response.ok) {
        throw new Error(`API Error: ${response.statusText}`);
      }

      const data = await response.json();
      setResult(data);
      return data;
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Unknown error';
      setError(errorMessage);
      throw err;
    } finally {
      setIsLoading(false);
    }
  }, []);

  return { isLoading, error, result, query };
};
