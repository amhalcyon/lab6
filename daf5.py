mylist = ["hey", "fff", "ggg"]
f = open("some2.txt", "x")
f.write("".join(mylist))
f.close

f = open("some2.txt", "r")
print(f.read())