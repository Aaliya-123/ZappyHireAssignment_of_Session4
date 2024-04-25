try:
  filename = input("Enter the filename: ")
  with open(filename, "r") as file:
    print(f"File contents of {filename}:")
    for line in file:
      print(line, end="")

except FileNotFoundError:
  print("This file does not exist!")
