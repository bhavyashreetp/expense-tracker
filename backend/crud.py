from sqlalchemy.orm import Session
from backend.models import Expense
from backend.schemas import ExpenseCreate

def create_expense(db: Session, expense: ExpenseCreate):
    existing = db.query(Expense).filter(
        Expense.request_id == expense.request_id
    ).first()

    if existing:
        return existing

    db_expense = Expense(
        amount=expense.amount,
        category=expense.category,
        description=expense.description,
        date=expense.date,
        request_id=expense.request_id
    )

    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def get_expenses(db: Session, category=None, sort=None):
    query = db.query(Expense)

    if category:
        query = query.filter(Expense.category == category)

    if sort == "date_desc":
        query = query.order_by(Expense.date.desc())

    return query.all()
