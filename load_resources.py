import kenlm


def load_lm(path):
    return kenlm.Model(path)


def load_lexical_table():
    return None
