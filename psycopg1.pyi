# Stubs for psycopg2.psycopg1 (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from psycopg2 import *
from psycopg2.extensions import connection as _2connection, cursor as _2cursor
from typing import Any

_2connect = connect

def connect(*args: Any, **kwargs: Any): ...

class connection(_2connection):
    def cursor(self): ...
    def autocommit(self, on_off: int = ...) -> None: ...

class cursor(_2cursor):
    def dictfetchone(self): ...
    def dictfetchmany(self, size: Any): ...
    def dictfetchall(self): ...
