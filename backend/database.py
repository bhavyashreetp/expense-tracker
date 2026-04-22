import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("postgresql://expense_tracker_sshe_user:1Y2gYbHHbLRpSY5o4KuMO7ZZjTxLn9MG@dpg-d7k9t81j2pic739flabg-a/expense_tracker_sshe")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()