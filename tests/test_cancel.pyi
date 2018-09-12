# Stubs for psycopg2.tests.test_cancel (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .testconfig import dsn
from .testutils import ConnectingTestCase, skip_before_postgres, slow, unittest

class CancelTests(ConnectingTestCase):
    def setUp(self) -> None: ...
    def test_empty_cancel(self) -> None: ...
    def test_cancel(self) -> None: ...
    def test_async_cancel(self) -> None: ...
    def test_async_connection_cancel(self) -> None: ...

def test_suite(): ...
