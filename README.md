[<img src="https://em-content.zobj.net/thumbs/120/openmoji/338/flag-united-states_1f1fa-1f1f8.png" alt="us flag" width="48"/>](./README_en.md)

# Simplex Local LLM

Uma simples implementação de uma RAG (Retrieval-Augmented Generation) usando como base Python e Ollama.

Você poderá enviar PDFs e realizar prompts para obter respostas sobre o contexto dos arquivos enviados.

## Executando o projero

Instale o Python 3 e, preferencialmente, crie um ambiente virtual.

``python -m venv env``

Ativando o ambiente no Linux

``source env/bin/activate``

Ativando o ambiente no Windows

``.\.venv\Scripts\activate``

Installe as dependências 

``pip install -r requirements. txt``

Execute o projeto

``python app.py``

Acesse a interface com

``http://localhost:8080``

Na página inicial você poderá enviar os PDFs para treinamento ou acessar a página para executar os promps.

## Agradecimento

Baseado no tutorial de [Nasser Maronie](https://dev.to/nassermaronie/build-your-own-rag-app-a-step-by-step-guide-to-setup-llm-locally-using-ollama-python-and-chromadb-b12).

