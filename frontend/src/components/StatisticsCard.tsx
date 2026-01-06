interface StatisticsCardProps {
  number: string;
  label: string;
  icon?: string;
}

export default function StatisticsCard({ number, label }: StatisticsCardProps) {
  return (
    <div className="bg-white border border-slate-200 rounded-xl p-8 text-center hover:shadow-lg transition-shadow">
      <div className="text-4xl font-light text-slate-700 mb-3">{number}</div>
      <div className="text-slate-600 text-sm font-normal">{label}</div>
    </div>
  );
}
