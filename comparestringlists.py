import sys

'''
Script to compare two lists of strings,
one list is my output, the other is the
correct output from Rosalind.
'''

output = open("output.txt", "r")
output = [line.strip() for line in output]

correct = open("correct.txt", "r")
correct = [line.strip() for line in correct]

errors = []

for i in range(0, len(correct)):
    if output[i] != correct[i]:
        errors.append((i+1, output[i], correct[i]))

if len(errors) > 0:
    for error in errors:
        print(error)

else:
    print("no errors")

