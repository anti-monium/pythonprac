import sys

def output(*args, sep='', end='\n', file=sys.stdout, flush=False):
    print(*args, sep=sep, end=end, file=file, flush=flush)

