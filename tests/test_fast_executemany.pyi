# Stubs for psycopg2.tests.test_fast_executemany (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from . import testutils
from .testutils import unittest

class TestPaginate(unittest.TestCase):
    def test_paginate(self): ...

class FastExecuteTestMixin:
    def setUp(self) -> None: ...

class TestExecuteBatch(FastExecuteTestMixin, testutils.ConnectingTestCase):
    def test_empty(self) -> None: ...
    def test_one(self) -> None: ...
    def test_tuples(self) -> None: ...
    def test_many(self) -> None: ...
    def test_pages(self) -> None: ...
    def test_unicode(self) -> None: ...

class TestExecuteValues(FastExecuteTestMixin, testutils.ConnectingTestCase):
    def test_empty(self) -> None: ...
    def test_one(self) -> None: ...
    def test_tuples(self) -> None: ...
    def test_dicts(self) -> None: ...
    def test_many(self) -> None: ...
    def test_pages(self) -> None: ...
    def test_unicode(self) -> None: ...
    def test_invalid_sql(self) -> None: ...
    def test_percent_escape(self) -> None: ...

def test_suite(): ...