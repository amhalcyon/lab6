import os

path = "c:/Users/ADMIN/Documents/kbtu/pp2git/"

print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("Files and all directories:")
print([ name for name in os.listdir(path)])
print("Files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])