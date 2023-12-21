num1 = int(input("Enter the number of key-value pairs for dict1: "))
num2 = int(input("Enter the number of key-value pairs for dict2: "))
my_dict1={}
my_dict2={}

for i in range(num1):
    key = input("Enter key "+str(i+1)+ " ")
    value = int(input("Enter the value of key: "+str(i+1)+" : "))
    my_dict1[key] = value
    
for i in range(num2):
    key = input("Enter key "+str(i+1)+ " ")
    value = int(input("Enter the value of key: "+str(i+1)+" : "))
    my_dict2[key] = value
    
my_dict1.update(my_dict2)

print("Merged dictionary: ", my_dict1)