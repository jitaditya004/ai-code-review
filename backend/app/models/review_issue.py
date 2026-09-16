from enum import Enum

from sqlalchemy import (
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Severity(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class IssueCategory(str, Enum):
    SECURITY = "security"
    BUG = "bug"
    PERFORMANCE = "performance"
    STYLE = "style"
    MAINTAINABILITY = "maintainability"


class ReviewIssue(Base):
    __tablename__ = "review_issues"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    review_id: Mapped[int] = mapped_column(
        ForeignKey("reviews.id"),
        index=True,
    )

    file_path: Mapped[str] = mapped_column(
        String(1000)
    )

    line_start: Mapped[int] = mapped_column(
        Integer
    )

    line_end: Mapped[int] = mapped_column(
        Integer
    )

    category: Mapped[IssueCategory] = mapped_column()

    severity: Mapped[Severity] = mapped_column()

    confidence: Mapped[float] = mapped_column(
        Float
    )

    explanation: Mapped[str] = mapped_column(
        Text
    )

    suggested_fix: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    review = relationship(
        "Review",
        back_populates="issues",
    )