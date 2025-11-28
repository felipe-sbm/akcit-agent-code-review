# 🤖 Akcit Code Review AI

Sistema de revisão de código com inteligência artificial, desenvolvido como projeto acadêmico da parceria **IMD/UFRN** e **Akcit**.

## 📋 Visão Geral

Este projeto combina um **frontend Blazor WebAssembly** com um **backend Python/FastAPI** para oferecer:

- 🔍 **Code Review**: Análise inteligente de código com sugestões de melhoria
- ✍️ **Redator de Matérias**: Escrita automática de artigos com pesquisa web
- ✅ **Checador de Fatos**: Verificação de afirmações com relatórios detalhados

## 🏗️ Arquitetura

```
akcit-agent-code-review/
│
├── frontend/                    # Blazor WebAssembly (.NET 9)
│   ├── Pages/                   # Páginas Razor
│   │   ├── Home.razor          # Página inicial
│   │   └── CodeReview.razor    # Interface de code review
│   ├── Layout/                  # Layouts e navegação
│   ├── wwwroot/                 # Assets estáticos
│   └── Program.cs              # Entry point
│
├── backend/                     # Python FastAPI
│   ├── main.py                 # API REST
│   ├── agents/                 # Agentes de IA
│   │   ├── code_review_agent.py
│   │   ├── writer_agent.py
│   │   └── fact_checker_agent.py
│   ├── llm/                    # Integração LLMs
│   ├── tools/                  # Ferramentas (busca web)
│   └── config/                 # Configurações
│
└── README.md
```

## 🚀 Quick Start

### Pré-requisitos

- [.NET 9 SDK](https://dotnet.microsoft.com/download)
- [Python 3.10+](https://python.org)
- API Keys:
  - [Groq](https://console.groq.com) (gratuito)
  - [Tavily](https://tavily.com) (gratuito)

### 1. Backend (Python)

```bash
cd backend

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou: venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis
cp .env.example .env
# Edite .env com suas API keys

# Rodar servidor
python main.py
```

O backend estará em: http://localhost:8000

### 2. Frontend (Blazor)

```bash
cd frontend

# Restaurar pacotes
dotnet restore

# Rodar em modo desenvolvimento
dotnet watch
```

O frontend estará em: http://localhost:5000 (ou porta indicada)

## 📚 API Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/health` | Health check |
| POST | `/api/code-review` | Revisão de código (JSON) |
| POST | `/api/code-review/upload` | Revisão via upload |
| POST | `/api/writer` | Escrita de matérias |
| POST | `/api/fact-check` | Checagem de fatos |

Documentação interativa: http://localhost:8000/docs

## 🔧 Configuração

### Variáveis de Ambiente (Backend)

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| `LLM_PROVIDER` | Provider: `groq` ou `openai` | `groq` |
| `GROQ_API_KEY` | API key do Groq | - |
| `TAVILY_API_KEY` | API key do Tavily | - |
| `PORT` | Porta do servidor | `8000` |
| `DEBUG` | Modo debug | `false` |

## 🛠️ Tecnologias

### Frontend
- Blazor WebAssembly (.NET 9)
- Bootstrap 5
- C#

### Backend
- FastAPI (Python)
- LangChain
- Groq (LLM gratuito)
- Tavily (busca web)

## 👥 Créditos

Projeto desenvolvido para o curso do **IMD/UFRN** em parceria com a **Akcit**.

- **Orientação**: Julia Dollis e Prof. Alyson Matheus
- **Repositório**: [github.com/felipe-sbm/akcit-agent-code-review](https://github.com/felipe-sbm/akcit-agent-code-review)

## 📝 Licença

Projeto acadêmico - uso educacional.
