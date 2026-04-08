import React from 'react';

export default function Home() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-200 p-8 font-sans">
      
      {/* Topbar com Perfil e Status da API */}
      <div className="flex justify-between items-center mb-12 border-b border-slate-800 pb-6">
        <header>
          <h1 className="text-4xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-emerald-400 to-cyan-400">
            The Human Graph
          </h1>
          <p className="text-slate-400 mt-2">Plataforma de Inteligência Organizacional & Gestão de Risco</p>
        </header>
        
        <div className="flex items-center gap-4">
          <div className="flex items-center gap-2 bg-slate-900 border border-slate-800 px-4 py-2 rounded-full shadow-sm">
            <div className="w-2 h-2 bg-emerald-500 rounded-full animate-pulse"></div>
            <span className="text-xs text-slate-300 font-medium tracking-wide">API Conectada</span>
          </div>
          {/* Avatar do Usuário */}
          <div className="w-10 h-10 bg-gradient-to-br from-emerald-900 to-cyan-900 rounded-full border border-emerald-700/50 flex items-center justify-center text-sm font-bold text-emerald-100 shadow-lg cursor-pointer hover:scale-105 transition-transform">
            LM
          </div>
        </div>
      </div>

      {/* KPIs / Cards de Métricas */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
        <div className="bg-slate-900 p-6 rounded-xl border border-slate-800 shadow-lg hover:border-slate-700 transition-all cursor-default">
          <h3 className="text-slate-400 text-sm font-semibold mb-1">Total de Colaboradores</h3>
          <p className="text-3xl font-bold text-white">2</p>
        </div>
        
        <div className="bg-slate-900 p-6 rounded-xl border border-slate-800 shadow-lg hover:border-emerald-900 transition-all cursor-default">
          <h3 className="text-slate-400 text-sm font-semibold mb-1">Conexões Mapeadas no Grafo</h3>
          <p className="text-3xl font-bold text-emerald-400">1</p>
        </div>
        
        <div className="bg-slate-900 p-6 rounded-xl border border-slate-800 shadow-lg relative overflow-hidden cursor-default">
          <div className="absolute right-0 top-0 w-1 h-full bg-red-500/50"></div>
          <h3 className="text-slate-400 text-sm font-semibold mb-1">Risco de Evasão (Alerta)</h3>
          <p className="text-3xl font-bold text-red-400">15%</p>
        </div>
      </div>

      {/* Main Area: Mural de Feedbacks */}
      <div className="bg-slate-900 p-6 rounded-xl border border-slate-800 shadow-lg">
        <div className="flex justify-between items-center mb-6 border-b border-slate-800 pb-4">
          <h2 className="text-xl font-semibold text-slate-100">Mural de Reconhecimento Recente</h2>
          <button className="bg-emerald-600 hover:bg-emerald-500 text-white px-5 py-2 rounded-lg text-sm font-medium transition-all shadow-[0_0_15px_rgba(16,185,129,0.2)] hover:shadow-[0_0_20px_rgba(16,185,129,0.4)]">
            + Enviar Feedback
          </button>
        </div>
        
        <div className="space-y-4">
          {/* Exemplo de Feedback 1 (Positivo) */}
          <div className="bg-slate-950/50 p-5 rounded-lg border border-slate-800 flex flex-col gap-3 hover:bg-slate-950 transition-colors">
            <div className="flex justify-between items-start">
              <span className="font-medium text-emerald-300">Lucas M. → Ana T.</span>
              <span className="text-xs bg-emerald-900/30 text-emerald-400 py-1 px-3 rounded-full border border-emerald-800/50">
                Clean Code
              </span>
            </div>
            {/* Correção do ESLint: Uso de &quot; no lugar das aspas duplas */}
            <p className="text-sm text-slate-300 leading-relaxed italic">
              &quot;Mandou muito bem na refatoração de ontem, o código limpo ajudou muito a equipe a manter o prazo!&quot;
            </p>
            <div className="text-xs text-slate-500 font-medium">Há 2 horas</div>
          </div>

          {/* Exemplo de Feedback 2 (Alerta de Risco para IA) */}
          <div className="bg-slate-950/50 p-5 rounded-lg border border-slate-800 flex flex-col gap-3 border-l-2 border-l-red-500/50 hover:bg-slate-950 transition-colors">
            <div className="flex justify-between items-start">
              <span className="font-medium text-cyan-300">Ana T. → Carlos R.</span>
              <span className="text-xs bg-red-900/20 text-red-400 py-1 px-3 rounded-full border border-red-800/50">
                Resiliência
              </span>
            </div>
            {/* Correção do ESLint: Uso de &quot; */}
            <p className="text-sm text-slate-300 leading-relaxed italic">
              &quot;Parabéns por entregar o projeto. Sei que a sobrecarga foi enorme e a pressão nos gerou muito estresse e atraso.&quot;
            </p>
            <div className="text-xs text-slate-500 flex justify-between font-medium">
              <span>Há 5 horas</span>
              <span className="text-red-400/90 flex items-center gap-1.5 bg-red-900/10 px-2 py-0.5 rounded-md">
                <span className="text-[10px]">⚠️</span> IA detectou risco no tom da mensagem
              </span>
            </div>
          </div>
        </div>
      </div>

    </div>
  );
}