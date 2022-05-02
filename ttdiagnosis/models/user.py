from sqlalchemy import Column, Date, Integer, String

from ttdiagnosis.database.engine import Base, engine


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    session_date = Column(Date)


Base.metadata.create_all(engine)
