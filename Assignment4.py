def create_file(filename, con):
        with open(filename, "w") as file:
            file.write(con)
        print("File created succesfully!")


con=input("Enter content : ")
filename=input("Enter file name : ")
create_file(filename,con)