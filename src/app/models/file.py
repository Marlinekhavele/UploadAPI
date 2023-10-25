from sqlalchemy import Column, Integer, String
from app.database.base import Base

class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    status = Column(String, default="Processing")