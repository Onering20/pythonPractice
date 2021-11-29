from time import perf_counter
from types import FunctionType
import traceback

internal=False

class My_Perf_Counter:
    def __init__(self, name_or_function, suppress_out=False, *args, **kwargs) -> None:
        if isinstance(name_or_function, str):
            self.name = name_or_function
            self.func = None
            self.suppress = True
        elif isinstance(name_or_function, FunctionType):
            self.name = name_or_function.__name__
            self.func = name_or_function
            self.suppress = suppress_out
            if internal:
                self.args = args[0]
                self.kwargs = kwargs["kwargs"]
            else:
                self.args = args
                self.kwargs = kwargs

    def __enter__(self) -> None:
        if self.func == None:
            self.start_time = perf_counter()
        else:

            self.start_time = perf_counter()
            self.output = self.func(*self.args,**self.kwargs)
            if(not self.suppress):print(self.output)

    def __exit__(self, exc_type, exc_value, tb):
        stop_time = perf_counter()
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
            # return False # uncomment to pass exception through
        print(f'{self.name}: {1000*(stop_time - self.start_time):.3f} ms \n')
        return True


def test_function_time(func, suppress=False, *args, **kwargs):
    internal = True #doesn't change the global/Module variable
    with My_Perf_Counter(func, suppress, args, kwargs=kwargs):
            pass
