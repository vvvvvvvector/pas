import shutil

src_path = input()


def copy_text_file(filename):
    shutil.copy("{}".format(filename), "lab1zad1.txt")

    print("Copied")


copy_text_file(src_path)
