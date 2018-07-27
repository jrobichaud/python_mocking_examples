import unittest.mock


class Callee:
    def __init__(self, member):
        self.member = member

    def do_something(self, method_argument):
        pass


def do_call():
    Callee("Bar").do_something("Foo")


mocked_do_something_method = unittest.mock.Mock(wraps=Callee.do_something)

with unittest.mock.patch.object(
        Callee,
        'do_something',
        new=lambda *args, **kwargs: mocked_do_something_method(*args, **kwargs)):
    do_call()


def test_method_mocking():
    assert mocked_do_something_method.call_count == 1
    method_args, method_kwargs = mocked_do_something_method.call_args
    callee_self, callee_method_argument = method_args
    assert callee_self.member == "Bar"
    assert callee_method_argument == "Foo"
