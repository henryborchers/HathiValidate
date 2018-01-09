import abc
import logging
import typing
from . import result
from . import process

class absValidator(metaclass=abc.ABCMeta):

    def __init__(self):
        self.results :typing.List[result.ResultSummary] = []

    @abc.abstractmethod
    def validate(self):
        pass


class ValidateMissingFiles(absValidator):

    def __init__(self, path):
        super().__init__()
        self.path = path

    def validate(self):
        logger = logging.getLogger(__name__)
        logger.debug("Looking for missing files in {}".format(self.path))
        for missing_file in process.find_missing_files(self.path):
            self.results.append(missing_file)
        # super().validate(path, *args, **kwargs)

class ValidateExtraSubdirectories(absValidator):

    def __init__(self, path):
        super().__init__()
        self.path = path

    def validate(self):
        for extra_subdirectory in process.find_extra_subdirectory(self.path):
            self.results.append(extra_subdirectory)


class ValidateChecksumReport(absValidator):
    def __init__(self, path, checksum_report):
        super().__init__()
        self.path = path
        self.checksum_report = checksum_report

    def validate(self):

        for failing_checksum in process.find_failing_checksums(self.path, self.checksum_report):
            self.results.append(failing_checksum)


class ValidateMetaYML(absValidator):
    def __init__(self, yaml_file, path, required_page_data: bool):
        super().__init__()
        self.yaml_file = yaml_file
        self.path = path
        self.require_page_data = required_page_data

    def validate(self):
        for error in process.find_errors_meta(self.yaml_file, self.path, self.require_page_data):
            self.results.append(error)


class ValidateMarc(absValidator):
    def __init__(self, marc_file):
        super().__init__()
        self.marc_file = marc_file

    def validate(self):
        logger = logging.getLogger(__name__)
        logger.info("Validating {}".format(self.marc_file))
        for error in process.find_errors_marc(filename=self.marc_file):
            self.results.append(error)

class ValidateOCRFiles(absValidator):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def validate(self):
        for error in process.find_errors_ocr(path=self.path):
            self.results.append(error)