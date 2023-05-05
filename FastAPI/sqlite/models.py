from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base

class MateriaPrima(Base):
    __tablename__ = "materia_prima"
    codigo = Column(String, unique = True)
    descricao = Column(String, unique = True)
    preco_unitario = Column(Float)
    frete_sf = Column(Float)
    com_frete = Column(Float)
    custo_sf = Column(Float)
    porcentagem = Column(Float)
    dados_cigam = Column(String)
    especial = Column(String)
    estoque = Column(Float)
    unidade = Column(String)
    converte_kg = Column(Float)
    descri_converte = Column(String)
    formula = Column(String)
    data_alteracao = Column(String)
    data_compra = Column(String)
    id_grupo = Column(String)
    desc_grupo = Column(String)
    id_sub_grupo = Column(String)
    desc_sub_grupo = Column(String)



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
