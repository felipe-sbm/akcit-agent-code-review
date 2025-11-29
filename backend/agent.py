"""
Agente de IA para Code Review usando Groq API.
"""
import os
from openai import OpenAI


class CodeReviewAgent:
    """Agente que analisa código e fornece feedback usando IA."""

    SYSTEM_PROMPT = """Você é um especialista em revisão de código com anos de experiência.
Sua função é analisar código enviado pelo usuário e fornecer feedback detalhado.

Ao analisar o código, você deve:
1. Identificar bugs, erros de lógica ou problemas potenciais
2. Sugerir melhorias de performance quando aplicável
3. Apontar más práticas e sugerir alternativas
4. Verificar se o código segue boas práticas da linguagem
5. Fornecer exemplos de código corrigido quando necessário

Formato da resposta:
- Use markdown para formatar sua resposta
- Seja claro e objetivo
- Forneça exemplos de código quando sugerir correções
- Organize por categorias: Bugs, Melhorias, Boas Práticas, etc.

Responda sempre em português brasileiro."""

    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY não configurada")

        # Groq usa API compatível com OpenAI
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.groq.com/openai/v1"
        )
        self.model = "llama-3.3-70b-versatile"  # Modelo rápido e capaz

    def review(self, code: str, task: str, filename: str) -> str:
        """
        Analisa o código e retorna feedback da IA.

        Args:
            code: Conteúdo do arquivo de código
            task: Descrição da tarefa/problema do usuário
            filename: Nome do arquivo para contexto

        Returns:
            Resposta da IA em markdown
        """
        # Detectar linguagem pela extensão
        extension = filename.rsplit(".", 1)[-1].lower() if "." in filename else "txt"
        language_map = {
            "py": "Python",
            "js": "JavaScript",
            "ts": "TypeScript",
            "cs": "C#",
            "java": "Java",
            "cpp": "C++",
            "c": "C",
            "razor": "Razor (C#/HTML)",
            "html": "HTML",
            "css": "CSS",
            "json": "JSON",
            "xml": "XML",
        }
        language = language_map.get(extension, extension.upper())

        user_message = f"""**Arquivo:** {filename}
**Linguagem:** {language}
**Tarefa solicitada:** {task}

**Código para análise:**
```{extension}
{code}
```

Por favor, analise o código acima conforme a tarefa solicitada."""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.SYSTEM_PROMPT},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.3,  # Mais determinístico para code review
                max_tokens=4096,
            )
            return response.choices[0].message.content

        except Exception as e:
            return f"❌ Erro ao processar com IA: {str(e)}"
