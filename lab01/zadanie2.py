import shutil

src_path = input()


def copy_image(filename):
    shutil.copy("{}".format(filename), "lab1zad2.png")

    print("Copied")


copy_image(src_path)
