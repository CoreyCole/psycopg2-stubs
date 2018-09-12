# Stubs for psycopg2.tests.test_notify (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .testconfig import dsn
from .testutils import ConnectingTestCase, script_to_py3, slow, unittest
from typing import Any, Optional

class NotifiesTests(ConnectingTestCase):
    def autocommit(self, conn: Any) -> None: ...
    def listen(self, name: Any) -> None: ...
    def notify(self, name: Any, sec: int = ..., payload: Optional[Any] = ...): ...
    def test_notifies_received_on_poll(self) -> None: ...
    def test_many_notifies(self) -> None: ...
    def test_notifies_received_on_execute(self) -> None: ...
    def test_notify_object(self) -> None: ...
    def test_notify_attributes(self) -> None: ...
    def test_notify_payload(self): ...
    def test_notify_deque(self) -> None: ...
    def test_notify_noappend(self) -> None: ...
    def test_notify_init(self) -> None: ...
    def test_compare(self) -> None: ...
    def test_compare_tuple(self) -> None: ...
    def test_hash(self) -> None: ...

def test_suite(): ...