from itertools import permutations
txt=input("Enter the string")
l=permutations(txt)
for i in l:
    print(''.join(i))
# took help frm net