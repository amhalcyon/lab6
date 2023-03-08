import os

print('Exist:', os.access("c:/Users/ADMIN/Documents/kbtu/pp2git/lab6/bif1.py", os.F_OK))
print('Readable:', os.access("c:/Users/ADMIN/Documents/kbtu/pp2git/lab6/bif1.py", os.R_OK))
print('Writable:', os.access("c:/Users/ADMIN/Documents/kbtu/pp2git/lab6/bif1.py", os.W_OK))
print('Executable:', os.access("c:/Users/ADMIN/Documents/kbtu/pp2git/lab6/bif1.py", os.X_OK))