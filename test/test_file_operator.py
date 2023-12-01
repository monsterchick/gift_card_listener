from module import file_operator


f = file_operator.File()
f.find_root_dir()
# print(f.find_root_dir())

f.find_current_dir()
# print(f.find_current_dir())

f.find_file_path(image_name='redeem_box.png')