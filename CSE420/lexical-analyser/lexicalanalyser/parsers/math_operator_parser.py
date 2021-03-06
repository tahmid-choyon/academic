import _io
from typing import List

from lexicalanalyser.parsers.base import BaseParser


class MathOperatorParser(BaseParser):
    NAME = "MathOperator"
    REGEX_STR = '\\+|-|\\*|/|\\^|='

    def get_parsed_data(self, file_reader: _io.TextIOWrapper) -> List:
        return list(
            set(
                super(MathOperatorParser, self).get_parsed_data(file_reader)
            )
        )
