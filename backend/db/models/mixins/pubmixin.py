from datetime import datetime

from sqlalchemy.orm import Mapped

from .. import Config


Base = Config.BASE

class PUBMixin(Base):

    pub_date: Mapped[datetime]