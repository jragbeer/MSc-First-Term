#!/usr/bin/env python

from operator import itemgetter
import sys

new = list()
other = {}

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    word, count = line.split()
    yy = word.replace(';', '').replace(')', '').replace('(', '').replace('\\', '').replace('/', '').replace('#', '').replace(':', '').replace('"', '').replace("!", "").replace('.', '').replace(',', "").replace('?', '').lower()
    new.append((yy,1))
for x in new:
    if x[0] in other:
        other[x[0]]= other[x[0]]+1
    else:
        other[x[0]] = 1


sorted_by_value = sorted(other.items(), key=lambda kv: kv[1])
for x in sorted_by_value[::-1][:10]:
    print(x)
