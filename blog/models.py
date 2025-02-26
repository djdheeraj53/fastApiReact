from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from database import Base

class Blog(Base):
    __tablename__ = "blogs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)  # ✅ Correct
    title: Mapped[str] = mapped_column(String, nullable=False)  # ✅ Correct
    body: Mapped[str] = mapped_column(String, nullable=False)  # ✅ Correct