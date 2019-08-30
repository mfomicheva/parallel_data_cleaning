from random import randint


operations = ('swap', 'copy_source', 'copy_target','random_source', 'random_target')


def read_file(path):
    return [l.strip() for l in open(path).readlines()]


def generate_synthetic_data(src_path, tgt_path, outpath_src, outpath_tgt):
    sources = read_file(src_path)
    targets = read_file(tgt_path)
    assert len(sources) == len(targets)
    out_src = open(outpath_src, 'w')
    out_tgt = open(outpath_tgt, 'w')
    for src, tgt in zip(sources, targets):
        operation = operations[randint(0, 4)]
        negative_pair = None
        if operation == 'swap':
            negative_pair = (tgt, src)
        elif operation == 'copy_source':
            negative_pair = (src, src)
        elif operation == 'copy_target':
            negative_pair = (tgt, tgt)
        elif operation == 'random_source':
            negative_pair = (sources[randint(0, len(sources) - 1)], tgt)
        elif operation == 'random_target':
            negative_pair = (src, targets[randint(0, len(targets) - 1)])
        else:
            pass
        out_src.write('{}\n'.format(negative_pair[0]))
        out_tgt.write('{}\n'.format(negative_pair[1]))
    out_src.close()
    out_tgt.close()
