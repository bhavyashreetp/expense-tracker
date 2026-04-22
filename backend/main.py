from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from backend.database import SessionLocal, engine, Base
from backend.crud import create_expense, get_expenses
from backend.schemas import ExpenseCreate, ExpenseResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/expenses", response_model=ExpenseResponse)
def add_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    return create_expense(db, expense)

@app.get("/expenses", response_model=list[ExpenseResponse])
def list_expenses(category: str = None, sort: str = None, db: Session = Depends(get_db)):
    return get_expenses(db, category, sort)
