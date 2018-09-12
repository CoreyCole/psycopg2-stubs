# Stubs for psycopg2.tests.test_extras_dictcursor (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .testutils import ConnectingTestCase, skip_before_postgres, skip_before_python, skip_if_no_namedtuple, unittest
from typing import Any

class ExtrasDictCursorTests(ConnectingTestCase):
    def setUp(self) -> None: ...
    conn: Any = ...
    def testDictConnCursorArgs(self) -> None: ...
    def testDictCursorWithPlainCursorFetchOne(self): ...
    def testDictCursorWithPlainCursorFetchMany(self): ...
    def testDictCursorWithPlainCursorFetchManyNoarg(self): ...
    def testDictCursorWithPlainCursorFetchAll(self): ...
    def testDictCursorWithPlainCursorIter(self): ...
    def testUpdateRow(self): ...
    def testDictCursorWithPlainCursorIterRowNumber(self) -> None: ...
    def testDictCursorWithPlainCursorRealFetchOne(self): ...
    def testDictCursorWithPlainCursorRealFetchMany(self): ...
    def testDictCursorWithPlainCursorRealFetchManyNoarg(self): ...
    def testDictCursorWithPlainCursorRealFetchAll(self): ...
    def testDictCursorWithPlainCursorRealIter(self): ...
    def testDictCursorWithPlainCursorRealIterRowNumber(self) -> None: ...
    def testDictCursorWithNamedCursorFetchOne(self): ...
    def testDictCursorWithNamedCursorFetchMany(self): ...
    def testDictCursorWithNamedCursorFetchManyNoarg(self): ...
    def testDictCursorWithNamedCursorFetchAll(self): ...
    def testDictCursorWithNamedCursorIter(self): ...
    def testDictCursorWithNamedCursorNotGreedy(self) -> None: ...
    def testDictCursorWithNamedCursorIterRowNumber(self) -> None: ...
    def testDictCursorRealWithNamedCursorFetchOne(self): ...
    def testDictCursorRealWithNamedCursorFetchMany(self): ...
    def testDictCursorRealWithNamedCursorFetchManyNoarg(self): ...
    def testDictCursorRealWithNamedCursorFetchAll(self): ...
    def testDictCursorRealWithNamedCursorIter(self): ...
    def testDictCursorRealWithNamedCursorNotGreedy(self) -> None: ...
    def testDictCursorRealWithNamedCursorIterRowNumber(self) -> None: ...
    def testPickleDictRow(self) -> None: ...
    def testPickleRealDictRow(self) -> None: ...

class NamedTupleCursorTest(ConnectingTestCase):
    conn: Any = ...
    def setUp(self): ...
    def test_cursor_args(self) -> None: ...
    def test_fetchone(self) -> None: ...
    def test_fetchmany_noarg(self) -> None: ...
    def test_fetchmany(self) -> None: ...
    def test_fetchall(self) -> None: ...
    def test_executemany(self) -> None: ...
    def test_iter(self) -> None: ...
    def test_error_message(self): ...
    def test_record_updated(self) -> None: ...
    def test_no_result_no_surprise(self) -> None: ...
    def test_bad_col_names(self) -> None: ...
    def test_nonascii_name(self) -> None: ...
    def test_minimal_generation(self): ...
    def test_named(self) -> None: ...
    def test_named_fetchone(self) -> None: ...
    def test_named_fetchmany(self) -> None: ...
    def test_named_fetchall(self) -> None: ...
    def test_not_greedy(self) -> None: ...
    def test_named_rownumber(self) -> None: ...

def test_suite(): ...