import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
# DATABASE_URL = "mysql+mysqlconnector://root:1234@localhost/test"
load_dotenv()
DB_USER = str(os.getenv("DB_USER", default='postgres'))
DB_PASSWORD = str(os.getenv("DB_PASSWORD", default='1234'))
DB_HOST = str(os.getenv("DB_HOST", default='localhost'))
DB_SCHEMA = str(os.getenv("DB_SCHEMA", default='postgres'))
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_SCHEMA}"
# DATABASE_URL = "postgresql://postgres:password@postgres:5432/dbname"
print(13, DATABASE_URL)
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
# Create all database tables (if they don't exist)
Base.metadata.create_all(engine)


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
