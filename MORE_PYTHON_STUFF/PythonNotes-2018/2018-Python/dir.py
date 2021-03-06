#!/usr/bin/python

# The built-in function dir() is used to find out which names a module
# defines. It returns a sorted list of strings:
#
# >>> import fibo, sys
# >>> dir(fibo)
# ['__name__', 'fib', 'fib2']
# >>> dir(sys)
# ['__displayhook__', '__doc__', '__excepthook__', '__loader__', '__name__',
#  '__package__', '__stderr__', '__stdin__', '__stdout__',
#  '_clear_type_cache', '_current_frames', '_debugmallocstats', '_getframe',
#  '_home', '_mercurial', '_xoptions', 'abiflags', 'api_version', 'argv',
#  'base_exec_prefix', 'base_prefix', 'builtin_module_names', 'byteorder',
#  'call_tracing', 'callstats', 'copyright', 'displayhook',
#  'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix',
#  'executable', 'exit', 'flags', 'float_info', 'float_repr_style',
#  'getcheckinterval', 'getdefaultencoding', 'getdlopenflags',
#  'getfilesystemencoding', 'getobjects', 'getprofile', 'getrecursionlimit',
#  'getrefcount', 'getsizeof', 'getswitchinterval', 'gettotalrefcount',
#  'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
#  'intern', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path',
#  'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1',
#  'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit',
#  'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout',
#  'thread_info', 'version', 'version_info', 'warnoptions']
#
# Without arguments, dir() lists the names you have defined currently:
#
# >>> a = [1, 2, 3, 4, 5]
# >>> import fibo
# >>> fib = fibo.fib
# >>> dir()
# ['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
#
# Note that it lists all types of names: variables, modules, functions,
# etc.
#
# dir() does not list the names of built-in functions and variables. If
# you want a list of those, they are defined in the standard module
# builtins:
#
# >>> import builtins
# >>> dir(builtins)
# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
#  'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
#  'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
#  'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
#  'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
#  'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
#  'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
#  'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
#  'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
#  'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
#  'NotImplementedError', 'OSError', 'OverflowError',
#  'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
#  'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
#  'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
#  'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
#  'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
#  'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
#  'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
#  '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
#  'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
#  'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
#  'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
#  'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
#  'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
#  'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
#  'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
#  'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
#  'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
#  'zip']
