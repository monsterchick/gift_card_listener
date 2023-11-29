import os
import pytesseract
import config
from module import return_abs_file_path
import pyautogui


# 設定Tesseract的安裝路徑
pytesseract.pytesseract.tesseract_cmd = config.tesseract_path

# print(config.tesseract_path)

# 圖片名字
img_apply_balance = config.img_apply_balance
redeem_box = config.redeem_box
img_applied = config.applied
img_reload = config.reload
img_successful = config.successful

# 返回圖片絕對路徑
# print(return_abs_file_path.find_file_path(img_successful))
img_path_apply_balance = return_abs_file_path.find_file_path(img_apply_balance)
img_path_redeem_box = return_abs_file_path.find_file_path(redeem_box)
img_path_img_applied = return_abs_file_path.find_file_path(img_applied)
img_path_img_reload = return_abs_file_path.find_file_path(img_reload)
img_path_img_successful = return_abs_file_path.find_file_path(img_successful)
# print(img_path_img_successful)



def redeem_card(image_path):
    '''
    :param image_path: 圖片的絕對路徑
    :return: 激活卡操作
    '''

    try:

        # 進行文字識別
        txt_apply = pytesseract.image_to_string(image_path)
        # print(txt_apply)

        # 圖片四角坐標
        # print('q',image_path)
        btn_location = pyautogui.locateOnScreen(image_path, confidence=0.3)
        print(btn_location)

        img_center_point = pyautogui.center(btn_location)
        # print(img_center_point)

        # 鼠標移動到按鈕中心
        pyautogui.moveTo(img_center_point)
        # 雙擊間隔為1秒
        # pyautogui.doubleClick(duration=1)

        # 鼠標跟蹤（需要在CMD裡面執行python文件
        # mouse_position = pyautogui.displayMousePosition()
        # print(mouse_position)

    except Exception as e:
        print('Not Found!')

def screenshot():
    '''

    :return: 截圖 + 發群 + 調用refresh_page()
    '''
def listen_wechat():
    '''

    :return: 監聽發卡（每隔兩秒截圖），
    有卡時調用redeem_card(), screenshot(),
    沒卡時隨機調用refresh_page()
    '''
    pass
def refresh_page():
    '''
    :return: 刷新頁面 + 回車確認 + 清理激活碼
    '''
    pass

redeem_card(img_path_apply_balance)
