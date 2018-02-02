import shutil
import os
from sys import argv


def duplicate_file_list(flist, num_of_duplicates):
    for i in range(num_of_duplicates):
        for fname in flist:
            shutil.copy(fname, fname + "_" + str(i))

if __name__ == "__main__":
    try:
        dir_path = argv[1]
        propagation_factor = int(argv[2])
    except (IndexError, ValueError):
        print "USAGE: file_manipulator.py dir_path, num_of_duplicates"
    os.chdir(dir_path)
    files = os.listdir(".")
    duplicate_file_list(files, propagation_factor)
