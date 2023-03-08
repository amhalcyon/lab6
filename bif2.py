s = str(input())
u = 0
l = 0
for i in s:
    if i.isupper():
        u += 1
    elif i.islower():
        l += 1

print("Upper case letters:", u)
print("Lowe case letters:", l)