# Embeddings

# Pré-requisitos
Antes de rodar o projeto, você precisa garantir que possui as seguintes ferramentas instaladas:

Python 3.13

Ollama (instalar o Ollama localmente)

Dependências do Python (como o langchain-community)

1. Instalar a IDE (Visual Studio Code)
VS Code é um editor de código leve, extensível, para desenvolvimento de software, você pode baixá-lo aqui (https://code.visualstudio.com)

2. Instalar o Ollama
O Ollama é um serviço de embeddings. Para usá-lo, instale o Ollama localmente seguindo as instruções disponíveis no site oficial.(https://ollama.com)

3. Instalar o modelo do Ollama
Tipo de modelo em que será feito o processo de embedding, você pode baixá-lo aqui (https://ollama.com/library/mxbai-embed-large)

4. Instalar as dependências do projeto
Certifique-se de que você tem o Python 3.13 ou superior instalado. Caso não tenha o Python instalado, você pode baixá-lo aqui.(https://www.python.org)

Depois, instale as dependências necessárias com o pip:

pip install langchain langchain-community

5. Rodar o modelo localmente
Inicie o modelo do Ollama utilizando o seguinte comando no terminal:

ollama serve

Esse comando irá conectar seu ambiente ao Ollama localmente.

6. Rodar o código no terminal

python embedds.py
