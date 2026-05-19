# connection.py: Ler a URL do banco no .env e criar um objeto de conexão reutilizável para a API.

import os # Ferramenta nativa do Python pra mexer com o sistema operacional
from dotenv import load_dotenv # Ler o que tem no .env
from sqlalchemy import create_engine # Conecta Python ao banco de dados

load_dotenv() # Ativa a leitura do .env

DATABASE_URL = os.getenv("DATABASE_URL") # pega o endereço do banco de dados que ta no .env

if DATABASE_URL is None: # Se a variável não existir...
    raise RuntimeError("DATABASE_URL não encontrada no .env") # Interrompe o programa com um erro

engine = create_engine(DATABASE_URL) # O objeto central que sabe como conversar com o banco está disponível
