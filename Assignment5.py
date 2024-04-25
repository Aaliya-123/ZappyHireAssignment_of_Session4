def poem(filename):
    with open(filename, "r") as file:
      for line in file:
        print(line, end="")
        
        
file = "poem.txt"
poem(file)