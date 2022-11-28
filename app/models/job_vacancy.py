from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database.database import Base

class Vacancy(Base):
    __tablename__ = "vacancy"

    id = Column(Integer, primary_key = True, index = True, nullable = False, autoincrement = True)
    title = Column(String, nullable=False)

class VacancyHours(Base):
    __tablename__ = "vacancy_hours"

    id = Column(Integer, primary_key = True, index = True, nullable = False, autoincrement = True)
    hours_category = Column(String, nullable = False)