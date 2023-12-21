# create a new file 
# write two statements
# close the file

"""
file = open("Ravi.txt","r")
file.write("We are learning Python \n")
file.write("Silicon Institute")
file.close()
"""
file = open("Ravi.txt","w")
myList = ["We are learning Python \n", "Silicon Institute"]
file.writelines(myList)
file.close()



