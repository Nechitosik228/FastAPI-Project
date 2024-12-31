from sqlalchemy.orm import Mapped,mapped_column

from .. import Config


Base = Config.BASE

class PKMixin(Base):
    id: Mapped[int] = mapped_column(primary_key=True)