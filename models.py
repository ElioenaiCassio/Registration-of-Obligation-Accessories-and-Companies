from sqlalchemy import Column, String, Integer, ForeignKey
from database import Base, engine

class Companies(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    cnpj = Column(String, unique=True, nullable=False)
    address = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telephone = Column(String, nullable=False)

    def __init__(self, name, cnpj, address, email, telephone):
        self.name = name
        self.cnpj = cnpj
        self.address = address
        self.email = email
        self.telephone = telephone

class AccessoryObligation(Base):
    __tablename__ = "obligations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    periodicity = Column(String, nullable=False)
    company_id = Column(Integer, ForeignKey("companies.id"))

    def __init__(self, name, periodicity, company_id):
        self.name = name
        self.periodicity = periodicity
        self.company_id = company_id

Base.metadata.create_all(bind=engine)
