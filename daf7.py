f = open("some1.txt")
t = open("some3.txt", "x")
s = str(f.read())
t.write(s)
t.close()

t = open("some3.txt", "r")
print(t.read())