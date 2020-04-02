from itertools import groupby
from operator import itemgetter

a = [{"n": i%2 } for i in range(10)]
a.sort(key=itemgetter('n'))
print(a)

# for n, al in groupby(a, key=itemgetter('n')):
#     print(len(al))


print([{"n": len(list(al)), "n2": len(list(al))}for n, al in groupby(a, key=itemgetter('n'))])