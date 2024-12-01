import sys
from collections import Counter

if len(sys.argv) != 2:
    print("usage: python3 main.py <filename>")
    sys.exit(1)

with open(sys.argv[1]) as f:
    col1, col2 = zip(*(map(int, line.split()) for line in f))

print(sum(abs(a - b) for a, b in zip(sorted(col1), sorted(col2))))
print(sum(x * Counter(col2)[x] for x in col1))
