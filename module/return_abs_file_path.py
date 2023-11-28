import os


# 跟目錄下子目錄
sub_dir = os.listdir()
def find_file_path(image_name):
    try:
        # 遍歷根目錄文件夾
        for dir in sub_dir:
            filepath_to_check = os.path.join(dir, image_name)
            # print(filepath_to_check)
            # 找到文件路徑並返回
            if os.path.exists(filepath_to_check):
                # 圖片路徑
                file_path = os.path.abspath(filepath_to_check)
                # print(file_path)
            # 沒有找到文件路徑
            else:
                # print(False)
                pass
        return file_path
    # 文件路徑不存在，顯示未找到
    except Exception as e:
        print('file not found!')

# 返回圖片路徑/提示未找到
# print(find_file_path(image_name=img_reload))
# find_file_path(image_name=img_reload)