import sys


def parse_args_with_help(parser):
    try:
        args = parser.parse_args()
        return args
    except:
        parser.print_help()
        sys.exit(0)
