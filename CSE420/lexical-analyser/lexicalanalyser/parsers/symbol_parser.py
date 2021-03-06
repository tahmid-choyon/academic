import _io
from typing import List

from lexicalanalyser.parsers.base import BaseParser


class SymbolParser(BaseParser):
    NAME = "Other"
    REGEX_STR = ';|\\(|\\)|{|}|\\[|\\]'

    def get_parsed_data(self, file_reader: _io.TextIOWrapper) -> List:
        return list(
            set(
                super(SymbolParser, self).get_parsed_data(file_reader)
            )
        )
