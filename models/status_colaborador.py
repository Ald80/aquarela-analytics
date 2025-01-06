from sqlalchemy import Column, Integer, String, ForeignKey, Float, create_engine
from sqlalchemy.orm import relationship, declarative_base
from database.session_db import Base


class StatusColaborador(Base):
    __tablename__="status_colaborador"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    cd_status = Column(String(50), nullable=False, unique=True)

    colaboradores = relationship("Colaborador", back_populates="status")