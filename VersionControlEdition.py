import os
from tkinter import Tk, filedialog
from datetime import datetime


def list_files(startpath):
    paths_list = []
    raw_paths = []
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, "").count(os.sep)
        indent = " " * 4 * (level)
        folder_name = os.path.basename(root)
        paths_list.append(f"{indent}{folder_name}/")
        raw_paths.append(f"{folder_name}/")

        subindent = " " * 4 * (level + 1)
        for f in files:
            paths_list.append(f"{subindent}{f}")
            raw_paths.append(f)
    return paths_list, raw_paths


def read_old_file(old_file_path):
    if os.path.exists(old_file_path):
        with open(old_file_path, "r", encoding="utf-8") as f:
            return [x.strip() for x in f.readlines()]
    else:
        return []


def main(output_directory):
    root = Tk()
    root.withdraw()

    directory_path = filedialog.askdirectory(title="どのディレクトリ構造を可視化するか選択してください")
    after_info = os.path.basename(directory_path)

    new_file_list, new_raw_list = list_files(directory_path)

    old_file_path = filedialog.askopenfilename(title="比較する古いテキストファイルを選択してください")
    before_info = os.path.basename(old_file_path)

    old_file_list = read_old_file(old_file_path)

    diff_added = set(new_raw_list) - set(old_file_list)
    diff_removed = set(old_file_list) - set(new_raw_list)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M_%S")
    plain_output_path = os.path.join(
        output_directory, f"file_structure_{timestamp}_plain.txt"
    )
    diff_output_path = os.path.join(
        output_directory, f"file_structure_{timestamp}_diff.txt"
    )

    # 差分情報なしのプレーンなテキストファイル
    with open(plain_output_path, "w", encoding="utf-8") as f:
        f.write(f"Before: {before_info}\n")
        f.write(f"After: {after_info}\n\n")
        for line in new_file_list:
            f.write(f"{line}\n")

    # 差分情報が含まれたテキストファイル
    with open(diff_output_path, "w", encoding="utf-8") as f:
        f.write(f"Before: {before_info}\n")
        f.write(f"After: {after_info}\n\n")
        for i, line in enumerate(new_file_list):
            prefix = "+ " if new_raw_list[i] in diff_added else ""
            f.write(f"{prefix}{line}\n")

        for line in diff_removed:
            indentation = " " * 4 * (line.count("/") - 1)
            f.write(f"{indentation}- {line}\n")


if __name__ == "__main__":
    output_dir = input("出力パスを入力してください: ")
    main(output_dir)
