import sys

kmers = [line.strip() for line in sys.stdin]
print(kmers[0][:-1] + "".join([k[-1] for k in kmers]))

