
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.core.database import Base

from sqlalchemy.orm import relationship

class AIRequest(Base):
    __tablename__ = "ai_requests"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    domain = Column(String(50), nullable=False)

    input_text = Column(Text, nullable=False)

    status = Column(
        String(30),
        nullable=False,
        default="pending",
        server_default="pending"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    user = relationship(
    "User",
    back_populates="ai_requests"
    )
