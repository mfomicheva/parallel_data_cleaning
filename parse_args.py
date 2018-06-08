import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s', '--src_path', help='source path'
    )
    parser.add_argument(
        '-t', '--tgt_path', help='target path'
    )
    parser.add_argument(
        '-slm', '--source_lang_model', help='source language model',
        default='toy_resources/lm.tok.de'
    )
    parser.add_argument(
        '-tlm', '--target_lang_model', help='target language model',
        default='toy_resources/lm.tok.en'
    )
    return parser.parse_args()


args = parse_arguments()
