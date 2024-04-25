import random

def flo_ran(minv,maxv):
    random_float = random.uniform(0.0, 1.0)
    return minv + (random_float * (maxv - minv))


minv=int(input("Enter a no : "))
maxv=int(input("Enter a no : "))
rno = flo_ran(minv,maxv)
print(f"Random Floating No : {rno}")
