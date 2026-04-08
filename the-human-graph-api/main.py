from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from pydantic import BaseModel

# Importando nossos arquivos locais de banco de dados
import models
from database import engine, get_db

# --- NOVO: Importando a conexão do Banco de Grafos (Neo4j) ---
from graph_db import graph_conn

# Essa linha cria o arquivo human_graph.db e as tabelas automaticamente
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="The Human Graph API",
    description="Motor de Inteligência Organizacional e Gestão de Risco",
    version="1.0.0"
)

# --- 1. SCHEMAS (Pydantic) ---

class UsuarioBase(BaseModel):
    nome: str
    cargo: str
    departamento: str

class Usuario(UsuarioBase):
    id: int
    class Config:
        from_attributes = True

class FeedbackBase(BaseModel):
    remetente_id: int
    destinatario_id: int
    mensagem: str

class Feedback(FeedbackBase):
    id: int
    competencia_detectada: str
    score_risco: float
    data_envio: datetime
    class Config:
        from_attributes = True

# --- 2. MOTOR DE INTELIGÊNCIA (Mock NLP) ---

def analise_ia_mock(mensagem: str):
    mensagem_lower = mensagem.lower()
    palavras_risco = ["cansado", "sobrecarga", "estresse", "atraso", "pressão", "desmotivado", "microgerenciamento"]
    
    competencias = {
        "Liderança": ["guiou", "liderou", "mentoria", "ajudou a equipe", "direção"],
        "Clean Code": ["código limpo", "refatoração", "arquitetura", "bugs", "otimizou"],
        "Resiliência": ["aguentou", "pressão", "prazo apertado", "crise"],
        "Empatia": ["ouviu", "compreendeu", "apoiou", "clima"]
    }

    score_risco = sum(0.25 for palavra in palavras_risco if palavra in mensagem_lower)
    score_risco = min(score_risco, 1.0)

    competencia_detectada = "Geral"
    for comp, palavras_chave in competencias.items():
        if any(palavra in mensagem_lower for palavra in palavras_chave):
            competencia_detectada = comp
            break

    return competencia_detectada, score_risco

# --- 3. ROTAS DA API ---

@app.get("/")
def home():
    return {"status": "The Human Graph API rodando com Banco de Dados Duplo! 🚀"}

@app.post("/usuarios", response_model=Usuario)
def criar_usuario(usuario: UsuarioBase, db: Session = Depends(get_db)):
    db_usuario = models.UsuarioDB(**usuario.model_dump())
    db.add(db_usuario) 
    db.commit()        
    db.refresh(db_usuario) 

    # --- NOVO: Salvando no Grafo (Neo4j) ---
    graph_conn.criar_usuario_no_grafo(
        usuario_id=db_usuario.id, 
        nome=db_usuario.nome, 
        departamento=db_usuario.departamento
    )

    return db_usuario

@app.get("/usuarios", response_model=List[Usuario])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(models.UsuarioDB).all()

@app.post("/feedbacks", response_model=Feedback)
def enviar_feedback(feedback_in: FeedbackBase, db: Session = Depends(get_db)):
    
    competencia, risco = analise_ia_mock(feedback_in.mensagem)
    
    db_feedback = models.FeedbackDB(
        remetente_id=feedback_in.remetente_id,
        destinatario_id=feedback_in.destinatario_id,
        mensagem=feedback_in.mensagem,
        competencia_detectada=competencia,
        score_risco=risco
    )
    
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    
    # --- NOVO: Criando a conexão no Grafo (Neo4j) ---
    graph_conn.criar_feedback_no_grafo(
        remetente_id=db_feedback.remetente_id,
        destinatario_id=db_feedback.destinatario_id,
        competencia=db_feedback.competencia_detectada,
        score_risco=db_feedback.score_risco
    )
    
    return db_feedback