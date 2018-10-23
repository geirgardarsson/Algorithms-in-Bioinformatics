import sys
from collections import defaultdict

k = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

d = defaultdict(int)

for i in range(0, len(s) - k + 1):
    d[s[i:i+k]] += 1

for key in d:
    print(key)

