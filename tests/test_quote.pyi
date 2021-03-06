# Stubs for psycopg2.tests.test_quote (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .testutils import ConnectingTestCase, unittest

class QuotingTestCase(ConnectingTestCase):
    def test_string(self) -> None: ...
    def test_string_null_terminator(self) -> None: ...
    def test_binary(self): ...
    def test_unicode(self): ...
    def test_latin1(self) -> None: ...
    def test_koi8(self) -> None: ...

class TestQuotedString(ConnectingTestCase):
    def test_encoding_from_conn(self) -> None: ...

class TestQuotedIdentifier(ConnectingTestCase):
    def test_identifier(self) -> None: ...
    def test_unicode_ident(self) -> None: ...

class TestStringAdapter(ConnectingTestCase):
    def test_encoding_default(self) -> None: ...
    def test_encoding_error(self) -> None: ...
    def test_set_encoding(self) -> None: ...
    def test_connection_wins_anyway(self) -> None: ...
    def test_adapt_bytes(self) -> None: ...

def test_suite(): ...
