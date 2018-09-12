# Stubs for psycopg2.tests.test_psycopg2_dbapi20 (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from . import dbapi20, dbapi20_tpc
from .testconfig import dsn
from .testutils import decorate_all_tests, skip_if_tpc_disabled, unittest
from typing import Any

class Psycopg2Tests(dbapi20.DatabaseAPI20Test):
    driver: Any = ...
    connect_args: Any = ...
    connect_kw_args: Any = ...
    lower_func: str = ...
    def test_callproc(self) -> None: ...
    def test_setoutputsize(self) -> None: ...
    def test_nextset(self) -> None: ...

class Psycopg2TPCTests(dbapi20_tpc.TwoPhaseCommitTests, unittest.TestCase):
    driver: Any = ...
    def connect(self): ...

def test_suite(): ...
