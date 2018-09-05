import sys

dna = sys.stdin.readline().strip()

comp = {
    "A": "T",
    "C": "G",
    "G": "C",
    "T": "A"
}

i = len(dna) - 1
out = ""

while i >= 0:
    out += comp[dna[i]]
    i -= 1

print(out)

