import os

if os.path.exists("c:/Users/ADMIN/Documents/kbtu/pp2git/lab6/some4.txt"):
    os.remove("c:/Users/ADMIN/Documents/kbtu/pp2git/lab6/some4.txt")
else:
    print("No such file")