# 🌐 The Human Graph

## Plataforma de Inteligência Organizacional & Gestão de Risco

O **The Human Graph** é um ecossistema moderno focado em DHO (Desenvolvimento Humano e Organizacional) que transcende a tradicional gestão de feedbacks. Utilizando uma arquitetura de banco de dados duplo e análise preditiva, a plataforma mapeia não apenas as competências técnicas dos colaboradores, mas a verdadeira teia de influência e comunicação corporativa, permitindo a identificação precoce de silos, riscos de evasão e sobrecarga de trabalho.

---

## 🚀 Principais Funcionalidades (v1.0)

* **Arquitetura de Dados Híbrida:** Persistência transacional local (SQLite/PostgreSQL) operando em sincronia com um banco de dados de Grafos em nuvem (Neo4j).
* **Organizational Network Analysis (ONA):** Cada colaborador é um "Nó" e cada feedback é uma "Aresta". O sistema mapeia o fluxo real de comunicação e influência dentro da empresa.
* **Motor NLP de Risco:** Uma inteligência artificial (Mock NLP) embarcada na API analisa o sentimento e o contexto das mensagens enviadas, calculando em tempo real o **Risco de Burnout e Evasão** (score de 0.0 a 1.0) baseado em indicadores de estresse corporativo.
* **Dashboard Executivo Premium:** Interface de alta performance focada em experiência do usuário (UX), projetada com Dark Mode e micro-interações para visualização fluida de KPIs e alertas do DHO.

---

## 🛠️ Stack Tecnológica

O projeto foi construído separando as responsabilidades de interface e processamento de dados, garantindo escalabilidade e governança estrutural.

### Back-end (Motor Lógico)

* **Python 3.x**
* **FastAPI:** Framework de altíssimo desempenho para construção de APIs.
* **SQLAlchemy (SQLite):** ORM para o mapeamento e persistência relacional.
* **Neo4j (AuraDB):** Banco de dados orientado a grafos para análise topológica da organização.
* **Pydantic:** Validação de dados e tipagem rigorosa.

### Front-end (Interface Visual)

* **Next.js 14+ (App Router):** Framework React para renderização otimizada.
* **Tailwind CSS:** Estilização utilitária para construção rápida de interfaces customizadas e responsivas.
* **React:** Construção de componentes UI interativos.

---

## ⚙️ Como rodar o projeto localmente

Para rodar a plataforma, você precisará de dois terminais abertos simultaneamente (um para a API e outro para a Aplicação Web). É necessário ter o Node.js e o Python instalados em sua máquina, além de uma conta gratuita no **Neo4j AuraDB**.

### 1. Configurando o Back-end (API)

```bash
# Navegue até a pasta da API
cd the-human-graph-api

# Crie e ative o ambiente virtual
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate

# Instale as dependências
pip install fastapi uvicorn pydantic sqlalchemy neo4j

# Configure suas credenciais do Neo4j no arquivo graph_db.py

# Inicie o servidor da API
uvicorn main:app --reload
A API estará rodando em: http://127.0.0.1:8000. Acesse /docs para visualizar o Swagger interativo.

2. Configurando o Front-end (Web)
Bash
# Navegue até a pasta do Front-end
cd the-human-graph-web

# Instale as dependências do Node
npm install

# Inicie o servidor de desenvolvimento
npm run dev
O Dashboard estará disponível em: http://localhost:3000.

🛣️ Roadmap / Próximos Passos
[ ] Integrar a API do Back-end com o Front-end Next.js utilizando fetch/axios para popular os dados dinamicamente.

[ ] Implementar visualização 3D/2D interativa do grafo gerado no Neo4j na interface do usuário.

[ ] Substituir o Mock NLP pela API da OpenAI (GPT-4o) para análise de sentimento semântica avançada.

[ ] Incorporar gráficos de Business Intelligence para métricas de risco por departamento.

Desenvolvido por molz3ra corp. Projetando o futuro da gestão corporativa através de Sistemas de Informação e Design Funcional!
