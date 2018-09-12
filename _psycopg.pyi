# Stubs for psycopg2._psycopg (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

BINARY: Any
BINARYARRAY: Any
BOOLEAN: Any
BOOLEANARRAY: Any
CIDRARRAY: Any
DATE: Any
DATEARRAY: Any
DATETIME: Any
DATETIMEARRAY: Any
DATETIMETZ: Any
DATETIMETZARRAY: Any
DECIMAL: Any
DECIMALARRAY: Any
FLOAT: Any
FLOATARRAY: Any
INETARRAY: Any
INTEGER: Any
INTEGERARRAY: Any
INTERVAL: Any
INTERVALARRAY: Any
LONGINTEGER: Any
LONGINTEGERARRAY: Any
MACADDRARRAY: Any
NUMBER: Any
PYDATE: Any
PYDATEARRAY: Any
PYDATETIME: Any
PYDATETIMEARRAY: Any
PYDATETIMETZ: Any
PYDATETIMETZARRAY: Any
PYINTERVAL: Any
PYINTERVALARRAY: Any
PYTIME: Any
PYTIMEARRAY: Any
REPLICATION_LOGICAL: int
REPLICATION_PHYSICAL: int
ROWID: Any
ROWIDARRAY: Any
STRING: Any
STRINGARRAY: Any
TIME: Any
TIMEARRAY: Any
UNICODE: Any
UNICODEARRAY: Any
UNKNOWN: Any
adapters: Any
apilevel: str
binary_types: Any
encodings: Any
paramstyle: str
string_types: Any
threadsafety: int

def Date(year, month, day): ...
def DateFromPy(*args, **kwargs): ...
def DateFromTicks(ticks): ...
def IntervalFromPy(*args, **kwargs): ...
def Time(hour, minutes, seconds, tzinfo=None): ...
def TimeFromPy(*args, **kwargs): ...
def TimeFromTicks(ticks): ...
def Timestamp(year, month, day, hour, minutes, seconds, tzinfo=None): ...
def TimestampFromPy(*args, **kwargs): ...
def TimestampFromTicks(ticks): ...
def _connect(*args, **kwargs): ...
def adapt(obj, protocol, alternate): ...
def get_wait_callback(*args, **kwargs): ...
def libpq_version(*args, **kwargs): ...
def new_array_type(oids, name, baseobj): ...
def new_type(oids, name, castobj): ...
def parse_dsn(dsn): ...
def quote_ident(str, conn_or_curs): ...
def register_type(obj, conn_or_curs): ...
def set_wait_callback(*args, **kwargs): ...

class AsIs:
    adapted: Any = ...
    def __init__(self, *args, **kwargs): ...
    def getquoted(self): ...
    def __conform__(self, *args, **kwargs): ...

class Binary:
    adapted: Any = ...
    buffer: Any = ...
    def __init__(self, *args, **kwargs): ...
    def getquoted(self): ...
    def prepare(self, conn): ...
    def __conform__(self, *args, **kwargs): ...

class Boolean:
    adapted: Any = ...
    def __init__(self, *args, **kwargs): ...
    def getquoted(self): ...
    def __conform__(self, *args, **kwargs): ...

class Column(tuple):
    __new__: Any = ...
    _asdict: Any = ...
    _fields: Any = ...
    _fields_defaults: Any = ...
    _make: Any = ...
    _replace: Any = ...
    display_size: Any = ...
    internal_size: Any = ...
    name: Any = ...
    null_ok: Any = ...
    precision: Any = ...
    scale: Any = ...
    type_code: Any = ...
    __getnewargs__: Any = ...
    __slots__: Any = ...

class DataError(DatabaseError): ...

class DatabaseError(Error): ...

class Decimal:
    adapted: Any = ...
    def __init__(self, *args, **kwargs): ...
    def getquoted(self): ...
    def __conform__(self, *args, **kwargs): ...

class Diagnostics:
    column_name: Any = ...
    constraint_name: Any = ...
    context: Any = ...
    datatype_name: Any = ...
    internal_position: Any = ...
    internal_query: Any = ...
    message_detail: Any = ...
    message_hint: Any = ...
    message_primary: Any = ...
    schema_name: Any = ...
    severity: Any = ...
    source_file: Any = ...
    source_function: Any = ...
    source_line: Any = ...
    sqlstate: Any = ...
    statement_position: Any = ...
    table_name: Any = ...
    def __init__(self, *args, **kwargs): ...

class Error(Exception):
    cursor: Any = ...
    diag: Any = ...
    pgcode: Any = ...
    pgerror: Any = ...
    def __init__(self, *args, **kwargs): ...
    def __reduce__(self): ...
    def __setstate__(self, state): ...

class Float:
    adapted: Any = ...
    def __init__(self, *args, **kwargs): ...
    def getquoted(self): ...
    def __conform__(self, *args, **kwargs): ...

class ISQLQuote:
    _wrapped: Any = ...
    def __init__(self, *args, **kwargs): ...
    def getbinary(self): ...
    def getbuffer(self): ...
    def getquoted(self): ...

class Int:
    adapted: Any = ...
    def __init__(self, *args, **kwargs): ...
    def getquoted(self): ...
    def __conform__(self, *args, **kwargs): ...

class IntegrityError(DatabaseError): ...

class InterfaceError(Error): ...

class InternalError(DatabaseError): ...

class List:
    adapted: Any = ...
    def __init__(self, *args, **kwargs): ...
    def getquoted(self): ...
    def prepare(self, conn): ...
    def __conform__(self, *args, **kwargs): ...

class NotSupportedError(DatabaseError): ...

