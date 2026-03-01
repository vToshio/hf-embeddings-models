# Testes de Embeddings

Instalando as dependências para a execução dos testes

```bash
$ pip install uv
```

Para realizar os testes, primeiro é necessário realizar a adição de um arquivo .env, com a chave obrigatória "HF_MODEL"
Como base, utilize o modelo "all-MiniLM-L6-v2"

Após isso, basta executar o comando abaixo:

```bash
$ uv run main.py
```