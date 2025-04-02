[<img src="https://em-content.zobj.net/thumbs/160/openmoji/338/flag-brazil_1f1e7-1f1f7.png" alt="us flag" width="48"/>](./README.md)

# Simplex Local LLM

A simple implementation of a Retrieval-Augmented Generation (RAG) using Python and Ollama as a base.

You can upload PDFs and use prompts to get answers about the context of the uploaded files.

## Running the project

Install Python 3 and, preferably, create a virtual environment.

``python -m venv env``

Activating the environment on Linux

``source env/bin/activate``

Activating the environment on Windows

``.\.venv\Scripts\activate``

Install the dependencies

``pip install -r requirements.txt``

Run the project

``python app.py``

Access the interface with

``http://localhost:8080``

On the home page, you can upload PDFs for training or access the page to execute the prompts.

## Acknowledgment
Based on the tutorial by [Nasser Maronie](https://dev.to/nassermaronie/build-your-own-rag-app-a-step-by-step-guide-to-setup-llm-locally-using-ollama-python-and-chromadb-b12).