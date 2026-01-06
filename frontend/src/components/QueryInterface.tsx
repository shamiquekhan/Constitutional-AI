import { useState, useRef } from 'react';

interface QueryInterfaceProps {
  onQuery: (query: string, options?: any) => void;
  isLoading: boolean;
}

export default function QueryInterface({ onQuery, isLoading }: QueryInterfaceProps) {
  const [query, setQuery] = useState('');
  const [showAdvanced, setShowAdvanced] = useState(false);
  const [filters, setFilters] = useState({
    jurisdiction: 'all',
    codeType: 'all',
    yearRange: 'all'
  });
  const inputRef = useRef<HTMLTextAreaElement>(null);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (query.trim()) {
      onQuery(query, filters);
    }
  };

  const suggestions = [
    "Can I be arrested for speaking against the government?",
    "What is Section 498A IPC used for?",
    "How does the right to equality work under Article 14?",
    "What is the procedure for filing an FIR?",
    "What are the provisions for sexual harassment at workplace?"
  ];

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      {/* Main Input - Scandinavian Clean Design */}
      <div className="relative">
        <textarea
          ref={inputRef}
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask any legal question... e.g., 'What does Article 19 guarantee?'"
          className="w-full px-8 py-6 bg-white border border-slate-200 rounded-xl focus:border-sky focus:outline-none focus:ring-4 focus:ring-sky focus:ring-opacity-10 resize-none text-base text-slate-700 shadow-soft"
          rows={4}
          disabled={isLoading}
        />
        
        <div className="absolute bottom-4 right-4 flex gap-3">
          <button
            type="button"
            onClick={() => setShowAdvanced(!showAdvanced)}
            className="px-4 py-2 text-sm font-normal text-slate-600 hover:text-slate-900 transition bg-white border border-slate-200 rounded-lg"
          >
            {showAdvanced ? 'Hide Filters' : 'Show Filters'}
          </button>
          <button
            type="submit"
            disabled={isLoading || !query.trim()}
            className="px-8 py-2 bg-slate-700 text-white rounded-lg hover:bg-slate-600 disabled:opacity-50 disabled:cursor-not-allowed transition font-normal shadow-base"
          >
            {isLoading ? 'Searching...' : 'Search'}
          </button>
        </div>
      </div>

      {/* Suggestions */}
      <div className="flex flex-wrap gap-3">
        <span className="text-sm font-normal text-slate-500 self-center">Common Questions:</span>
        {suggestions.slice(0, 3).map((suggestion, i) => (
          <button
            key={i}
            type="button"
            onClick={() => {
              setQuery(suggestion);
              inputRef.current?.focus();
            }}
            className="text-sm px-4 py-2 bg-sky-light text-slate-700 rounded-lg hover:bg-sky hover:text-white transition border border-sky"
          >
            {suggestion.substring(0, 30)}...
          </button>
        ))}
      </div>

      {/* Advanced Options */}
      {showAdvanced && (
        <div className="bg-nordic-off-white border border-slate-200 rounded-xl p-8 space-y-6 shadow-soft">
          <h3 className="font-medium text-slate-700 text-lg">Filter Results</h3>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {/* Jurisdiction Filter */}
            <div>
              <label className="block text-sm font-normal text-slate-600 mb-2">
                Jurisdiction
              </label>
              <select
                value={filters.jurisdiction}
                onChange={(e) => setFilters({...filters, jurisdiction: e.target.value})}
                className="w-full px-4 py-3 border border-slate-200 rounded-lg focus:border-sky outline-none text-sm bg-white text-slate-700"
              >
                <option value="all">All India</option>
                <option value="delhi">Delhi</option>
                <option value="bombay">Bombay</option>
                <option value="calcutta">Calcutta</option>
                <option value="madras">Madras</option>
                <option value="punjab">Punjab & Haryana</option>
              </select>
            </div>

            {/* Code Type Filter */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Legal Code
              </label>
              <select
                value={filters.codeType}
                onChange={(e) => setFilters({...filters, codeType: e.target.value})}
                className="w-full px-3 py-2 border border-gray-200 rounded-lg focus:border-blue outline-none text-sm"
              >
                <option value="all">All</option>
                <option value="constitution">Constitution</option>
                <option value="ipc">IPC</option>
                <option value="crpc">CrPC</option>
                <option value="cpc">CPC</option>
              </select>
            </div>

            {/* Year Range */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Cases From
              </label>
              <select
                value={filters.yearRange}
                onChange={(e) => setFilters({...filters, yearRange: e.target.value})}
                className="w-full px-3 py-2 border border-gray-200 rounded-lg focus:border-blue outline-none text-sm"
              >
                <option value="all">Any Year</option>
                <option value="2024">Last Year</option>
                <option value="2021">Last 3 Years</option>
                <option value="2011">Last 10 Years</option>
              </select>
            </div>
          </div>
        </div>
      )}
    </form>
  );
}
