student = {
    "name" : "ravi",
    "college" : "silicon",
    "age" : 23
    }

x = list(student.keys())
y = list(student.values())
x.extend(y)

print(x)