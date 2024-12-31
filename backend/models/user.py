from typing import List

from .config import Config
from .mixins import PUBMixin, PKMixin

from sqlalchemy.orm import Mapped, relationship


Base = Config.BASE


class User(PKMixin, Base, PUBMixin):
    __tablename__ = "users"

    name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]

    posts: Mapped[List["Post"]] = relationship(back_populates="users")

    comments: Mapped[List["Comment"]] = relationship(back_populates="users")
