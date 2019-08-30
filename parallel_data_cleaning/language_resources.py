import faiss
import kenlm
import numpy as np
import sys

from collections import defaultdict


class Resources:

    def __init__(self):
        self.paths = dict()
        self.loaded = dict()

    def load_resources(self):
        if self.paths['language_model']:
            sys.stderr.write('LOADING LM: %s ... ' % self.paths['language_model'])
            sys.stderr.flush()
            self.loaded['language_model'] = kenlm.Model(self.paths['language_model'])
            sys.stderr.write('DONE\n')

        if self.paths['lexical_table']:
            sys.stderr.write('LOADING LEX: %s ... ' % self.paths['lexical_table'])
            sys.stderr.flush()
            self.loaded['lexical_table'] = self._load_table(self.paths['lexical_table'])
            sys.stderr.write('DONE\n')

        if self.paths['embeddings']:
            sys.stderr.write('LOADING EMBEDDINGS: %s ... ' % self.paths['embeddings'])
            sys.stderr.flush()
            self.loaded['embeddings'] = self._load_embeddings(self.paths['embeddings'])
            sys.stderr.write('DONE\n')

    @staticmethod
    def _load_embeddings(fname, dim=1024, verbose=False):
        x = np.fromfile(fname, dtype=np.float32, count=-1)
        x.resize(x.shape[0] // dim, dim)
        if verbose:
            print(' - Embeddings: {:s}, {:d}x{:d}'.format(fname, x.shape[0], dim))
        faiss.normalize_L2(x)
        return x

    @staticmethod
    def _load_table(path):
        table = defaultdict(dict)
        for line in open(path):
            parts = line.strip().split()
            table[parts[0]][parts[1]] = float(parts[2])
        return table
