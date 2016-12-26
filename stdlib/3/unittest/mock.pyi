# Stubs for unittest.mock

import sys
from typing import Any

if sys.version_info >= (3, 3):
    FILTER_DIR = ...  # type: Any

    class _slotted: ...

    class _SentinelObject:
        name = ...  # type: Any
        def __init__(self, name): ...

    class _Sentinel:
        def __init__(self): ...
        def __getattr__(self, name): ...

    sentinel = ...  # type: Any
    DEFAULT = ...  # type: Any

    class _CallList(list):
        def __contains__(self, value): ...

    class _MockIter:
        obj = ...  # type: Any
        def __init__(self, obj): ...
        def __iter__(self): ...
        def __next__(self): ...

    class Base:
        def __init__(self, *args, **kwargs): ...

    class NonCallableMock(Base):
        def __new__(cls, *args, **kw): ...
        def __init__(self, spec=None, wraps=None, name=None, spec_set=None, parent=None, _spec_state=None, _new_name='', _new_parent=None, _spec_as_instance=False, _eat_self=None, unsafe=False, **kwargs): ...
        def attach_mock(self, mock, attribute): ...
        def mock_add_spec(self, spec, spec_set=False): ...
        return_value = ...  # type: Any
        @property
        def __class__(self): ...
        called = ...  # type: Any
        call_count = ...  # type: Any
        call_args = ...  # type: Any
        call_args_list = ...  # type: Any
        mock_calls = ...  # type: Any
        side_effect = ...  # type: Any
        method_calls = ...  # type: Any
        def reset_mock(self, visited=None): ...
        def configure_mock(self, **kwargs): ...
        def __getattr__(self, name): ...
        def __dir__(self): ...
        def __setattr__(self, name, value): ...
        def __delattr__(self, name): ...
        def assert_not_called(_mock_self): ...
        def assert_called_with(_mock_self, *args, **kwargs): ...
        def assert_called_once_with(_mock_self, *args, **kwargs): ...
        def assert_has_calls(self, calls, any_order=False): ...
        def assert_any_call(self, *args, **kwargs): ...

    class CallableMixin(Base):
        side_effect = ...  # type: Any
        def __init__(self, spec=None, side_effect=None, return_value=..., wraps=None, name=None, spec_set=None, parent=None, _spec_state=None, _new_name='', _new_parent=None, **kwargs): ...
        def __call__(_mock_self, *args, **kwargs): ...

    class Mock(CallableMixin, NonCallableMock): ...

    class _patch:
        attribute_name = ...  # type: Any
        getter = ...  # type: Any
        attribute = ...  # type: Any
        new = ...  # type: Any
        new_callable = ...  # type: Any
        spec = ...  # type: Any
        create = ...  # type: Any
        has_local = ...  # type: Any
        spec_set = ...  # type: Any
        autospec = ...  # type: Any
        kwargs = ...  # type: Any
        additional_patchers = ...  # type: Any
        def __init__(self, getter, attribute, new, spec, create, spec_set, autospec, new_callable, kwargs): ...
        def copy(self): ...
        def __call__(self, func): ...
        def decorate_class(self, klass): ...
        def decorate_callable(self, func): ...
        def get_original(self): ...
        target = ...  # type: Any
        temp_original = ...  # type: Any
        is_local = ...  # type: Any
        def __enter__(self): ...
        def __exit__(self, *exc_info): ...
        def start(self): ...
        def stop(self): ...

    def patch(target, new=..., spec=None, create=False, spec_set=None, autospec=None, new_callable=None, **kwargs): ...

    class _patch_dict:
        in_dict = ...  # type: Any
        values = ...  # type: Any
        clear = ...  # type: Any
        def __init__(self, in_dict, values=..., clear=False, **kwargs): ...
        def __call__(self, f): ...
        def decorate_class(self, klass): ...
        def __enter__(self): ...
        def __exit__(self, *args): ...
        start = ...  # type: Any
        stop = ...  # type: Any

    class MagicMixin:
        def __init__(self, *args, **kw): ...

    class NonCallableMagicMock(MagicMixin, NonCallableMock):
        def mock_add_spec(self, spec, spec_set=False): ...

    class MagicMock(MagicMixin, Mock):
        def mock_add_spec(self, spec, spec_set=False): ...

    class MagicProxy:
        name = ...  # type: Any
        parent = ...  # type: Any
        def __init__(self, name, parent): ...
        def __call__(self, *args, **kwargs): ...
        def create_mock(self): ...
        def __get__(self, obj, _type=None): ...

    class _ANY:
        def __eq__(self, other): ...
        def __ne__(self, other): ...

    ANY = ...  # type: Any

    class _Call(tuple):
        def __new__(cls, value=..., name=None, parent=None, two=False, from_kall=True): ...
        name = ...  # type: Any
        parent = ...  # type: Any
        from_kall = ...  # type: Any
        def __init__(self, value=..., name=None, parent=None, two=False, from_kall=True): ...
        def __eq__(self, other): ...
        __ne__ = ...  # type: Any
        def __call__(self, *args, **kwargs): ...
        def __getattr__(self, attr): ...
        def count(self, *args, **kwargs): ...
        def index(self, *args, **kwargs): ...
        def call_list(self): ...

    call = ...  # type: Any

    def create_autospec(spec, spec_set=False, instance=False, _parent=None, _name=None, **kwargs): ...

    class _SpecState:
        spec = ...  # type: Any
        ids = ...  # type: Any
        spec_set = ...  # type: Any
        parent = ...  # type: Any
        instance = ...  # type: Any
        name = ...  # type: Any
        def __init__(self, spec, spec_set=False, parent=None, name=None, ids=None, instance=False): ...

    def mock_open(mock=None, read_data=''): ...

    class PropertyMock(Mock):
        def __get__(self, obj, obj_type): ...
        def __set__(self, obj, val): ...