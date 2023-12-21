num = int(input("Enter a number: "))

new_dict={}

for i in range(1, num+1):
    new_dict[i] = i*i
    
print(new_dict)