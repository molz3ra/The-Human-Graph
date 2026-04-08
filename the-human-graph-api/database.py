from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Cria um arquivo local chamado "human_graph.db" para guardar os dados
SQLALCHEMY_DATABASE_URL = "sqlite:///./human_graph.db"

# O 'check_same_thread' é necessário apenas para o SQLite trabalhar bem com o FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Função para abrir e fechar a conexão com o banco a cada requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()