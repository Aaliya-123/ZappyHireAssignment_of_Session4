def count(filename):
    with open(filename, "r") as file:
        con=file.read()
        word=con.split()
        c=len(word)
        print(f"This file has {c} words.")
        

filename=input("Enter file name : ")
count(filename)