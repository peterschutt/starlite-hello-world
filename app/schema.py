from piccolo.columns.column_types import ForeignKey, Integer, Varchar
from piccolo.table import Table


class Manager(Table):
    """Manager."""

    name = Varchar(length=100)


class Band(Table):
    """Band."""

    name = Varchar(length=100)
    manager = ForeignKey(references=Manager)
    popularity = Integer()
