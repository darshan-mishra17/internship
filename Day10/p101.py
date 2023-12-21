file_name=input("enter file name:")
with open(file_name,"r") as file:
    for i in file:
        for j in i:
            print(j)
