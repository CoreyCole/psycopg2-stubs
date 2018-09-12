# Stubs for psycopg2.tests.test_types_basic (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .testutils import ConnectingTestCase, decorate_all_tests, unittest
from typing import Any

class TypesBasicTests(ConnectingTestCase):
    def execute(self, *args: Any): ...
    def testQuoting(self) -> None: ...
    def testUnicode(self) -> None: ...
    def testNumber(self) -> None: ...
    def testBoolean(self) -> None: ...
    def testDecimal(self) -> None: ...
    def testFloatNan(self): ...
    def testFloatInf(self): ...
    def testBinary(self) -> None: ...
    def testBinaryNone(self) -> None: ...
    def testBinaryEmptyString(self) -> None: ...
    def testBinaryRoundTrip(self) -> None: ...
    def testArray(self) -> None: ...
    def testEmptyArrayRegression(self) -> None: ...
    def testEmptyArrayNoCast(self) -> None: ...
    def testEmptyArray(self) -> None: ...
    def testArrayEscape(self) -> None: ...
    def testArrayMalformed(self) -> None: ...
    def testArrayOfNulls(self) -> None: ...
    def testNestedArrays(self) -> None: ...
    def testTypeRoundtripBuffer(self) -> None: ...
    def testTypeRoundtripBufferArray(self) -> None: ...
    def testTypeRoundtripBytes(self) -> None: ...
    def testTypeRoundtripBytesArray(self) -> None: ...
    def testAdaptBytearray(self) -> None: ...
    def testAdaptMemoryview(self) -> None: ...
    def testByteaHexCheckFalsePositive(self) -> None: ...
    def testNegNumber(self) -> None: ...
    def testGenericArray(self) -> None: ...
    def testGenericArrayNull(self): ...
    def testNetworkArray(self) -> None: ...

class AdaptSubclassTest(unittest.TestCase):
    def test_adapt_subtype(self) -> None: ...
    def test_adapt_most_specific(self): ...
    def test_no_mro_no_joy(self): ...
    def test_adapt_subtype_3(self): ...
    def test_conform_subclass_precedence(self): ...

class ByteaParserTest(unittest.TestCase):
    def setUp(self) -> None: ...
    def cast(self, buffer: Any): ...
    def test_null(self) -> None: ...
    def test_blank(self) -> None: ...
    def test_blank_hex(self) -> None: ...
    def test_full_hex(self, upper: bool = ...) -> None: ...
    def test_full_hex_upper(self): ...
    def test_full_escaped_octal(self) -> None: ...
    def test_escaped_mixed(self) -> None: ...

def skip_if_cant_cast(f: Any): ...
def test_suite(): ...