import os
import re

def search_and_modify_files(parent_folder, target_file_extension, code_to_add, target_line_number):
    # 步驟1：確定父資料夾存在且為絕對路徑
    if not os.path.exists(parent_folder):
        print(f"錯誤：父資料夾 '{parent_folder}' 不存在。")
        return

    parent_folder = os.path.abspath(parent_folder)

    # 步驟2：遍歷父資料夾及其子資料夾
    for root, _, files in os.walk(parent_folder):
        for file in files:
            if file.endswith(target_file_extension):
                file_path = os.path.join(root, file)

                # 步驟3：在目標檔案中尋找指定程式碼位置，並加入新程式碼
                with open(file_path, 'r') as f:
                    lines = f.readlines()

                if len(lines) >= target_line_number:
                    lines[target_line_number - 1] = lines[target_line_number - 1].rstrip() + code_to_add + "\n"

                with open(file_path, 'w') as f:
                    f.writelines(lines)

                print(f"已修改檔案：{file_path}")

if __name__ == "__main__":
    # 設定父資料夾路徑、目標檔案擴展名、要加入的程式碼，以及目標程式碼位置
    parent_folder = "D:/MA/29_幫欣宜輸出的IS影片/ISPRING_輸出完成/test"  # 替換成你的父資料夾路徑
    target_file_extension = "player.js"  # 要搜尋的目標檔案擴展名
    code_to_add = "document.oncontextmenu=function(e){return false;}"  # 要加入的程式碼
    target_line_number = 20  # 要加入程式碼的目標程式碼位置

    search_and_modify_files(parent_folder, target_file_extension, code_to_add, target_line_number)
