#!/usr/bin/env python3

class File(object):
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size
    
    def return_name(self):
        return self.name
    
    def return_size(self):
        return self.size

class Directory(object):
    def __init__(self,name,parent) -> None:
        self.name = name
        self.contents = {}
        self.sizes = 0
        self.subsize = 0
        self.parent = parent
    
    def add_file(self,file):
        self.contents.update({file.return_name():file.return_size()})
        self.sizes = self.sizes + file.return_size()

    def add_directory(self,directory):
        self.contents.update({directory.return_name():0})

    def return_size(self):
        return self.sizes
    
    def return_name(self):
        return self.name

    def return_parent(self):
        return self.parent
    
    def return_contents(self):
        return self.contents
    
    def set_size(self,size):
        self.sizes = size

    def report_root(self):
        root_size = 0
        for item,size in self.contents.items():
            root_size = root_size + size
        return root_size


    def report_size(self):
        subtotal = 0
        for item,size in self.contents.items():
            
            if item in directories.keys():
                subtotal = subtotal +  directories[item].report_size()
            else:
                subtotal = subtotal + size
        directories[self.return_name()].set_size(subtotal)
        return subtotal

directories = {}
directories.update({"/":Directory("/",0)})
active_directory = directories["/"]

file = open("input.txt")
for line in file:
    # If starts with '$ cd', we are changing directories
    if line.startswith("$ cd"):
        split = line.split()
        if split[2] == "/":
            pass
        elif split[2] == "..":
            active_directory = active_directory.return_parent()
        else:
            active_directory = directories[active_directory.return_name() + split[2] + "/"]
    # If '$ ls' in the line, it is a throw-away
    elif line.startswith("$ ls"):
        next
    
    # If line starts with dir, we add a directory
    elif line.startswith("dir"):
        directory_to_add = active_directory.return_name() + line.split()[1] + "/"
        directories.update({directory_to_add:Directory(directory_to_add,active_directory)})
        active_directory.add_directory(directories[directory_to_add])
    
    # If the first character in the line is a number, we have a file 
    elif line[0].isdigit():
        split = line.split()
        size = int(split[0])
        name = split[1]
        file_to_add = File(name,size)
        active_directory.add_file(file_to_add)
    
    else:
        print(f"We have an unknown line: {line}")
        exit
print(f"We have {len(directories)} directories:")
small_dir_sum = 0
size_root = directories["/"].return_size()
sub_size_root = directories["/"].report_size()


large_dir_size = 2143088
smallest_large_dir = 30000000
for directory in directories:
    size = directories[directory].return_size()
    if size < 100001:
        small_dir_sum = small_dir_sum + size
    elif size >large_dir_size:
        if size < smallest_large_dir:
            smallest_large_dir = size

print(f"Small dir size: {small_dir_sum}")
print(f"Smallest large dir to delete: {smallest_large_dir}")