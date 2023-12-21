# writelines() method expects a list of strings to overide the existing data.

mylist = ["My name is Ravi \n","I live in Bhubaneswar \n", "My age is 23\n"]

file = open("Ravi.txt", "w")
file.writelines(mylist)
file.close()

file = open("Ravi.txt","r")
print(file.read())
