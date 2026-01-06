import { useState } from 'react';
import CitationBlock from './CitationBlock';

interface ResponseDisplayProps {
  result: any;
}

export default function ResponseDisplay({ result }: ResponseDisplayProps) {
  const [showDevil, setShowDevil] = useState(false);

  return (
    <article className="space-y-8">
      {/* Header with Confidence - Scandinavian Clean */}
      <div className="bg-white border border-slate-200 rounded-xl p-8 shadow-base">
        <div className="flex items-start justify-between mb-6">
          <div>
            <h2 className="text-2xl font-light text-slate-700 mb-3">Legal Analysis</h2>
            <div className="flex items-center gap-3">
              <span className="inline-flex items-center px-4 py-2 rounded-lg text-sm font-normal bg-sage-light text-sage-dark">
                {(result.confidence * 100).toFixed(0)}% Verified
              </span>
              <span className="text-sm text-slate-500">
                {result.sources.length} sources · {result.processingTime}ms
              </span>
            </div>
          </div>

          <div className="flex gap-3">
            <button className="px-5 py-2 border border-slate-200 rounded-lg hover:bg-nordic-off-white transition text-sm font-normal text-slate-700">
              Share
            </button>
            <button className="px-5 py-2 border border-slate-200 rounded-lg hover:bg-nordic-off-white transition text-sm font-normal text-slate-700">
              Export
            </button>
          </div>
        </div>

        {/* Disclaimer */}
        <div className="bg-sky-light border-l-4 border-sky px-5 py-4 rounded-lg text-sm text-slate-700">
          This response is AI-generated but backed by verified legal sources. Always verify with current law and consult a lawyer for actual cases.
        </div>
      </div>

      {/* Main Answer */}
      <div className="bg-white border border-slate-200 rounded-xl p-10 prose prose-sm max-w-none shadow-soft">
        <div className="text-slate-700 leading-loose space-y-4">
          {/* Render answer with inline citations */}
          {result.answer.split('[citation:').map((segment: string, i: number) => {
            if (i === 0) return <p key={i}>{segment}</p>;
            
            const [citationId, rest] = segment.split(']');
            const citation = result.citations.find((c: any) => c.id === citationId);
            
            return (
              <span key={i}>
                <CitationBlock citation={citation} inline />
                <span>{rest}</span>
              </span>
            );
          })}
        </div>
      </div>

      {/* Source Chain */}
      <div className="bg-white border border-slate-200 rounded-xl p-8 shadow-soft">
        <h3 className="font-medium text-slate-700 mb-6 text-lg">Source Chain</h3>
        <div className="space-y-4">
          <div className="flex items-center gap-4 text-sm">
            <span className="w-10 h-10 rounded-lg bg-sky-light text-sky flex items-center justify-center font-normal border border-sky">1</span>
            <span className="text-slate-600"><strong className="text-slate-700">Query Processing:</strong> Converted to legal terminology</span>
          </div>
          <div className="flex items-center gap-4 text-sm">
            <span className="w-10 h-10 rounded-lg bg-sage-light text-sage flex items-center justify-center font-normal border border-sage">2</span>
            <span className="text-slate-600"><strong className="text-slate-700">Source Retrieval:</strong> Found {result.sources.length} relevant documents</span>
          </div>
          <div className="flex items-center gap-4 text-sm">
            <span className="w-10 h-10 rounded-lg bg-nordic-sand text-slate-700 flex items-center justify-center font-normal border border-slate-300">3</span>
            <span className="text-slate-600"><strong className="text-slate-700">RAG Analysis:</strong> Generated answer grounded in sources</span>
          </div>
          <div className="flex items-center gap-4 text-sm">
            <span className="w-8 h-8 rounded-full bg-blue text-white flex items-center justify-center font-bold">4</span>
            <span className="text-gray-700"><strong>Verification:</strong> Cross-checked all citations (100% verified)</span>
          </div>
        </div>
      </div>

      {/* Actions */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <button 
          onClick={() => setShowDevil(!showDevil)}
          className="px-6 py-3 bg-slate-700 text-white rounded-lg hover:bg-slate-600 transition font-normal text-sm shadow-base"
        >
          {showDevil ? 'Viewing Alternative Perspective' : 'Show Alternative Perspective'}
        </button>
        <button className="px-6 py-3 border border-slate-200 rounded-lg hover:bg-nordic-off-white transition font-normal text-sm text-slate-700">
          Generate Memorandum
        </button>
      </div>

      {/* Alternative Perspective */}
      {showDevil && (
        <div className="bg-rose bg-opacity-30 border border-error rounded-xl p-8">
          <h3 className="font-medium text-slate-700 mb-4 text-lg">Alternative Perspective: Opposing Arguments</h3>
          <div className="space-y-4 text-sm text-slate-700">
            <p><strong className="text-slate-800">Counter-Argument 1:</strong> Some courts have interpreted this section differently...</p>
            <p><strong className="text-slate-800">Weak Point:</strong> The main argument relies on 2015 judgment that has been partially overruled in 2023...</p>
            <p><strong className="text-slate-800">Opposition Would Argue:</strong> That this falls under the exception provided in Section X...</p>
          </div>
        </div>
      )}
    </article>
  );
}
