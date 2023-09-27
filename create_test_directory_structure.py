import os


def create_directory(path):
    if not os.path.exists(path):
        os.mkdir(path)


def create_text_file(path, content="This is a sample file."):
    with open(path, "w") as f:
        f.write(content)


if __name__ == "__main__":
    base_dir = "test_directory"
    create_directory(base_dir)

    create_text_file(os.path.join(base_dir, "file1.txt"))
    create_text_file(os.path.join(base_dir, "file2.txt"))

    sub_dir = os.path.join(base_dir, "sub_directory")
    create_directory(sub_dir)

    create_text_file(os.path.join(sub_dir, "file3.txt"))
    create_text_file(os.path.join(sub_dir, "file4.txt"))

    sub_sub_dir = os.path.join(sub_dir, "sub_sub_directory")
    create_directory(sub_sub_dir)

    create_text_file(os.path.join(sub_sub_dir, "file5.txt"))
    create_text_file(os.path.join(sub_sub_dir, "file6.txt"))
