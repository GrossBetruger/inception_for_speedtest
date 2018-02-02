import shutil
import os
from sys import argv


def duplicate_file_list(flist, num_of_duplicates):
    for i in range(num_of_duplicates):
        for fname in flist:
            shutil.copy(fname, fname + "_" + str(i))


def clean_file_names(dir_path, junk_pattern):
    for filename in os.listdir(dir_path):
        # old_filename = filename
        # filename.replace(junk_pattern, "")
        # print "names", old_filename, filename
        # print "junk pattern", junk_pattern
        os.rename(os.path.join(dir_path, filename), os.path.join(dir_path, filename.replace(junk_pattern, "")))


if __name__ == "__main__":
    try:
        mode = argv[1]
        dir_path = argv[2]
        if mode == "rename":
            junk_chars = argv[3]
        elif mode == "duplicate":
            propagation_factor = int(argv[3])
        else:
            raise ValueError
    except (IndexError, ValueError):
        print "USAGE: file_manipulator.py rename/duplicate dir_path, chars_to_remove/num_of_duplicates"

    if mode == "duplicate":
        os.chdir(dir_path)
        files = os.listdir(".")
        duplicate_file_list(files, propagation_factor)
    elif mode == "rename":
        clean_file_names(dir_path, junk_chars)