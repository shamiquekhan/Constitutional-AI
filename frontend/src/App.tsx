import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Research from './pages/Research';
import Tools from './pages/Tools';
import Settings from './pages/Settings';
import './styles/globals.css';

export default function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gradient-to-br from-off-white via-white to-gray-100">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/research" element={<Research />} />
          <Route path="/tools" element={<Tools />} />
          <Route path="/settings" element={<Settings />} />
        </Routes>
      </div>
    </Router>
  );
}
