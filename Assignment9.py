import random

def ran(filename):
    n = random.randint(0, 50)  
    with open(filename, "a") as file:
      file.write(str(n) + "\n")
    print(f"Random number {n} saved to '{filename}'.")
    
    
filename = "random_numbers.txt"

ran(filename)