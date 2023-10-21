from sqlalchemy import Column, Integer, Text

from db_api.database import Base


class Table(Base):
    __tablename__ = "Table"

    id = Column(Integer, primary_key=True)
    first_column = Column(Text)
    second_column = Column(Text)