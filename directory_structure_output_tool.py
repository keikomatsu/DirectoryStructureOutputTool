import os
from tkinter import Tk, filedialog, simpledialog
from datetime import datetime


def list_files(startpath):
    paths_list = []
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, "").count(os.sep)
        indent = " " * 4 * (level)
        paths_list.append("{}{}/".format(indent, os.path.basename(root)))
        subindent = " " * 4 * (level + 1)
        for f in files:
            paths_list.append("{}{}".format(subindent, f))
    return paths_list


def main(output_directory):
    root = Tk()
    root.withdraw()
    directory_path = filedialog.askdirectory(title="どのディレクトリ構造を可視化するのか選択してください")
    file_list = list_files(directory_path)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_path = os.path.join(
        output_directory, "file_structure_{}.txt".format(timestamp)
    )

    with open(output_path, "w", encoding="utf-8") as f:
        for item in file_list:
            f.write("%s\n" % item)

    simpledialog.messagebox.showinfo(
        "情報", "file_structure_{}.txtとして保存しました。".format(timestamp)
    )


if __name__ == "__main__":
    output_dir = input("出力パスを入力してください: ")
    main(output_dir)
