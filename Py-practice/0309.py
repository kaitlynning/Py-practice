from functools import partial 
  
def f(a, b, c, x): 
    return 1000*a + 100*b + 10*c + x 
  
# A partial function that calls f with 
# a as 3, b as 1 and c as 4. 
g = partial(f, 3, 1, 4) 

print(g(5)) 
'''
ˇ3145

'''