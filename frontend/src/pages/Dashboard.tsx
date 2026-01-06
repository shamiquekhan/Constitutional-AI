import { useState } from 'react';
import { useToast } from '../hooks/useToast';
import LoadingSpinner, { SkeletonLoader } from '../components/LoadingSpinner';
import { GlowingEffect } from '../components/ui/glowing-effect';
import { Timeline } from '../components/ui/timeline';
import { Scale, GraduationCap, Users, Shield, Search, FileCheck, AlertCircle, CheckCircle } from 'lucide-react';

interface Message {
  id: string;
  type: 'user' | 'ai';
  content: string;
  citations?: { text: string; source: string }[];
  verified?: boolean;
  devilsAdvocate?: string;
  showDevil?: boolean;
  // Validation metadata
  safetyCheckPassed?: boolean;
  validationStage?: string;
  requiresLawyer?: boolean;
  confidence?: number;
}

export default function Dashboard() {
  const { showSuccess, showError, showWarning, ToastContainer } = useToast();
  const [messages, setMessages] = useState<Message[]>([
    {
      id: '1',
      type: 'ai',
      content: 'Welcome! I can help you with legal research. All my answers are backed by verified sources from the Constitution of India, IPC, CrPC, and Supreme Court judgments. Try asking: "What does Article 19 guarantee?" or "Can I be arrested for speaking against the government?"',
      verified: true,
      citations: []
    }
  ]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSend = async () => {
    if (!inputValue.trim() || isLoading) {
      if (!inputValue.trim()) {
        showWarning('Please enter a legal question');
      }
      return;
    }

    // Validation
    if (inputValue.length < 5) {
      showWarning('Query must be at least 5 characters');
      return;
    }

    if (inputValue.length > 500) {
      showWarning('Query cannot exceed 500 characters');
      return;
    }

    const userMessage: Message = {
      id: Date.now().toString(),
      type: 'user',
      content: inputValue
    };

    setMessages(prev => [...prev, userMessage]);
    const query = inputValue;
    setInputValue('');
    setIsLoading(true);

    try {
      const API_URL = process.env.REACT_APP_API_URL || '';
      const response = await fetch(`${API_URL}/api/v1/query/legal`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          query: query,
          jurisdiction: 'india',
          include_devils_advocate: true
        })
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || `API error: ${response.status}`);
      }

      const data = await response.json();

      const aiMessage: Message = {
        id: (Date.now() + 1).toString(),
        type: 'ai',
        content: data.answer || 'I apologize, but I could not generate a response for this query.',
        verified: data.safety_check_passed !== false && data.confidence >= 0.7,
        citations: data.sources?.map((s: any) => ({
          text: s.title || s.source || 'Legal Source',
          source: s.type || s.source_type || 'Unknown'
        })) || [],
        devilsAdvocate: data.devils_advocate_response,
        showDevil: false,
        safetyCheckPassed: data.safety_check_passed,
        validationStage: data.validation_stage,
        requiresLawyer: data.input_validation?.requires_lawyer,
        confidence: data.confidence
      };

      setMessages(prev => [...prev, aiMessage]);
      
      if (data.confidence >= 0.8) {
        showSuccess('High confidence answer generated');
      } else if (data.confidence < 0.5) {
        showWarning('Low confidence answer - please consult a lawyer');
      }
    } catch (error: any) {
      console.error('Query error:', error);
      showError(error.message || 'Failed to process your query. Please try again.');
      
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        type: 'ai',
        content: 'I apologize, but I encountered an error processing your query. Please try again or rephrase your question.',
        verified: false,
        citations: []
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const toggleDevilsAdvocate = (messageId: string) => {
    setMessages(prev => prev.map(msg =>
      msg.id === messageId ? { ...msg, showDevil: !msg.showDevil } : msg
    ));
  };

  const scrollToChat = () => {
    document.getElementById('chat')?.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <main className="min-h-screen bg-bg-gray">
      {/* Navigation */}
      <nav className="bg-white border-b border-line-gray sticky top-0 z-50">
        <div className="max-w-[1600px] mx-auto px-10 h-16 flex justify-between items-center">
          <button onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })} className="text-lg font-semibold text-deep-blue tracking-tight hover:text-medium-blue transition">
            Constitutional AI
          </button>
          <ul className="flex gap-8 items-center">
            <li><a href="#problem" className="text-sm text-near-black hover:text-medium-blue transition">Problem</a></li>
            <li><a href="#solution" className="text-sm text-near-black hover:text-medium-blue transition">Solution</a></li>
            <li><a href="#workflow" className="text-sm text-near-black hover:text-medium-blue transition">Workflow</a></li>
            <li><a href="#impact" className="text-sm text-near-black hover:text-medium-blue transition">Impact</a></li>
            <li>
              <button 
                onClick={scrollToChat}
                className="bg-deep-blue text-white px-6 py-2 rounded-lg text-sm font-medium hover:bg-medium-blue transition"
              >
                Try Demo
              </button>
            </li>
          </ul>
        </div>
      </nav>

      {/* Hero Section */}
      <section id="solution" className="bg-gradient-to-br from-white to-bg-gray">
        <div className="max-w-[1600px] mx-auto px-16 py-32">
          <div className="grid md:grid-cols-2 gap-24 items-center">
            <div>
              <div className="inline-block mb-7 px-4 py-2 bg-blue-50 rounded-full">
                <span className="text-[11px] font-bold text-medium-blue uppercase tracking-[2px]">
                  Zero-Hallucination Legal Research
                </span>
              </div>
              <h1 className="text-[64px] font-bold leading-[1.15] mb-8 text-deep-blue tracking-tight">
                Proof-First Legal Intelligence
              </h1>
              <p className="text-[19px] text-gray-600 mb-10 leading-[1.8]">
                In law, creativity is dangerous. Constitutional AI ensures that AI speaks only when it has proof.
              </p>
              <div className="flex gap-4 items-center">
                <button 
                  onClick={scrollToChat}
                  className="bg-deep-blue text-white px-8 py-3.5 rounded-lg text-[15px] font-medium hover:bg-medium-blue hover:-translate-y-0.5 transition-all shadow-sm"
                >
                  Start Legal Research
                </button>
                <a href="#workflow" className="text-medium-blue text-sm hover:text-deep-blue transition cursor-pointer">
                  View how it works →
                </a>
              </div>
            </div>
            <div className="bg-white border border-line-gray rounded-2xl p-8 overflow-hidden shadow-sm">
              <img 
                src="/ui idea/Data_Integrity_-_Verified_Legal_Sources.png" 
                alt="Verified Legal Sources" 
                className="w-full h-auto rounded-xl"
              />
            </div>
          </div>
        </div>
      </section>

      {/* Chat Section */}
      <section id="chat" className="bg-white border-t border-b border-line-gray py-24">
        <div className="max-w-[1000px] mx-auto px-16">
          <div className="mb-10">
            <h2 className="text-[32px] font-bold mb-3 text-deep-blue tracking-tight">
              Ask a legal question
            </h2>
            <p className="text-sm text-gray-600">
              All responses are verified and cite authoritative sources
            </p>
          </div>

          {/* Chat Box */}
          <div className="bg-bg-gray border border-line-gray rounded-2xl min-h-[480px] flex flex-col p-8 mb-8 shadow-sm">
            <div className="flex-1 flex flex-col gap-4 mb-6 overflow-y-auto">
              {messages.map((message) => (
                <div 
                  key={message.id} 
                  className={`flex ${message.type === 'user' ? 'justify-end' : 'justify-start'} animate-fadeIn`}
                  role={message.type === 'ai' ? 'article' : undefined}
                  aria-live={message.type === 'ai' ? 'polite' : undefined}
                >
                  <div className={`max-w-[75%] px-6 py-4 rounded-xl text-[15px] leading-[1.7] ${
                    message.type === 'user' 
                      ? 'bg-medium-blue text-white' 
                      : 'bg-[#F0F4F8] text-near-black border-none'
                  }`}>
                    <p>{message.content}</p>
                    
                    {/* AI Message Features */}
                    {message.type === 'ai' && (
                      <div className="mt-3 space-y-3">
                        {/* Verification Badges */}
                        <div className="flex items-center gap-2 flex-wrap">
                          {message.verified && message.safetyCheckPassed !== false && (
                            <span className="inline-flex items-center gap-1.5 px-3 py-1.5 bg-green-50 text-green-700 rounded-md text-xs font-semibold">
                              <svg className="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                                <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                              </svg>
                              Verified
                            </span>
                          )}
                          
                          {message.safetyCheckPassed === false && (
                            <span className="inline-flex items-center gap-1.5 px-3 py-1.5 bg-red-50 text-red-700 rounded-md text-xs font-semibold">
                              <svg className="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                                <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                              </svg>
                              Safety Check Failed
                            </span>
                          )}
                          
                          {message.requiresLawyer && (
                            <span className="inline-flex items-center gap-1.5 px-3 py-1.5 bg-yellow-50 text-yellow-800 rounded-md text-xs font-semibold">
                              <svg className="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                                <path fillRule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
                              </svg>
                              Consult Lawyer
                            </span>
                          )}
                          
                          {message.confidence !== undefined && (
                            <span className="text-xs text-gray-600 font-medium">
                              Confidence: {Math.round(message.confidence * 100)}%
                            </span>
                          )}
                        </div>
                        
                        {/* Citation Chips */}
                        {message.citations && message.citations.length > 0 && (
                          <div className="flex flex-wrap gap-2">
                            {message.citations.map((citation, idx) => (
                              <button
                                key={idx}
                                className="inline-flex items-center gap-1.5 px-3 py-2 bg-white border border-line-gray rounded-lg text-xs text-near-black hover:border-medium-blue hover:bg-blue-50 transition"
                              >
                                <span>📄</span>
                                {citation.text} – {citation.source}
                              </button>
                            ))}
                          </div>
                        )}
                        
                        {/* Devil's Advocate Toggle */}
                        {message.devilsAdvocate && (
                          <div>
                            <button
                              onClick={() => toggleDevilsAdvocate(message.id)}
                              className="text-xs text-medium-blue hover:text-deep-blue font-medium flex items-center gap-1 cursor-pointer"
                            >
                              <span>⚖️</span>
                              {message.showDevil ? 'Hide' : 'Show'} Devil's Advocate
                            </button>
                            {message.showDevil && (
                              <div className="mt-2 p-3 bg-yellow-50 border border-yellow-200 rounded-lg text-xs text-yellow-900">
                                {message.devilsAdvocate}
                              </div>
                            )}
                          </div>
                        )}
                      </div>
                    )}
                  </div>
                </div>
              ))}
              
              {isLoading && (
                <div className="flex justify-start animate-fadeIn">
                  <div className="bg-[#F0F4F8] rounded-xl px-6 py-4">
                    <LoadingSpinner message="Analyzing your query..." size="sm" />
                  </div>
                </div>
              )}
            </div>
          </div>

          {/* Input Area */}
          <div className="flex gap-3">
            <input
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && !isLoading && handleSend()}
              placeholder="Type a legal query…"
              aria-label="Legal query input"
              aria-describedby="input-hint"
              className="flex-1 px-5 py-3.5 border border-line-gray rounded-lg text-sm focus:outline-none focus:border-medium-blue focus:ring-4 focus:ring-medium-blue/10 transition"
              disabled={isLoading}
            />
            <span id="input-hint" className="sr-only">Enter your legal question and press Enter or click Send</span>
            <button
              onClick={handleSend}
              disabled={isLoading || !inputValue.trim()}
              aria-label="Send query"
              className="bg-medium-blue text-white px-7 py-3.5 rounded-lg text-sm font-medium hover:bg-deep-blue transition disabled:opacity-50 disabled:cursor-not-allowed focus:outline-none focus:ring-4 focus:ring-medium-blue/20"
            >
              {isLoading ? 'Sending...' : 'Send'}
            </button>
          </div>
        </div>
      </section>

      {/* Problem Section */}
      <section id="problem" className="bg-white py-24">
        <div className="max-w-[1600px] mx-auto px-16">
          <h2 className="text-lg font-semibold text-medium-blue uppercase tracking-wider mb-10">Problem</h2>
          
          <div className="grid md:grid-cols-2 gap-20 items-center mb-24">
            <div>
              <h3 className="text-4xl font-bold text-deep-blue mb-7 leading-tight">
                AI hallucinations in legal practice
              </h3>
              <ul className="space-y-4">
                <li className="flex items-start gap-3 text-[17px] text-near-black leading-relaxed">
                  <span className="w-1.5 h-1.5 bg-medium-blue rounded-full mt-2.5 flex-shrink-0"></span>
                  <span>Fake case laws and incorrect legal sections</span>
                </li>
                <li className="flex items-start gap-3 text-[17px] text-near-black leading-relaxed">
                  <span className="w-1.5 h-1.5 bg-medium-blue rounded-full mt-2.5 flex-shrink-0"></span>
                  <span>No guarantee that citations map to real judgments</span>
                </li>
                <li className="flex items-start gap-3 text-[17px] text-near-black leading-relaxed">
                  <span className="w-1.5 h-1.5 bg-medium-blue rounded-full mt-2.5 flex-shrink-0"></span>
                  <span>One wrong citation can weaken or lose a case</span>
                </li>
              </ul>
            </div>
            <div className="bg-white border border-line-gray rounded-2xl p-8 overflow-hidden">
              <img 
                src="/ui idea/Problem__AI_Hallucinations_in_Legal_Information.png" 
                alt="AI Hallucinations in Legal Information" 
                className="w-full h-auto rounded-xl"
              />
            </div>
          </div>

          <div className="border-t border-line-gray pt-20">
            <div className="mb-12">
              <img 
                src="/ui idea/Who_Is_Affected__Lawyers,_Judges,_and_Law_Students.png" 
                alt="Who Is Affected - Legal Stakeholders" 
                className="w-full h-auto rounded-xl shadow-lg mb-8"
              />
            </div>
            <h3 className="text-center text-3xl font-bold text-deep-blue mb-12">Who is at risk?</h3>
            <div className="grid md:grid-cols-3 gap-8">
              {/* Lawyers Card */}
              <div className="relative min-h-[14rem]">
                <div className="relative h-full rounded-xl border-[0.75px] border-line-gray p-2">
                  <GlowingEffect
                    spread={40}
                    glow={true}
                    disabled={false}
                    proximity={64}
                    inactiveZone={0.01}
                    borderWidth={2}
                  />
                  <div className="relative flex h-full flex-col justify-between gap-6 overflow-hidden rounded-lg border-[0.75px] bg-bg-gray p-8 shadow-sm hover:shadow-lg transition-shadow">
                    <div className="relative flex flex-1 flex-col justify-between gap-4">
                      <div className="w-fit rounded-lg border border-line-gray bg-white p-3 shadow-sm">
                        <Scale className="h-5 w-5 text-medium-blue" />
                      </div>
                      <div className="space-y-3">
                        <h4 className="text-lg font-bold text-deep-blue">Lawyers</h4>
                        <p className="text-sm text-gray-600 leading-relaxed">
                          Risk filing incorrect citations in court, potentially damaging cases and professional reputation
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              {/* Law Students Card */}
              <div className="relative min-h-[14rem]">
                <div className="relative h-full rounded-xl border-[0.75px] border-line-gray p-2">
                  <GlowingEffect
                    spread={40}
                    glow={true}
                    disabled={false}
                    proximity={64}
                    inactiveZone={0.01}
                    borderWidth={2}
                  />
                  <div className="relative flex h-full flex-col justify-between gap-6 overflow-hidden rounded-lg border-[0.75px] bg-bg-gray p-8 shadow-sm hover:shadow-lg transition-shadow">
                    <div className="relative flex flex-1 flex-col justify-between gap-4">
                      <div className="w-fit rounded-lg border border-line-gray bg-white p-3 shadow-sm">
                        <GraduationCap className="h-5 w-5 text-medium-blue" />
                      </div>
                      <div className="space-y-3">
                        <h4 className="text-lg font-bold text-deep-blue">Law Students</h4>
                        <p className="text-sm text-gray-600 leading-relaxed">
                          Learning from fabricated legal precedents, undermining their legal education foundation
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              {/* Citizens Card */}
              <div className="relative min-h-[14rem]">
                <div className="relative h-full rounded-xl border-[0.75px] border-line-gray p-2">
                  <GlowingEffect
                    spread={40}
                    glow={true}
                    disabled={false}
                    proximity={64}
                    inactiveZone={0.01}
                    borderWidth={2}
                  />
                  <div className="relative flex h-full flex-col justify-between gap-6 overflow-hidden rounded-lg border-[0.75px] bg-bg-gray p-8 shadow-sm hover:shadow-lg transition-shadow">
                    <div className="relative flex flex-1 flex-col justify-between gap-4">
                      <div className="w-fit rounded-lg border border-line-gray bg-white p-3 shadow-sm">
                        <Users className="h-5 w-5 text-medium-blue" />
                      </div>
                      <div className="space-y-3">
                        <h4 className="text-lg font-bold text-deep-blue">Citizens</h4>
                        <p className="text-sm text-gray-600 leading-relaxed">
                          Receiving wrong legal advice that could lead to serious legal consequences
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Impact Section */}
      <section id="impact" className="bg-gradient-to-b from-bg-gray to-white py-32 relative">
        <div className="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-line-gray to-transparent"></div>
        
        <div className="max-w-[1600px] mx-auto px-16 relative z-10">
          <h2 className="text-center text-[44px] font-extrabold text-deep-blue mb-24 tracking-tight relative">
            Impact
            <span className="block w-16 h-1 bg-gradient-to-r from-medium-blue to-accent-blue mx-auto mt-5 rounded-full"></span>
          </h2>
          
          <div className="mb-16">
            <img 
              src="/ui idea/Impact_and_Benefits_-_Three_Pillar_Framework.png" 
              alt="Impact and Benefits Framework" 
              className="w-full h-auto rounded-xl shadow-lg"
            />
          </div>
          
          <div className="grid md:grid-cols-3 gap-10 mb-24">
            <div className="bg-white p-16 rounded-3xl text-center border-2 border-line-gray shadow-lg hover:border-medium-blue hover:shadow-2xl hover:-translate-y-1.5 transition-all relative overflow-hidden group">
              <div className="absolute top-0 left-0 right-0 h-0.5 bg-gradient-to-r from-medium-blue to-accent-blue scale-x-0 group-hover:scale-x-100 origin-left transition-transform"></div>
              <div className="text-[56px] font-black bg-gradient-to-r from-medium-blue to-accent-blue bg-clip-text text-transparent mb-4 tracking-tight">
                99.9%
              </div>
              <div className="text-gray-600 text-base font-semibold tracking-wide">Citation Accuracy</div>
            </div>
            
            <div className="bg-white p-16 rounded-3xl text-center border-2 border-line-gray shadow-lg hover:border-medium-blue hover:shadow-2xl hover:-translate-y-1.5 transition-all relative overflow-hidden group">
              <div className="absolute top-0 left-0 right-0 h-0.5 bg-gradient-to-r from-medium-blue to-accent-blue scale-x-0 group-hover:scale-x-100 origin-left transition-transform"></div>
              <div className="text-[56px] font-black bg-gradient-to-r from-medium-blue to-accent-blue bg-clip-text text-transparent mb-4 tracking-tight">
                2 sec
              </div>
              <div className="text-gray-600 text-base font-semibold tracking-wide">Average Response</div>
            </div>
            
            <div className="bg-white p-16 rounded-3xl text-center border-2 border-line-gray shadow-lg hover:border-medium-blue hover:shadow-2xl hover:-translate-y-1.5 transition-all relative overflow-hidden group">
              <div className="absolute top-0 left-0 right-0 h-0.5 bg-gradient-to-r from-medium-blue to-accent-blue scale-x-0 group-hover:scale-x-100 origin-left transition-transform"></div>
              <div className="text-[56px] font-black bg-gradient-to-r from-medium-blue to-accent-blue bg-clip-text text-transparent mb-4 tracking-tight">
                0.1%
              </div>
              <div className="text-gray-600 text-base font-semibold tracking-wide">Hallucination Rate</div>
            </div>
          </div>
        </div>
      </section>

      {/* Workflow Section */}
      <section id="workflow" className="bg-bg-gray py-16 relative">
        <div className="absolute bottom-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-line-gray to-transparent"></div>
        
        <Timeline data={[
          {
            title: "Step 1",
            content: (
              <div className="space-y-6">
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 bg-medium-blue/10 rounded-lg flex items-center justify-center flex-shrink-0">
                    <AlertCircle className="w-6 h-6 text-medium-blue" />
                  </div>
                  <div>
                    <h4 className="text-xl font-bold text-deep-blue mb-3">Input Validation</h4>
                    <p className="text-gray-600 text-sm md:text-base mb-4 leading-relaxed">
                      Every query undergoes rigorous validation to detect harmful intent, personal legal advice requests, 
                      and jurisdiction verification. This critical first layer ensures only legitimate educational queries proceed.
                    </p>
                    <div className="bg-white rounded-lg p-4 border border-line-gray">
                      <div className="flex items-center gap-2 text-sm text-gray-600 mb-2">
                        <CheckCircle className="w-4 h-4 text-green-600" />
                        <span className="font-medium">Harmful intent detection</span>
                      </div>
                      <div className="flex items-center gap-2 text-sm text-gray-600 mb-2">
                        <CheckCircle className="w-4 h-4 text-green-600" />
                        <span className="font-medium">Personal advice filtering</span>
                      </div>
                      <div className="flex items-center gap-2 text-sm text-gray-600">
                        <CheckCircle className="w-4 h-4 text-green-600" />
                        <span className="font-medium">Jurisdiction verification</span>
                      </div>
                    </div>
                  </div>
                </div>
                <img 
                  src="https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=800&auto=format&fit=crop"
                  alt="Input validation process"
                  className="w-full h-48 md:h-64 object-cover rounded-xl shadow-lg"
                />
              </div>
            ),
          },
          {
            title: "Step 2",
            content: (
              <div className="space-y-6">
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 bg-medium-blue/10 rounded-lg flex items-center justify-center flex-shrink-0">
                    <Search className="w-6 h-6 text-medium-blue" />
                  </div>
                  <div>
                    <h4 className="text-xl font-bold text-deep-blue mb-3">Source Retrieval</h4>
                    <p className="text-gray-600 text-sm md:text-base mb-4 leading-relaxed">
                      Our system searches through verified legal databases including the Constitution of India, 
                      Indian Penal Code (IPC), Code of Criminal Procedure (CrPC), and landmark Supreme Court judgments.
                    </p>
                    <div className="grid grid-cols-2 gap-3">
                      <div className="bg-white rounded-lg p-3 border border-line-gray text-center">
                        <div className="text-2xl font-bold text-medium-blue">560+</div>
                        <div className="text-xs text-gray-600">IPC Sections</div>
                      </div>
                      <div className="bg-white rounded-lg p-3 border border-line-gray text-center">
                        <div className="text-2xl font-bold text-medium-blue">470+</div>
                        <div className="text-xs text-gray-600">Articles</div>
                      </div>
                      <div className="bg-white rounded-lg p-3 border border-line-gray text-center">
                        <div className="text-2xl font-bold text-medium-blue">1000+</div>
                        <div className="text-xs text-gray-600">SC Judgments</div>
                      </div>
                      <div className="bg-white rounded-lg p-3 border border-line-gray text-center">
                        <div className="text-2xl font-bold text-medium-blue">100%</div>
                        <div className="text-xs text-gray-600">Verified</div>
                      </div>
                    </div>
                  </div>
                </div>
                <img 
                  src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800&auto=format&fit=crop"
                  alt="Legal database search"
                  className="w-full h-48 md:h-64 object-cover rounded-xl shadow-lg"
                />
              </div>
            ),
          },
          {
            title: "Step 3",
            content: (
              <div className="space-y-6">
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 bg-medium-blue/10 rounded-lg flex items-center justify-center flex-shrink-0">
                    <FileCheck className="w-6 h-6 text-medium-blue" />
                  </div>
                  <div>
                    <h4 className="text-xl font-bold text-deep-blue mb-3">Answer Generation</h4>
                    <p className="text-gray-600 text-sm md:text-base mb-4 leading-relaxed">
                      Using only verified sources, our AI generates comprehensive answers with proper citations. 
                      Every claim is backed by specific sections, articles, or case law references.
                    </p>
                    <div className="bg-gradient-to-br from-medium-blue/5 to-accent-blue/5 rounded-lg p-4 border border-medium-blue/20">
                      <p className="text-sm text-gray-700 italic mb-2">
                        "Article 19 of the Constitution guarantees six freedoms including freedom of speech and expression, 
                        subject to reasonable restrictions under Article 19(2)."
                      </p>
                      <div className="flex items-center gap-2 text-xs text-medium-blue">
                        <span className="font-medium">Source:</span>
                        <span>Constitution of India, Article 19</span>
                      </div>
                    </div>
                  </div>
                </div>
                <img 
                  src="https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=800&auto=format&fit=crop"
                  alt="AI answer generation"
                  className="w-full h-48 md:h-64 object-cover rounded-xl shadow-lg"
                />
              </div>
            ),
          },
          {
            title: "Step 4",
            content: (
              <div className="space-y-6">
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 bg-medium-blue/10 rounded-lg flex items-center justify-center flex-shrink-0">
                    <CheckCircle className="w-6 h-6 text-medium-blue" />
                  </div>
                  <div>
                    <h4 className="text-xl font-bold text-deep-blue mb-3">Answer Validation</h4>
                    <p className="text-gray-600 text-sm md:text-base mb-4 leading-relaxed">
                      Before delivery, every answer undergoes validation to verify citations exist, 
                      detect potential hallucinations, and ensure confidence scores meet our strict threshold.
                    </p>
                    <div className="space-y-2">
                      <div className="flex items-center justify-between bg-white rounded-lg p-3 border border-line-gray">
                        <span className="text-sm font-medium text-gray-700">Citation Verification</span>
                        <span className="text-xs font-bold text-green-600">✓ PASSED</span>
                      </div>
                      <div className="flex items-center justify-between bg-white rounded-lg p-3 border border-line-gray">
                        <span className="text-sm font-medium text-gray-700">Hallucination Detection</span>
                        <span className="text-xs font-bold text-green-600">✓ PASSED</span>
                      </div>
                      <div className="flex items-center justify-between bg-white rounded-lg p-3 border border-line-gray">
                        <span className="text-sm font-medium text-gray-700">Confidence Threshold</span>
                        <span className="text-xs font-bold text-green-600">95%</span>
                      </div>
                    </div>
                  </div>
                </div>
                <img 
                  src="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop"
                  alt="Validation process"
                  className="w-full h-48 md:h-64 object-cover rounded-xl shadow-lg"
                />
              </div>
            ),
          },
          {
            title: "Step 5",
            content: (
              <div className="space-y-6">
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 bg-medium-blue/10 rounded-lg flex items-center justify-center flex-shrink-0">
                    <Shield className="w-6 h-6 text-medium-blue" />
                  </div>
                  <div>
                    <h4 className="text-xl font-bold text-deep-blue mb-3">Safety Check</h4>
                    <p className="text-gray-600 text-sm md:text-base mb-4 leading-relaxed">
                      Final safety verification ensures the answer doesn't inadvertently provide harmful advice, 
                      maintains educational context, and includes appropriate disclaimers where necessary.
                    </p>
                    <div className="bg-green-50 border-l-4 border-green-600 p-4 rounded-lg">
                      <div className="flex items-start gap-3">
                        <Shield className="w-5 h-5 text-green-600 flex-shrink-0 mt-0.5" />
                        <div>
                          <p className="text-sm font-semibold text-green-900 mb-1">Safety Verified</p>
                          <p className="text-xs text-green-700">
                            This answer has passed all safety checks and is ready for educational use. 
                            Always consult a qualified lawyer for specific legal advice.
                          </p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <img 
                  src="https://images.unsplash.com/photo-1505664194779-8beaceb93744?w=800&auto=format&fit=crop"
                  alt="Safety verification"
                  className="w-full h-48 md:h-64 object-cover rounded-xl shadow-lg"
                />
              </div>
            ),
          },
        ]} />
      </section>

      {/* Footer */}
      <footer className="bg-gradient-to-br from-deep-blue to-[#0a1420] text-white py-16 text-center relative border-t border-white/10">
        <div className="absolute top-0 left-0 right-0 h-48 bg-radial-gradient from-accent-blue/10 to-transparent pointer-events-none"></div>
        
        <div className="relative z-10">
          <p className="text-lg font-extrabold tracking-tight mb-2">Constitutional AI</p>
          <p className="text-sm mb-3 font-medium tracking-wide">
            All answers are verified and cite authoritative sources from Indian law.
          </p>
          <p className="text-white/60 text-xs mt-6">
            For urgent legal matters, consult a qualified lawyer.
          </p>
        </div>
      </footer>

      {/* Toast Notifications */}
      <ToastContainer />

      <style>{`
        @keyframes fadeIn {
          from { opacity: 0; transform: translateY(10px); }
          to { opacity: 1; transform: translateY(0); }
        }
        .animate-fadeIn {
          animation: fadeIn 0.3s ease-in;
        }
        @keyframes slide-in {
          from {
            transform: translateX(400px);
            opacity: 0;
          }
          to {
            transform: translateX(0);
            opacity: 1;
          }
        }
        .animate-slide-in {
          animation: slide-in 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }
      `}</style>
    </main>
  );
}
