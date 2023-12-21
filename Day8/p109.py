txt=input("enter a string")
nwtxt=''
for i in txt:
    nwtxt=i+nwtxt
if nwtxt == txt:
    print("Palindrome")
else:
    print("not palindrome")