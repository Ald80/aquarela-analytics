from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.session_db import Base


class Colaborador(Base):
    __tablename__ = "colaborador"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    sobrenome = Column(String(255), nullable=False)
    matricula = Column(String(50), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)

    id_cargo = Column(Integer, ForeignKey("cargo.id"), nullable=False)
    id_status = Column(Integer, ForeignKey("status_colaborador.id"), nullable=False)
    id_lider = Column(Integer, ForeignKey("lider.id"), nullable=False)

    cargo = relationship("Cargo", back_populates="colaboradores")
    status = relationship("StatusColaborador", back_populates="colaboradores")
    lider = relationship("Lider", back_populates="colaboradores")
