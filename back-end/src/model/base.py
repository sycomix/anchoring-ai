"""Base."""
from connection import db


# pylint: disable=too-few-public-methods
class DbBase(db.Model):
    """DB base."""
    __abstract__ = True

    def as_dict(self):
        """Dict format."""
        return {
            c.name: getattr(self, c.name)
            if str(c.type) == 'JSON'
            else str(getattr(self, c.name))
            for c in self.__table__.columns
            if getattr(self, c.name) is not None
        }
