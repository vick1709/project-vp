#print the mean of the data.txt

import sys

summation =0
n = 0


# sum input values
for number in open('data.txt'):
	summation += float(number)
	n += 1

print summation/n
