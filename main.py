from fastapi import FastAPI, HTTPException, Depends
from typing import List
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import schemas
import models

app = FastAPI()

# Criar tabelas
models.Base.metadata.create_all(bind=engine)

# Dependência de sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/companies", response_model=schemas.CompanyResponse)
def create_companies(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    db_company = models.Companies(**company.model_dump())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

@app.get("/companies", response_model=List[schemas.CompanyResponse])
def get_companies(db: Session = Depends(get_db)):
    return db.query(models.Companies).all()

@app.get("/companies/{company_id}", response_model=schemas.CompanyResponse)
def get_company(company_id: int, db: Session = Depends(get_db)):
    company = db.query(models.Companies).filter(models.Companies.id == company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return company

@app.put("companies/{company_id}", response_model=schemas.CompanyResponse)
def update_company(company_id: int, company_update: schemas.CompanyCreate, db: Session = Depends(get_db)):
    company = db.query(models.Companies).filter(models.Companies.id == company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    for key, value in company_update.model_dump().items():
        setattr(company, key, value)
    db.commit()
    db.refresh(company)
    return company
    
@app.delete("companies/{company_id}", response_model=schemas.CompanyResponse)
def delete_company(company_id: int, db: Session = Depends(get_db)):
    company = db.query(models.Companies).filter(models.Companies.id == company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    
    db.delete(company)
    db.commit()
    return {"message": "Empresa deletada com sucesso"}

@app.post("/obligations", response_model=schemas.ObligationResponse)
def create_obligation(obligation: schemas.ObligationCreate, db: Session = Depends(get_db)):
    db_obligation = models.AccessoryObligation(**obligation.model_dump())
    db.add(db_obligation)
    db.commit()
    db.refresh(db_obligation)
    return db_obligation

@app.get("/obligations", response_model=List[schemas.ObligationResponse])
def get_obligations(db: Session = Depends(get_db)):
    return db.query(models.AccessoryObligation).all()

@app.get("/obligations/{obligation_id}", response_model=schemas.ObligationResponse)
def get_obligation(obligation_id: int, db: Session = Depends(get_db)):
    obligation = db.query(models.AccessoryObligation).filter(models.AccessoryObligation.id == obligation_id).first()
    if not obligation:
        raise HTTPException(status_code=404, detail="Obrigação acessória não encontrada")
    return obligation

@app.put("/obligations/{obligation_id}", response_model=schemas.ObligationResponse)
def update_obligation(obligation_id: int, obligation_update: schemas.ObligationCreate, db: Session = Depends(get_db)):
    obligation = db.query(models.AccessoryObligation).filter(models.AccessoryObligation.id == obligation_id).first()
    if not obligation:
        raise HTTPException(status_code=404, detail="Obrigação acessória não encontrada")
    for key, value in obligation_update.model_dump().items():
        setattr(obligation, key, value)
    db.commit()
    db.refresh(obligation)
    return obligation

@app.delete("/obligations/{obligation_id}")
def delete_obligation(obligation_id: int, db: Session = Depends(get_db)):
    obligation = db.query(models.AccessoryObligation).filter(models.AccessoryObligation.id == obligation_id).first()
    if not obligation:
        raise HTTPException(status_code=404, detail="Obrigação acessória não encontrada")
    db.delete(obligation)
    db.commit()
    return {"message": "Obrigação acessória deletada com sucesso"}