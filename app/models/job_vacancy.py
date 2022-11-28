from sqlalchemy import Integer, Column, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship
from app.database.database import Base

class Vacancy(Base):
    __tablename__ = "vacancy"

    id = Column(Integer, primary_key = True, index = True, nullable = False, autoincrement = True)
    title = Column(String, nullable=False)
    active = Column(Boolean)
    vacancy_category_id = Column(ForeignKey("vacancy_category.id"))
    vacancy_hours_id = Column(ForeignKey("vacancy_hours.id"))

    vacancy_category = relationship("VacancyCategory", back_populates = "vacancy")
    vacancy_hours = relationship("VacancyHours", back_populates="vacancy")

class VacancyHours(Base):
    __tablename__ = "vacancy_hours"

    id = Column(Integer, primary_key = True, index = True, nullable = False, autoincrement = True)
    category = Column(String, nullable = False)

    vacancy = relationship("Vacancy", back_populates="vacancy_hours", uselist=False)

class VacancyCategory(Base):
    __tablename__ = "vacancy_category"

    id = Column(Integer, primary_key = True, index = True, nullable = False, autoincrement = True)
    type = Column(String, nullable = False)
    description = Column(String)

    relationship("Vacancy", back_populates = "vacancy_hours", uselist = False)

class VacancyDescription(Base):
    __tablename__ = "vacancy_description"

    id = Column(Integer, primary_key = True, index = True, nullable = False, autoincrement = True)
    description = Column(String)

class VacancyDescriptionTag(Base):
    __tablename__ = "vacancy_description_tag"

    id = Column(Integer, primary_key = True, index = True, nullable = False, autoincrement = True)
    type = Column(String, nullable = False)
    