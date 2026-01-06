/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./public/index.html"
  ],
  theme: {
    extend: {
      colors: {
        // Scandinavian Black-Blue-Gray Palette
        'deep-blue': '#0D1B2A',
        'medium-blue': '#1B4F72',
        'accent-blue': '#2D7A8E',
        'near-black': '#111111',
        'line-gray': '#E1E5EA',
        'bg-gray': '#F5F7FA',
        'card-white': '#FFFFFF',
        // Extended Blues
        'scandi-blue': {
          50: '#E8EDF2',
          100: '#D1DBE5',
          200: '#A3B7CB',
          300: '#7593B1',
          400: '#476F97',
          500: '#1B4F72',
          600: '#163F5B',
          700: '#112F44',
          800: '#0D1F2D',
          900: '#0D1B2A',
        },
        // Status Colors
        success: '#10B981',
        warning: '#F59E0B',
        error: '#EF4444',
        info: '#3B82F6'
      },
      fontFamily: {
        sans: ['-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'sans-serif'],
        mono: ['IBM Plex Mono', 'Monaco', 'Courier New', 'monospace']
      },
      fontSize: {
        'xs': '12px',
        'sm': '14px',
        'base': '16px',
        'lg': '18px',
        'xl': '20px',
        '2xl': '24px',
        '3xl': '28px',
        '4xl': '32px',
        '5xl': '36px'
      },
      fontWeight: {
        regular: 400,
        medium: 500,
        semibold: 600,
        bold: 700
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms')
  ],
}
