# Stubs for psycopg2._ipaddress (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

ipaddress: Any

def register_ipaddress(conn_or_curs: Optional[Any] = ...) -> None: ...
def cast_interface(s: Any, cur: Optional[Any] = ...): ...
def cast_network(s: Any, cur: Optional[Any] = ...): ...
def adapt_ipaddress(obj: Any): ...