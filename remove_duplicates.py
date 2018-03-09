import os 
from re import search


def remove_duplicates(dir_path):
    files = [os.path.join(dir_path, file_name) for file_name in os.listdir(dir_path)]
    for fpath in files:
        if search(".+?jpg.+?jpg", fpath):
            os.unlink(fpath)


if __name__ == "__main__":
    os.chdir("training_set")
    for set_dir_path in os.listdir("."):
        remove_duplicates(set_dir_path)

