import sys
import kenlm

from collections import Counter


class Resources:

    def __init__(self):
        self.paths = dict()
        self.loaded = dict()

    def load_resources(self):
        sys.stderr.write('LOADING LM: %s ... ' % self.paths['language_model'])
        sys.stderr.flush()
        self.loaded['language_model'] = kenlm.Model(self.paths['language_model'])
        sys.stderr.write('DONE\n')

        sys.stderr.write('LOADING LEX: %s ... ' % self.paths['lexical_table'])
        sys.stderr.flush()
        self.loaded['lexical_table'] = self._load_table(self.paths['lexical_table'])
        sys.stderr.write('DONE\n')

    @staticmethod
    def _load_table(path):
        table = Counter()
        for line in open(path):
            parts = line.strip().split()
            table[parts[0], parts[1]] = float(parts[2])
        return table
