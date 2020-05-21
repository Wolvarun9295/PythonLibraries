#!usr/bin/python

from operator import itemgetter
import sys

current_word = {}

for line in sys.stdin:
    line = line.strip()

    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue
    try:
        current_word[word] = current_word[word] + count
    except:
        current_word[word] = count

for word in current_word.keys():
    print('%s\t%s' % (word, current_word[word]))
