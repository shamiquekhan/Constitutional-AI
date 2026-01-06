/**
 * Formats citation text for display
 */
export const formatCitation = (citation: string): string => {
  // Add proper formatting for legal citations
  return citation.trim();
};

/**
 * Formats date to readable format
 */
export const formatDate = (dateString: string): string => {
  const date = new Date(dateString);
  return date.toLocaleDateString('en-IN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });
};

/**
 * Truncates text to specified length
 */
export const truncateText = (text: string, maxLength: number): string => {
  if (text.length <= maxLength) return text;
  return text.substring(0, maxLength) + '...';
};

/**
 * Highlights search terms in text
 */
export const highlightText = (text: string, searchTerm: string): string => {
  if (!searchTerm) return text;
  const regex = new RegExp(`(${searchTerm})`, 'gi');
  return text.replace(regex, '<mark>$1</mark>');
};

/**
 * Formats confidence score as percentage
 */
export const formatConfidence = (score: number): string => {
  return `${(score * 100).toFixed(1)}%`;
};

/**
 * Exports content as PDF (placeholder)
 */
export const exportAsPDF = async (_content: string, filename: string): Promise<void> => {
  // TODO: Implement PDF export functionality
  console.log('Exporting as PDF:', filename);
};

/**
 * Exports content as DOCX (placeholder)
 */
export const exportAsDOCX = async (_content: string, filename: string): Promise<void> => {
  // TODO: Implement DOCX export functionality
  console.log('Exporting as DOCX:', filename);
};

/**
 * Copies text to clipboard
 */
export const copyToClipboard = async (text: string): Promise<boolean> => {
  try {
    await navigator.clipboard.writeText(text);
    return true;
  } catch (err) {
    console.error('Failed to copy to clipboard:', err);
    return false;
  }
};
