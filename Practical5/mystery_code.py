# What does this piece of code do?
# Answer:Generate ten random integers from 1 to 100 and prints the last generated integer

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
#The loop is repeated 10 times
while progress<10:
        progress+=1
#Generate a random integer between 1 and 100
        n = randint(1,100)
#The last integer generated is printed after the loop is completed
print(n)
