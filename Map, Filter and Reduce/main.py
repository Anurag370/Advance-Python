lst = [1,2,3,4,5,6,7,8,9,10]

# MAP
## Vanila Function
def square(x):
    return x**2
newl = list(map(square,lst))
print("Vanila Function: ",newl)

## Lambda Function
newl = list(map(lambda x: x**3,lst))
print("With Lambda: ",newl)

# FILTER
## Vanila Function
def even(x):
    if x%2==0:
        return 1
newl = list(filter(even,lst))
print(newl)

## Lambda Function
newl = list(filter(lambda x: x%2==0,lst))
print(newl)

# REDUCE
from functools import reduce #Needed to  use reduce

newl = reduce(lambda x,y: x+y,lst)
print(newl)