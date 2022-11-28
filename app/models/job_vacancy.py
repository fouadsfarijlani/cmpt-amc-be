from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database.database import Base

class vacancy(Base):
    __tablename__ = "vacancy"

    id = Column(Integer, primary_key = True, index = True, nullable = False, autoincrement = True)
    title = Column(String, nullable=False)