import itertools as itt

print(*sorted(set(filter(lambda x: 'TOR' in x and 'TOR'  in x.replace('TOR', '', 1) and 'TOR' not in x.replace('TOR', '', 2), list(map(''.join, itt.product(('T', 'O', 'R'), repeat = int(input()))))))), sep = ', ')
