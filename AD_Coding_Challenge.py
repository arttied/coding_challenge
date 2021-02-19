import sys
import numpy as np
  
declen = 2  
numlist = []
line = ''
print("Welcome to the Coding Challenge for Arthur Delsing", file = sys.stdout)
print("Please Enter the Decimal Precision (Default is 2): ", file = sys.stdout)
declen = sys.stdin.readline()
declen = '{%.' + str(declen.strip()) + 'f}'
    

def print_to_stdout(l):
    print("Your Current Mean:", declen%np.mean(l), ", Standard Deviation: ",\
    declen%np.std(l),", and Median: ",declen%np.median(l),file = sys.stdout)

while line != 'q':
    print(f'Please Enter Number or q to quit :', file = sys.stdout)
    line = sys.stdin.readline()
    if line.strip() != 'q':
        line = filter(str.isdigit, line)
        line = "".join(line)
        numlist.append(int(line.strip()))
        print_to_stdout(numlist)
    else:
        break

print("Thank you for the Challenge")