interface SourceChainProps {
  sources: any[];
}

export default function SourceChain({ sources }: SourceChainProps) {
  return (
    <div className="bg-white border border-slate-200 rounded-xl p-8 shadow-soft">
      <h3 className="font-medium text-slate-700 mb-6 flex items-center gap-3 text-lg">
        <span className="w-10 h-10 rounded-lg bg-sky-light text-sky flex items-center justify-center text-sm font-normal border border-sky">
          <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
            <path fillRule="evenodd" d="M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z" clipRule="evenodd" />
          </svg>
        </span>
        Source Chain
      </h3>

      <div className="space-y-5">
        {sources.map((source, i) => (
          <div key={i} className="relative">
            {/* Connector Line */}
            {i < sources.length - 1 && (
              <div className="absolute left-5 top-14 w-0.5 h-10 bg-slate-200"></div>
            )}

            {/* Source Item */}
            <div className="flex gap-5">
              <div className="flex flex-col items-center">
                <div className="w-10 h-10 rounded-lg bg-nordic-off-white border border-slate-200 text-slate-700 flex items-center justify-center text-sm font-normal">
                  {i + 1}
                </div>
              </div>
              <div className="flex-1 pb-4">
                <p className="font-medium text-slate-700 text-sm">{source.document_name || `Source ${i + 1}`}</p>
                <p className="text-sm text-slate-500 mt-1">{source.document_type || 'Legal Document'}</p>
                <p className="text-sm text-slate-500 mt-2 flex items-center gap-2">
                  <span>Relevance: {((source.relevance_score || 0.9) * 100).toFixed(0)}%</span>
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Download Option */}
      <button className="w-full mt-6 px-5 py-3 border border-slate-200 rounded-lg hover:bg-nordic-off-white transition text-sm font-normal text-slate-700 flex items-center justify-center gap-2">
        <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
        </svg>
        Download Verification Report
      </button>
    </div>
  );
}
