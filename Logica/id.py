v1 = "a"
v2 = "a"
v3 = "b"

print(id(v1))

if id(v1) == id(v2):
    print(True)
else:
    print(False)

if id(v1) == id(v3):
    print(True)
else:
    print(False)
