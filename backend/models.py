from sqlalchemy import Column, Integer, String, Date, DateTime, Numeric, engine
from datetime import datetime
from .database import Base
from .models import Expense
Base.metadata.create_all(bind=engine)

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Numeric(10, 2), nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, nullable=True)
    date = Column(Date, nullable=False)
    created_at = Column(DateTime, default=datetime)
    request_id = Column(String, unique=True, nullable=False)


