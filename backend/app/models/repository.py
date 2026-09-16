from datetime import datetime

from sqlalchemy import (
    BigInteger,
    DateTime,
    ForeignKey,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Repository(Base):
    __tablename__ = "repositories"

    __table_args__ = (
        UniqueConstraint(
            "github_repo_id",
            name="uq_repository_github_repo_id",
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    github_repo_id: Mapped[int] = mapped_column(
        BigInteger,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255)
    )

    full_name: Mapped[str] = mapped_column(
        String(500)
    )

    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        index=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    owner = relationship(
        "User",
        back_populates="repositories",
    )

    pull_requests = relationship(
        "PullRequest",
        back_populates="repository",
        cascade="all, delete-orphan",
    )