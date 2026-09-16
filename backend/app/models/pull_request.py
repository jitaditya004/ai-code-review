from datetime import datetime

from sqlalchemy import (
    BigInteger,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class PullRequest(Base):
    __tablename__ = "pull_requests"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    github_pr_id: Mapped[int] = mapped_column(
        BigInteger,
        index=True,
    )

    number: Mapped[int] = mapped_column(
        Integer
    )

    title: Mapped[str] = mapped_column(
        String(500)
    )

    head_sha: Mapped[str] = mapped_column(
        String(64)
    )

    repository_id: Mapped[int] = mapped_column(
        ForeignKey("repositories.id"),
        index=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    repository = relationship(
        "Repository",
        back_populates="pull_requests",
    )

    reviews = relationship(
        "Review",
        back_populates="pull_request",
        cascade="all, delete-orphan",
    )