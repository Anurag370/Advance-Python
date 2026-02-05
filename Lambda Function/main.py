# Vanila way to define a function
#def double(x):
#    return x*2

# Lambda Way
def addSix(fx,val):
    return 6+fx(val)

sq = lambda x: x**2
cb = lambda x: x**3

print(addSix(sq,4))
print(addSix(cb,2))

#