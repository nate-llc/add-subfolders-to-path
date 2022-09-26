import os
import sys
def add_subfolders_to_sys_path(current_directory, DEBUG = False):
    folders_in_directory = []

    for dir in os.walk(current_directory):
        if '.' not in str(dir[0]) and dir[0] != current_directory and dir[0] not in sys.path: #dir is a tuple of files, [0] is the folder which contains the files
            folders_in_directory.append(dir[0]) #if there isn't a . in the ENTIRE FOLDER PATH, and it's not the directory you're already in, append folder to list

    if DEBUG:
        for folder in sys.path:
            print(folder)
        print(len(sys.path), '\n')
    for value in folders_in_directory:
        sys.path.append(value) #add folders to sys.path

    if DEBUG:
        for folder in sys.path:
            print(folder)
        print(len(sys.path), '\n')


directory = os.getcwd() #use this if you just want the subfolders of your current working directory (as said by os.getcwd()0)
# directory = 'C:\\Users\\natey\\vscode' #this should be the top-most folder you want to add.
add_subfolders_to_sys_path(directory, DEBUG = True) 
