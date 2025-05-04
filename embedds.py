
#Conectando-se localmente ao Ollama
from langchain_community.embeddings import OllamaEmbeddings

#Conectando-se ao modelo escolhido do Ollama
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

#Criando o arquivo de texto em que será realizado o processo de embedding
documents = ["testando a geração de embeddings com o Ollama"]

#Transformando o texto em embedds
document_embeddings = embeddings.embed_documents(documents)

#Exibindo o tamanho do embedding do vetor
embedding_size = len(document_embeddings[0])
print(f"Tamanho dos embeddings: {embedding_size}")

#Exibindo os 10 primeiros valores do vetor de embedding
print("Primeiros 10 valores do vetor de embeddings:")
for i, value in enumerate(document_embeddings[0][:10]):
    print(f"Valor {i+1}: {value}")
