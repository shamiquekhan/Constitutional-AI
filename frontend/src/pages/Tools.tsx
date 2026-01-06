export default function Tools() {
  return (
    <main className="min-h-screen bg-white">
      <div className="max-w-6xl mx-auto px-6 py-16">
        <h1 className="text-4xl font-bold text-navy mb-8">Legal Tools</h1>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="bg-white border border-gray-100 rounded-lg p-6 hover:shadow-lg transition">
            <div className="text-3xl mb-4">⚖️</div>
            <h3 className="text-xl font-semibold text-navy mb-3">Devil's Advocate</h3>
            <p className="text-gray-600 text-sm mb-4">
              Generate opposing arguments for any legal position
            </p>
            <button className="px-4 py-2 bg-blue text-white rounded-lg hover:bg-navy transition text-sm font-semibold">
              Coming Soon
            </button>
          </div>

          <div className="bg-white border border-gray-100 rounded-lg p-6 hover:shadow-lg transition">
            <div className="text-3xl mb-4">📄</div>
            <h3 className="text-xl font-semibold text-navy mb-3">Memorandum Generator</h3>
            <p className="text-gray-600 text-sm mb-4">
              Auto-generate legal memos with verified citations
            </p>
            <button className="px-4 py-2 bg-blue text-white rounded-lg hover:bg-navy transition text-sm font-semibold">
              Coming Soon
            </button>
          </div>

          <div className="bg-white border border-gray-100 rounded-lg p-6 hover:shadow-lg transition">
            <div className="text-3xl mb-4">🔍</div>
            <h3 className="text-xl font-semibold text-navy mb-3">Citation Verifier</h3>
            <p className="text-gray-600 text-sm mb-4">
              Verify legal citations and check current status
            </p>
            <button className="px-4 py-2 bg-blue text-white rounded-lg hover:bg-navy transition text-sm font-semibold">
              Coming Soon
            </button>
          </div>

          <div className="bg-white border border-gray-100 rounded-lg p-6 hover:shadow-lg transition">
            <div className="text-3xl mb-4">📊</div>
            <h3 className="text-xl font-semibold text-navy mb-3">Analytics Dashboard</h3>
            <p className="text-gray-600 text-sm mb-4">
              Track research efficiency and time saved
            </p>
            <button className="px-4 py-2 bg-blue text-white rounded-lg hover:bg-navy transition text-sm font-semibold">
              Coming Soon
            </button>
          </div>
        </div>
      </div>
    </main>
  );
}
