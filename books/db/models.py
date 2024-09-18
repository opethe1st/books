from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy import String
from sqlalchemy import create_engine


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))


def setup_db():
    engine = create_engine("sqlite://", echo=True)
    Base.metadata.create_all(engine)
