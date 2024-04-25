try:
  n1 = input("Enter 1st number: ")
  n2 = int(input("Enter 2nd number: "))
  sum = n1 + n2
  print("Sum = ", sum)
except TypeError:
  print("The two inputs must be numerical! Try Again.")
