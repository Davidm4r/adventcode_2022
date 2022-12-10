
import re

class Directory:
    
    def __init__(self, name):
        self.name = name
        self.files = []
        self.directories = []
        self.previous_directory = ''
        
    def add_file(self, file_object):
        self.files.append(file_object)
        
    def add_directory(self, directory):
        self.directories.append(directory)
        
class File:
  def __init__(self, name, size):
    self.name = name
    self.size = size

list_of_directories = []
current_directory = Directory('/')
prev_directory = ''



def detect_dommand(line):
    global current_directory
    global prev_directory
    print(f"CURRENT DIRECTORY: {current_directory}")
    print(f"PREV DIRECTORY: {prev_directory}")
    back_directory = re.match(r"\$ cd \.\.", line)
    change_directory =  re.match(r"\$ cd (.*)", line)
    file_info = re.match(r"(\d+) (\w.*)", line)
    dir_info = re.match(r"dir (\w.*)", line)
   
    if back_directory:
        print(f"[{line}] Back directory {current_directory}")
        current_directory = current_directory.previous_directory

    elif change_directory:
        print(f"[{line}] Change directory to {change_directory.group(1)}")
        ##names_list_of_directories = [o.name for o in list_of_directories]
        if change_directory.group(1) in [o.name for o in current_directory.directories]:
            directory = current_directory.directories[[o.name for o in current_directory.directories].index(change_directory.group(1))]
        else:
            directory = Directory(change_directory.group(1))
        list_of_directories.append(directory)
        directory.previous_directory = current_directory
        current_directory = directory
   
    elif file_info:
        file_size = file_info.group(1)
        file_name = file_info.group(2)
        file_object = File(file_name, file_size)
        current_directory.add_file(file_object)
    elif dir_info:
        name_dir = dir_info.group(1)
        dir_object = Directory(name_dir)
        current_directory.add_directory(dir_object)

def calculate_size_per_directory(directory, sum_data):
    print("------------ AHHHHHH -------")
    print(f"Dir object: {directory}")
    print(f"Dir name: {directory.name}")
    print(f"Files: {directory.files}")
    print(f"Directories: {[a.name for a in directory.directories]}")
    for f in directory.files:
        sum_data += int(f.size)
    for directory in directory.directories:
        sum_data+= calculate_size_per_directory(directory, sum_data)
    return sum_data
        

filepath = 'input.txt'

with open(filepath) as fd:
    total_sum_priority = 0
    num_line = 0
    lines = fd.read().splitlines()
    for line in lines:
        detect_dommand(line)
        num_line+=1
        print(num_line)

print("\n\n\n")
print("LISTA DIRECTORIOS")    
total=0
for directory in list_of_directories:
    sum_data = 0
    print(f"NAME: {directory.name}")
    print(f"DIRECTORIES: {[d.name for d in directory.directories]}")
    print(f"FILES: {[(f.name, f.size) for f in directory.files]}")
    #print(f"PREVIOUS DIRECTORY: {directory.previous_directory}")
    #print("-----------")
    size_directory = (calculate_size_per_directory(directory, sum_data))
    #print(f"SIZE:{size_directory}")
    print(f"SIZE DIR {size_directory}")
    if size_directory < 100000:
        total+=size_directory
    print("\n")


print(total)

