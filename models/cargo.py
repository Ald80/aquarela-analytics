from sqlalchemy import Column, Integer, String, ForeignKey, Float, create_engine
from sqlalchemy.orm import relationship, declarative_base
from database.session_db import Base

class Cargo(Base):
    __tablename__="cargo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    cd_codigo = Column(String(50), nullable=False, unique=True)
    salario = Column(Float, nullable=False)

    colaboradores = relationship("Colaborador", back_populates="cargo")