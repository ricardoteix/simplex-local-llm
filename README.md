[<img src="https://em-content.zobj.net/thumbs/120/openmoji/338/flag-united-states_1f1fa-1f1f8.png" alt="us flag" width="48"/>](./README_en.md)

# Simplex Local LLM

Uma simples implementação de uma RAG (Retrieval-Augmented Generation) usando como base Python e Ollama.

Você poderá enviar PDFs e realizar prompts para obter respostas sobre o contexto dos arquivos enviados.

## Considerações de hardware

Este projeto foi desenvolvido em um **Alienware, Intel Core i9, 32GB de RAM, NVIDIA 4070 e HDs NVMe**.

Você pode até conseguir faze-lo funcionar com uma placa de vídeo onboard, como a Intel iRISxe, 
mas a experiência não deve ser boa nem gerar resultados aceitáveis, pois esses chips não são adequados
para LLM.

## Executando o projeto

### Ambiente

Use o arquivo ``.env.template`` como modelo para criar o ``.env`` do projeto.

Nele você pode alterar o valor da variável ``LLM_MODEL`` para um modelo compatível com Ollama. Veja a seguir.

### Ollama

Baixe e installe o Ollama aqui [https://ollama.com/download](https://ollama.com/download).

Em seguida, no terminal, baixe um dos modelos compatíveis com Ollama. Observe que baixar vários
deles pode complemeter o armazenamento em disco da sua máquina, pois são modelos grandes.

Alguns deles estão listados nos comandos abaixo. Nos meus testes usei ``qwen2.5:latest`` e ``deepseek-r1:8b``.

```bash
ollama pull mistral
ollama pull tinyllama 
ollama pull qwen2.5:latest  
ollama pull deepseek-r1:1.5b  
ollama pull deepseek-r1:7b  
ollama pull deepseek-r1:8b
```  

Em seguida

``ollama pull nomic-embed-text``

e execute o Ollama

``ollama serve``

### Install Python e dependências

Instale o Python 3 e, preferencialmente, crie um ambiente virtual.

``python -m venv env``

Ativando o ambiente no Linux

``source env/bin/activate``

Ativando o ambiente no Windows

``.\.venv\Scripts\activate``

Installe as dependências 

``pip install -r requirements.txt``

### Execute o projeto

``python app.py``

Acesse a interface com

``http://localhost:8080``

Na página inicial você poderá enviar os PDFs para treinamento ou acessar a página para executar os promps.

## Problemas na instalação do requirements.txt

Isso pode ocorrer por diversos fatores. No Windows foi usado o Python 12. Com a versão 13 houveram erros de
compilação das dependências. 

Se tiver o ``error: metadata-generation-failed`` o problema pode ser na compilação nas dependências do numpy.

### Possíveis soluções:

1. **Instalar um compilador C adequado**
   - O erro menciona que não encontrou compiladores como `cl`, `gcc`, `clang`, entre outros.
   - Se estiver no **Windows**, você pode instalar o **Microsoft C++ Build Tools**:
     - Baixe e instale [Microsoft Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
     - Durante a instalação, selecione **"Desktop development with C++"** e inclua o **Windows 10 SDK**.
   - Após instalar, reinicie o terminal e tente novamente.

2. **Instalar `numpy` a partir de um binário pré-compilado**
   - Tente instalar o `numpy` sem compilar do código-fonte:
     ```bash
     pip install --upgrade pip setuptools wheel
     pip install numpy==1.26.4 --prefer-binary
     ```
   - Isso baixa uma versão binária (wheel) compatível com seu sistema.

3. **Verificar se o `pip` está atualizado**
   - Às vezes, versões mais antigas do `pip` tentam compilar pacotes desnecessariamente.
   - Atualize o `pip` e as ferramentas de compilação:
     ```bash
     python -m pip install --upgrade pip setuptools wheel
     ```

4. **Usar Conda (se estiver disponível)**
   - Se estiver usando **Anaconda** ou **Miniconda**, experimente:
     ```bash
     conda install numpy=1.26.4
     ```

## Agradecimento

Baseado no tutorial de [Nasser Maronie](https://dev.to/nassermaronie/build-your-own-rag-app-a-step-by-step-guide-to-setup-llm-locally-using-ollama-python-and-chromadb-b12).
