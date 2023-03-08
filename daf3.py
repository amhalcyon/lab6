import os

path = "c:/Users/ADMIN/Documents/kbtu/pp2git/lab6/bif1.py"

print(os.path.exists(path))
print("Filename:")
print(os.path.basename(path))
print("Directory portion:")
print(os.path.dirname(path))