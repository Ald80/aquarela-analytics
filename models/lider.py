from sqlalchemy import Column, Integer, String, ForeignKey, Float, create_engine
from sqlalchemy.orm import relationship, declarative_base
from database.session_db import Base


class Lider(Base):
    __tablename__="lider"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    matricula = Column(String(50), nullable=False, unique=True)

    colaboradores = relationship("Colaborador", back_populates="lider")