class Notify:
    channel: Any = ...
    payload: Any = ...
    pid: Any = ...
    def __init__(self, *args, **kwargs): ...
    def __eq__(self, other): ...
    def __ge__(self, other): ...
    def __getitem__(self, index): ...
    def __gt__(self, other): ...
    def __hash__(self): ...
    def __le__(self, other): ...
    def __len__(self, *args, **kwargs): ...
    def __lt__(self, other): ...
    def __ne__(self, other): ...

class OperationalError(DatabaseError): ...

class ProgrammingError(DatabaseError): ...

class QueryCanceledError(OperationalError): ...

class QuotedString:
    adapted: Any = ...
    buffer: Any = ...
    encoding: Any = ...
    def __init__(self, *args, **kwargs): ...
    def getquoted(self): ...
    def prepare(self, conn): ...
    def __conform__(self, *args, **kwargs): ...

class ReplicationConnection(connection):
    autocommit: Any = ...
    isolation_level: Any = ...
    replication_type: Any = ...
    reset: Any = ...
    set_isolation_level: Any = ...
    set_session: Any = ...
    def __init__(self, *args, **kwargs): ...

class ReplicationCursor(cursor):
    io_timestamp: Any = ...
    def __init__(self, *args, **kwargs): ...
    def consume_stream(self, consumer, keepalive_interval=10): ...
    def read_message(self): ...
    def send_feedback(self, write_lsn=0, flush_lsn=0, apply_lsn=0, reply=False): ...
    def start_replication_expert(self, command, decode=False): ...

class ReplicationMessage:
    cursor: Any = ...
    data_size: Any = ...
    data_start: Any = ...
    payload: Any = ...
    send_time: Any = ...
    wal_end: Any = ...
    def __init__(self, *args, **kwargs): ...

class TransactionRollbackError(OperationalError): ...

class Warning(Exception): ...

class Xid:
    bqual: Any = ...
    database: Any = ...
    format_id: Any = ...
    from_string: Any = ...
    gtrid: Any = ...
    owner: Any = ...
    prepared: Any = ...
    def __init__(self, *args, **kwargs): ...
    def __getitem__(self, index): ...
    def __len__(self, *args, **kwargs): ...

class connection:
    DataError: Any = ...
    DatabaseError: Any = ...
    Error: Any = ...
    IntegrityError: Any = ...
    InterfaceError: Any = ...
    InternalError: Any = ...
    NotSupportedError: Any = ...
    OperationalError: Any = ...
    ProgrammingError: Any = ...
    Warning: Any = ...
    async: Any = ...
    async_: Any = ...
    autocommit: Any = ...
    binary_types: Any = ...
    closed: Any = ...
    cursor_factory: Any = ...
    deferrable: Any = ...
    dsn: Any = ...
    encoding: Any = ...
    isolation_level: Any = ...
    notices: Any = ...
    notifies: Any = ...
    protocol_version: Any = ...
    readonly: Any = ...
    server_version: Any = ...
    status: Any = ...
    string_types: Any = ...
    def __init__(self, *args, **kwargs): ...
    def cancel(self): ...
    def close(self): ...
    def commit(self): ...
    def cursor(self, *args, **kwargs): ...
    def fileno(self): ...
    def get_backend_pid(self): ...
    def get_dsn_parameters(self): ...
    def get_parameter_status(self, parameter): ...
    def get_transaction_status(self): ...
    def isexecuting(self): ...
    def lobject(self, *args, **kwargs): ...
    def poll(self): ...
    def reset(self): ...
    def rollback(self): ...
    def set_client_encoding(self, encoding): ...
    def set_isolation_level(self, level): ...
    def set_session(self, *args, **kwargs): ...
    def tpc_begin(self, xid): ...
    def tpc_commit(self, *args, **kwargs): ...
    def tpc_prepare(self): ...
    def tpc_recover(self): ...
    def tpc_rollback(self, *args, **kwargs): ...
    def xid(self, format_id, gtrid, bqual): ...
    def __enter__(self, *args, **kwargs): ...
    def __exit__(self, *args, **kwargs): ...

class cursor:
    arraysize: Any = ...
    binary_types: Any = ...
    closed: Any = ...
    connection: Any = ...
    description: Any = ...
    itersize: Any = ...
    lastrowid: Any = ...
    name: Any = ...
    query: Any = ...
    row_factory: Any = ...
    rowcount: Any = ...
    rownumber: Any = ...
    scrollable: Any = ...
    statusmessage: Any = ...
    string_types: Any = ...
    typecaster: Any = ...
    tzinfo_factory: Any = ...
    withhold: Any = ...
    def __init__(self, *args, **kwargs): ...
    def callproc(self, procname, parameters=None): ...
    def cast(self, oid, s): ...
    def close(self): ...
    def copy_expert(self, sql, file, size=8192): ...
    def copy_from(self, *args, **kwargs): ...
    def copy_to(self, *args, **kwargs): ...
    def execute(self, query, vars=None): ...
    def executemany(self, query, vars_list): ...
    def fetchall(self): ...
    def fetchmany(self, *args, **kwargs): ...
    def fetchone(self): ...
    def mogrify(self, query, vars=None): ...
    def nextset(self): ...
    def scroll(self, *args, **kwargs): ...
    def setinputsizes(self, sizes): ...
    def setoutputsize(self, size, column=None): ...
    def __enter__(self, *args, **kwargs): ...
    def __exit__(self, *args, **kwargs): ...
    def __iter__(self): ...
    def __next__(self): ...

class lobject:
    closed: Any = ...
    mode: Any = ...
    oid: Any = ...
    def __init__(self, *args, **kwargs): ...
    def close(self): ...
    def export(self, filename): ...
    def read(self, *args, **kwargs): ...
    def seek(self, offset, whence=0): ...
    def tell(self): ...
    def truncate(self, len=0): ...
    def unlink(self): ...
    def write(self, str): ...
