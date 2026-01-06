export default function Settings() {
  return (
    <main className="min-h-screen bg-white">
      <div className="max-w-4xl mx-auto px-6 py-16">
        <h1 className="text-4xl font-bold text-navy mb-8">Settings</h1>
        
        <div className="space-y-6">
          <section className="bg-white border border-gray-100 rounded-lg p-6">
            <h2 className="text-xl font-semibold text-navy mb-4">Preferences</h2>
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Default Jurisdiction
                </label>
                <select className="w-full px-4 py-2 border border-gray-200 rounded-lg focus:border-blue outline-none">
                  <option>All India</option>
                  <option>Delhi</option>
                  <option>Bombay</option>
                  <option>Calcutta</option>
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Citation Format
                </label>
                <select className="w-full px-4 py-2 border border-gray-200 rounded-lg focus:border-blue outline-none">
                  <option>Blue Book</option>
                  <option>ALWD</option>
                  <option>Oxford</option>
                </select>
              </div>

              <div className="flex items-center gap-3">
                <input type="checkbox" id="autoVerify" className="w-4 h-4" />
                <label htmlFor="autoVerify" className="text-sm text-gray-700">
                  Auto-verify citations in responses
                </label>
              </div>

              <div className="flex items-center gap-3">
                <input type="checkbox" id="showDevil" className="w-4 h-4" defaultChecked />
                <label htmlFor="showDevil" className="text-sm text-gray-700">
                  Enable Devil's Advocate mode
                </label>
              </div>
            </div>
          </section>

          <section className="bg-white border border-gray-100 rounded-lg p-6">
            <h2 className="text-xl font-semibold text-navy mb-4">API Configuration</h2>
            <p className="text-sm text-gray-600 mb-4">
              Advanced settings for API integration
            </p>
            <button className="px-4 py-2 bg-gray-100 text-navy rounded-lg hover:bg-gray-200 transition text-sm font-semibold">
              Configure API Keys
            </button>
          </section>

          <div className="flex justify-end gap-4">
            <button className="px-6 py-2 border border-gray-200 rounded-lg hover:bg-gray-50 transition font-semibold">
              Cancel
            </button>
            <button className="px-6 py-2 bg-blue text-white rounded-lg hover:bg-navy transition font-semibold">
              Save Changes
            </button>
          </div>
        </div>
      </div>
    </main>
  );
}
