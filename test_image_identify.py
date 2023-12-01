import config
from module import file_operator
import pyautogui


# img_list = []

# 圖片名字
# img_apply_balance = image_config.img_apply_balance
# redeem_box = image_config.redeem_box
# img_applied = image_config.applied
# img_reload = image_config.reload
# img_successful = image_config.successful

# 返回圖片絕對路徑
# print(return_abs_file_path.find_file_path(img_successful))
# img_path_apply_balance = return_abs_file_path.find_file_path(img_apply_balance)
# img_path_redeem_box = return_abs_file_path.find_file_path(redeem_box)
# img_path_img_applied = return_abs_file_path.find_file_path(img_applied)
# img_path_img_reload = return_abs_file_path.find_file_path(img_reload)
# img_path_img_successful = return_abs_file_path.find_file_path(img_successful)
# print(img_path_img_successful)

def find_icon(image_path):
    print(image_path)
    # try:
    img_pos_box = pyautogui.locateOnScreen('/image', confidence=0.7)
    print(img_pos_box)
    # img_center_point = pyautogui.center(img_pos_box)
    # # print(img_center_point)
    # pyautogui.moveTo(img_center_point)
    # pyautogui.doubleClick(duration=1)
    # except TypeError:
    #     print('{i} did not match. Please try again.'.format(i=image_path.split('\\')[-1]))
# find_icon(img_path_apply_balance)