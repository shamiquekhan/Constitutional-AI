import { useState } from 'react';
import { Link } from 'react-router-dom';

export default function Navigation() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  return (
    <nav className="sticky top-0 z-40 bg-white border-b border-line-gray backdrop-blur-sm bg-opacity-95">
      <div className="max-w-7xl mx-auto px-8 py-4 flex items-center justify-between">
        {/* Logo - Simple Wordmark */}
        <Link to="/" className="flex items-center">
          <span className="text-xl font-normal text-deep-blue tracking-tight">Constitutional AI</span>
        </Link>

        {/* Desktop Menu */}
        <div className="hidden md:flex items-center gap-8">
          <a href="#problem" className="text-near-black hover:text-medium-blue font-normal transition text-sm">
            Problem
          </a>
          <a href="#solution" className="text-near-black hover:text-medium-blue font-normal transition text-sm">
            Solution
          </a>
          <a href="#workflow" className="text-near-black hover:text-medium-blue font-normal transition text-sm">
            Workflow
          </a>
          <a href="#impact" className="text-near-black hover:text-medium-blue font-normal transition text-sm">
            Impact
          </a>
          <button className="px-6 py-2 bg-deep-blue text-white rounded-lg hover:bg-medium-blue transition font-normal text-sm">
            Try Demo
          </button>
        </div>

        {/* Mobile Menu Button */}
        <button
          className="md:hidden"
          onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
        >
          <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </button>
      </div>

      {/* Mobile Menu */}
      {mobileMenuOpen && (
        <div className="md:hidden border-t border-line-gray bg-bg-gray p-4 space-y-2">
          <a href="#problem" className="block text-near-black font-normal hover:bg-white p-3 rounded-lg transition">Problem</a>
          <a href="#solution" className="block text-near-black font-normal hover:bg-white p-3 rounded-lg transition">Solution</a>
          <a href="#workflow" className="block text-near-black font-normal hover:bg-white p-3 rounded-lg transition">Workflow</a>
          <a href="#impact" className="block text-near-black font-normal hover:bg-white p-3 rounded-lg transition">Impact</a>
        </div>
      )}
    </nav>
  );
}
