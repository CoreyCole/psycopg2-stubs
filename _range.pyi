# Stubs for psycopg2._range (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class Range:
    def __init__(self, lower: Optional[Any] = ..., upper: Optional[Any] = ..., bounds: str = ..., empty: bool = ...) -> None: ...
    @property
    def lower(self): ...
    @property
    def upper(self): ...
    @property
    def isempty(self): ...
    @property
    def lower_inf(self): ...
    @property
    def upper_inf(self): ...
    @property
    def lower_inc(self): ...
    @property
    def upper_inc(self): ...
    def __contains__(self, x: Any): ...
    def __bool__(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def __hash__(self): ...
    def __lt__(self, other: Any): ...
    def __le__(self, other: Any): ...
    def __gt__(self, other: Any): ...
    def __ge__(self, other: Any): ...

def register_range(pgrange: Any, pyrange: Any, conn_or_curs: Any, globally: bool = ...): ...

class RangeAdapter:
    name: Any = ...
    adapted: Any = ...
    def __init__(self, adapted: Any) -> None: ...
    def __conform__(self, proto: Any): ...
    def prepare(self, conn: Any) -> None: ...
    def getquoted(self): ...

class RangeCaster:
    subtype_oid: Any = ...
    typecaster: Any = ...
    array_typecaster: Any = ...
    def __init__(self, pgrange: Any, pyrange: Any, oid: Any, subtype_oid: Any, array_oid: Optional[Any] = ...) -> None: ...
    def parse(self, s: Any, cur: Optional[Any] = ...): ...

class NumericRange(Range): ...
class DateRange(Range): ...
class DateTimeRange(Range): ...
class DateTimeTZRange(Range): ...

class NumberRangeAdapter(RangeAdapter):
    def getquoted(self): ...

int4range_caster: Any
int8range_caster: Any
numrange_caster: Any
daterange_caster: Any
tsrange_caster: Any
tstzrange_caster: Any
