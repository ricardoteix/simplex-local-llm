[<img src="https://em-content.zobj.net/thumbs/160/openmoji/338/flag-brazil_1f1e7-1f1f7.png" alt="us flag" width="48"/>](./README.md)

# Simplex Local LLM

A simple implementation of a Retrieval-Augmented Generation (RAG) using Python and Ollama.

You can upload PDFs and make prompts to get answers based on the context of the uploaded files.

## Hardware Considerations

This project was developed on an **Alienware, Intel Core i9, 32GB RAM, NVIDIA 4070, and NVMe SSDs**.

You might be able to make it work with an onboard graphics card, such as the Intel Iris Xe, 
but the experience is likely to be poor and not produce acceptable results, as these chips are not suited 
for LLM tasks.

## Running the Project

### Environment

Use the ``.env.template`` file as a template to create your project's ``.env``.

In it, you can change the value of the ``LLM_MODEL`` variable to a model compatible with Ollama. See below.

### Ollama

Download and install Ollama here [https://ollama.com/download](https://ollama.com/download).

Then, in the terminal, download one of the models compatible with Ollama. Note that downloading several
of them can fill up your machine's storage, as these are large models.

Some of them are listed in the commands below. In my tests, I used ``qwen2.5:latest`` and ``deepseek-r1:8b``.

```bash
ollama pull mistral
ollama pull tinyllama 
ollama pull qwen2.5:latest  
ollama pull deepseek-r1:1.5b  
ollama pull deepseek-r1:7b  
ollama pull deepseek-r1:8b
```  

Then,  

``ollama pull nomic-embed-text``  

And run Ollama  

``ollama serve``  

### Install Python and Dependencies

Install Python 3 and, preferably, create a virtual environment.

``python -m venv env``

Activating the environment on Linux

``source env/bin/activate``

Activating the environment on Windows

``.\.venv\Scripts\activate``

Install the dependencies

``pip install -r requirements.txt``

### Run the Project

``python app.py``

Access the interface at

``http://localhost:8080``

On the homepage, you can upload PDFs for training or access the page to execute prompts.

## Issues with Installing requirements.txt

This can happen for various reasons. On Windows, Python 12 was used. With version 13, there were compilation errors with the dependencies.

If you encounter ``error: metadata-generation-failed``, the issue may be related to the compilation of the numpy dependencies.

### Possible Solutions:

1. **Install an appropriate C compiler**
   - The error indicates that it couldn't find compilers like `cl`, `gcc`, `clang`, among others.
   - If you are on **Windows**, you can install the **Microsoft C++ Build Tools**:
     - Download and install [Microsoft Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
     - During installation, select **"Desktop development with C++"** and include the **Windows 10 SDK**.
   - After installation, restart your terminal and try again.

2. **Install `numpy` from a precompiled binary**
   - Try installing `numpy` without compiling from source:
     ```bash
     pip install --upgrade pip setuptools wheel
     pip install numpy==1.26.4 --prefer-binary
     ```
   - This will download a binary (wheel) version compatible with your system.

3. **Check if `pip` is up to date**
   - Sometimes older versions of `pip` try to compile packages unnecessarily.
   - Update `pip` and the build tools:
     ```bash
     python -m pip install --upgrade pip setuptools wheel
     ```

4. **Use Conda (if available)**
   - If you are using **Anaconda** or **Miniconda**, try:
     ```bash
     conda install numpy=1.26.4
     ```
## Acknowledgment

Based on the tutorial by [Nasser Maronie](https://dev.to/nassermaronie/build-your-own-rag-app-a-step-by-step-guide-to-setup-llm-locally-using-ollama-python-and-chromadb-b12).



