from pydantic import BaseModel, EmailStr

class CompanyCreate(BaseModel):
    name: str
    cnpj: str
    address: str
    email: EmailStr
    telephone: str

class ObligationCreate(BaseModel):
    name: str
    periodicity: str
    company_id: int

class CompanyResponse(CompanyCreate):
    id: int

    class Config:
        from_attributes = True

class ObligationResponse(ObligationCreate):
    id: int

    class Config:
        from_attributes = True
