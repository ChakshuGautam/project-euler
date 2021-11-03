from collections import Counter


def list_difference(a, b):
    count = Counter(a)  # count items in a
    count.subtract(b)   # subtract items that are in b
    diff = []
    for x in a:
        if count[x] > 0:
           count[x] -= 1
           diff.append(x)
    return diff