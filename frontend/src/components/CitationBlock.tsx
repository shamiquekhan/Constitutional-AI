import { useState } from 'react';

interface CitationBlockProps {
  citation: any;
  inline?: boolean;
}

const getStatusColor = (status: string) => {
  switch(status) {
    case 'active': return 'sage';
    case 'amended': return 'ochre';
    case 'repealed': return 'error';
    default: return 'sky';
  }
};

const getStatusText = (status: string) => {
  switch(status) {
    case 'active': return 'Active';
    case 'amended': return 'Amended';
    case 'repealed': return 'Repealed';
    default: return 'Info';
  }
};

export default function CitationBlock({ citation, inline }: CitationBlockProps) {
  const [showModal, setShowModal] = useState(false);
  const statusColor = getStatusColor(citation?.status || 'active');

  if (!citation) return null;

  if (inline) {
    return (
      <>
        <button
          onClick={() => setShowModal(true)}
          className="inline px-2 py-1 rounded text-sky font-normal hover:text-sky-dark hover:bg-sky-light cursor-pointer transition"
        >
          [{citation.id}]
        </button>

        {showModal && (
          <div className="fixed inset-0 bg-slate-900 bg-opacity-30 backdrop-blur-sm flex items-center justify-center z-50 p-4">
            <div className="bg-white rounded-2xl max-w-2xl w-full max-h-[80vh] overflow-y-auto shadow-xl border border-slate-200">
              <div className="sticky top-0 bg-nordic-off-white border-b border-slate-200 p-8 flex justify-between items-start">
                <div>
                  <h3 className="text-xl font-medium text-slate-700">{citation.text}</h3>
                  <p className="text-sm text-slate-500 mt-2">{citation.source}</p>
                </div>
                <button
                  onClick={() => setShowModal(false)}
                  className="text-3xl text-slate-400 hover:text-slate-700 leading-none"
                >
                  ×
                </button>
              </div>

              <div className="p-8 space-y-6">
                {/* Citation Status */}
                <div className="flex items-center gap-3">
                  <span className={`inline-flex items-center px-4 py-2 rounded-lg text-sm font-normal bg-${statusColor}-light text-${statusColor}-dark border border-${statusColor}`}>
                    {getStatusText(citation.status)} · {citation.status?.toUpperCase() || 'ACTIVE'}
                  </span>
                  <span className="text-sm text-slate-500">Confidence: {((citation.confidence || 0.95) * 100).toFixed(0)}%</span>
                </div>

                {/* Full Text */}
                <div className="bg-nordic-off-white p-6 rounded-xl border-l-4 border-sky">
                  <p className="text-sm text-slate-700 leading-relaxed">
                    {citation.text || 'Citation content will be displayed here.'}
                  </p>
                </div>

                {/* Metadata */}
                <div className="grid grid-cols-2 gap-6 text-sm">
                  <div>
                    <p className="text-slate-500 font-normal mb-1">Section</p>
                    <p className="text-slate-700 font-medium">{citation.section || 'N/A'}</p>
                  </div>
                  <div>
                    <p className="text-gray-600 font-medium">Status</p>
                    <p className="text-navy font-semibold">{citation.status || 'Active'}</p>
                  </div>
                </div>

                {/* Amendments */}
                {citation.amendments && citation.amendments.length > 0 && (
                  <div>
                    <p className="text-sm font-medium text-gray-700 mb-2">Amendments:</p>
                    <ul className="space-y-2">
                      {citation.amendments.map((amendment: string, i: number) => (
                        <li key={i} className="text-sm text-gray-600 flex items-start gap-2">
                          <span className="text-warning">⚠</span>
                          <span>{amendment}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            </div>
          </div>
        )}
      </>
    );
  }

  return (
    <div className="bg-white border border-gray-100 rounded-lg p-4 hover:shadow-md transition cursor-pointer" onClick={() => setShowModal(true)}>
      <div className="flex items-start justify-between mb-3">
        <div>
          <p className="font-semibold text-navy text-sm">{citation.text}</p>
          <p className="text-xs text-gray-500">{citation.source}</p>
        </div>
        <span className={`inline-flex items-center px-2 py-1 rounded text-xs font-semibold bg-${statusColor} bg-opacity-10 text-${statusColor}`}>
          {getStatusText(citation.status)}
        </span>
      </div>
    </div>
  );
}
