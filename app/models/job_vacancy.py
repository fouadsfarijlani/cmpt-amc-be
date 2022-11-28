from sqlalchemy import Integer, Column, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship
from app.database.database import Base

class Vacancy(Base):
    __tablename__ = "vacancy"

    id = Column(Integer, primary_key = True, index = True, nullable = False, autoincrement = True)
    title = Column(String, nullable=False)
    active = Column(Boolean)
    hours_category_id = Column(ForeignKey("vacancy_hours.id"))

    vacancy_hours = relationship("VacancyHours", back_populates="vacancy")

class VacancyHours(Base):
    __tablename__ = "vacancy_hours"

    id = Column(Integer, primary_key = True, index = True, nullable = False, autoincrement = True)
    hours_category = Column(String, nullable = False)

    vacancy = relationship("Vacancy", back_populates="vacancy_hours", uselist=False)