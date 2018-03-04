import shutil
import os
from sys import argv


def is_parent_dir(dir_path):
    return all(os.path.isdir(os.path.join(dir_path, x)) for x in os.listdir(dir_path))


def duplicate_dir(dir_path, propagation_factor):
    os.chdir(dir_path)
    files = os.listdir(".")
    duplicate_file_list(files, propagation_factor)


def duplicate_file_list(flist, num_of_duplicates):
    for i in range(num_of_duplicates):
        for fname in flist:
            suffix = fname.split(".")[-1]
            shutil.copy(fname, fname + "_" + str(i) + "." + suffix)


def clean_file_names(dir_path, junk_pattern):
    for filename in os.listdir(dir_path):
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
        if is_parent_dir(dir_path):
            for child_dir in [os.path.join(os.getcwd(), dir_path, x) for x in os.listdir(dir_path) if not x.startswith(".")]:
                print "duplicating: ", child_dir
                duplicate_dir(child_dir, propagation_factor)
        else:
            print "duplicating", dir_path
            duplicate_dir(dir_path, propagation_factor)

    elif mode == "rename":
        clean_file_names(dir_path, junk_chars)
