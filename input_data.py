import sys
from string import punctuation


class InputData:

    def __init__(self):
        self.source = None
        self.target = None
        self.source_or_target = None

    def get_input_representation(self, source, target, unit_type):
        self.source = self._transform_input(source, unit_type)
        self.target = self._transform_input(target, unit_type)

    def set_source_or_target(self, source_or_target, unit_type):
        self.source_or_target = self._transform_input(source_or_target, unit_type)

    def _transform_input(self, source_or_target, unit_type):
        if unit_type == 'sentence':
            return source_or_target.strip()
        elif unit_type == 'words':
            return source_or_target.strip().split()
        elif unit_type == 'numbers':
            return self._get_numbers(source_or_target.strip().split())
        elif unit_type == 'alphanums':
            return self._get_alphanums(source_or_target.strip().split())
        elif unit_type in '.,:;!?':
            return self._get_punct_mark(source_or_target.strip().split(), unit_type)
        elif unit_type == 'punctuation':
            return self._get_punct_marks(source_or_target.strip().split())
        else:
            sys.stderr.write('Error! Invalid unit type {}\n'.format(unit_type))

    @staticmethod
    def _get_punct_marks(tokens):
        result = []
        for token in tokens:
            if token in punctuation:
                result.append(token)
        return result

    @staticmethod
    def _get_punct_mark(tokens, mark):
        result = []
        for token in tokens:
            if token == mark:
                result.append(token)
        return result

    @staticmethod
    def _get_numbers(tokens):
        result = []
        for token in tokens:
            if all(char.isdigit() for char in token):
                result.append(token)
        return result

    @staticmethod
    def _get_alphanums(tokens):
        result = []
        for token in tokens:
            token = token.replace('-', '')
            if not token.isalpha():
                result.append(token)
        return result
