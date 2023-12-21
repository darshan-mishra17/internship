num_pairs = int(input("Enter the number of key-value pairs: "))

new_dict =  {}

for i in range(num_pairs):
    key = input("Enter key "+str(i+1)+ " ")
    value = int(input("Enter the value of key: "+str(i+1)+" : "))
    new_dict[key] = value # or update()
    
print(new_dict)
print(sum(new_dict.values()))