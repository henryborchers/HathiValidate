import abc
import typing
import collections.abc


class Result:
    def __init__(self, result_type):
        self.result_type = result_type
        self.source = None
        self.message = ""

    def __str__(self) -> str:
        if self.source:
            message = '{}: "{}"'.format(self.source, self.message)
        else:
            message = '"{}"'.format(self.message)
        return "{}[{}]{}".format(Result.__name__, self.result_type, message)


class ResultSummary(collections.abc.Iterable):  # type: ignore
    def __init__(self):
        self.results = []
        self.source = None

    def __iadd__(self, other):
        self.results.append(other)
        return self

    def __iter__(self) -> typing.Iterator[Result]:
        return self.results.__iter__()

    def __len__(self):
        return len(self.results)

    def __contains__(self, x):
        return x in self.results


class AbsResultBuilder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_new_summary(self):
        pass

    @abc.abstractmethod
    def add_result(self, result: Result):
        pass

    @abc.abstractmethod
    def get_summary(self) -> ResultSummary:
        pass

    @abc.abstractmethod
    def set_source(self, source):
        pass


class ResultSummaryBuilder(AbsResultBuilder):
    def __init__(self):
        self.summary = None
        self.source = None

    def create_new_summary(self):
        self.summary = ResultSummary()

    def add_result(self, result: Result):
        self.summary += result

    def get_summary(self) -> ResultSummary:
        return self.summary

    def set_source(self, source):
        self.source = source


class SummaryDirector:
    def __init__(self, source):
        self.builder = ResultSummaryBuilder()
        self.builder.create_new_summary()
        self.builder.source = source

    def add_error(self, message):
        new_error = Result("error")
        new_error.message = message
        new_error.source = self.builder.source
        self.builder.add_result(new_error)

    def construct(self) -> ResultSummary:
        return self.builder.get_summary()
