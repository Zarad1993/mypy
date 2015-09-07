# Stubs for tornado.ioloop (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from tornado.util import Configurable

signal = ... # type: Any

class TimeoutError(Exception): ...

class IOLoop(Configurable):
    NONE = ... # type: Any
    READ = ... # type: Any
    WRITE = ... # type: Any
    ERROR = ... # type: Any
    @staticmethod
    def instance(): ...
    @staticmethod
    def initialized(): ...
    def install(self): ...
    @staticmethod
    def clear_instance(): ...
    @staticmethod
    def current(instance=True): ...
    def make_current(self): ...
    @staticmethod
    def clear_current(): ...
    @classmethod
    def configurable_base(cls): ...
    @classmethod
    def configurable_default(cls): ...
    def initialize(self, make_current=None): ...
    def close(self, all_fds=False): ...
    def add_handler(self, fd, handler, events): ...
    def update_handler(self, fd, events): ...
    def remove_handler(self, fd): ...
    def set_blocking_signal_threshold(self, seconds, action): ...
    def set_blocking_log_threshold(self, seconds): ...
    def log_stack(self, signal, frame): ...
    def start(self): ...
    def stop(self): ...
    def run_sync(self, func, timeout=None): ...
    def time(self): ...
    def add_timeout(self, deadline, callback, *args, **kwargs): ...
    def call_later(self, delay, callback, *args, **kwargs): ...
    def call_at(self, when, callback, *args, **kwargs): ...
    def remove_timeout(self, timeout): ...
    def add_callback(self, callback, *args, **kwargs): ...
    def add_callback_from_signal(self, callback, *args, **kwargs): ...
    def spawn_callback(self, callback, *args, **kwargs): ...
    def add_future(self, future, callback): ...
    def handle_callback_exception(self, callback): ...
    def split_fd(self, fd): ...
    def close_fd(self, fd): ...

class PollIOLoop(IOLoop):
    time_func = ... # type: Any
    def initialize(self, impl, time_func=None, **kwargs): ...
    def close(self, all_fds=False): ...
    def add_handler(self, fd, handler, events): ...
    def update_handler(self, fd, events): ...
    def remove_handler(self, fd): ...
    def set_blocking_signal_threshold(self, seconds, action): ...
    def start(self): ...
    def stop(self): ...
    def time(self): ...
    def call_at(self, deadline, callback, *args, **kwargs): ...
    def remove_timeout(self, timeout): ...
    def add_callback(self, callback, *args, **kwargs): ...
    def add_callback_from_signal(self, callback, *args, **kwargs): ...

class _Timeout:
    deadline = ... # type: Any
    callback = ... # type: Any
    tiebreaker = ... # type: Any
    def __init__(self, deadline, callback, io_loop): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...

class PeriodicCallback:
    callback = ... # type: Any
    callback_time = ... # type: Any
    io_loop = ... # type: Any
    def __init__(self, callback, callback_time, io_loop=None): ...
    def start(self): ...
    def stop(self): ...
    def is_running(self): ...
