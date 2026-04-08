from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

class UsuarioDB(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cargo = Column(String)
    departamento = Column(String)

class FeedbackDB(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    remetente_id = Column(Integer)
    destinatario_id = Column(Integer)
    mensagem = Column(String)
    competencia_detectada = Column(String)
    score_risco = Column(Float)
    data_envio = Column(DateTime, default=datetime.now)