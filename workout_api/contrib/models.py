from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID


class BaseModel(DeclarativeBase):
     id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=UUID4, nullable=False)
 