import sys
from string import punctuation


class Units:

    def get_units(self, initial_input, unit):
        if unit == 'sentence':
            return initial_input.strip()
        elif unit == 'words':
            return initial_input.strip().split()
        elif unit == 'numbers':
            return self._get_numbers(initial_input.strip().split())
        elif unit == 'alphanums':
            return self._get_alphanums(initial_input.strip().split())
        elif unit in '.,:;!?':
            return self._get_punct_mark(initial_input.strip().split(), unit)
        elif unit == 'punctuation':
            return self._get_punct_marks(initial_input.strip().split())
        else:
            sys.stderr.write('Error! Invalid unit type {}\n'.format(unit))

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
