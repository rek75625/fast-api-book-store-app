from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace with your actual database URI (e.g., "sqlite:///./test.db")
DATABASE_URL = "sqlite:///./test.db" 
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class DBItems(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)       # Changed to String for item names
    quantity = Column(Integer, default=0)   # Changed to Integer for item stock count
    image_src = Column(String, nullable=True) # String path/URL to the image

# Automatically generates the database table if it doesn't exist
DBItems.metadata.create_all(bind=engine)
