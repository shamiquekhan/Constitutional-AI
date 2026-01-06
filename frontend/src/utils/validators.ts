/**
 * Validates legal query input
 */
export const validateQuery = (query: string): { valid: boolean; error?: string } => {
  if (!query || query.trim().length === 0) {
    return { valid: false, error: 'Query cannot be empty' };
  }

  if (query.length < 3) {
    return { valid: false, error: 'Query must be at least 3 characters long' };
  }

  if (query.length > 1000) {
    return { valid: false, error: 'Query is too long (max 1000 characters)' };
  }

  return { valid: true };
};

/**
 * Validates email format
 */
export const validateEmail = (email: string): boolean => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

/**
 * Validates citation format
 */
export const validateCitation = (citation: string): boolean => {
  // Basic validation for legal citation format
  // Can be expanded based on specific citation standards
  return citation.length > 0 && /[A-Za-z0-9]/.test(citation);
};

/**
 * Sanitizes user input to prevent XSS
 */
export const sanitizeInput = (input: string): string => {
  const div = document.createElement('div');
  div.textContent = input;
  return div.innerHTML;
};
