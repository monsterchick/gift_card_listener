import os
import re
import time
from datetime import datetime
import pyautogui
import pytesseract
import config
from module import file_operator


# 設定Tesseract的安裝路徑
pytesseract.pytesseract.tesseract_cmd = config.tesseract_path
# print(config.tesseract_path)

class Script():
    def __init__(self):
        self.f = file_operator.File()

    def activate(self):
        btn_apply_path = self.f.find_file_path(image_name=config.img_apply_balance)
        btn_reload_path = self.f.find_file_path(image_name=config.reload)

        try:

            # 獲取圖片四角坐標 網頁縮放80%
            btn_location = pyautogui.locateOnScreen(btn_apply_path, confidence=0.7)
            # print(btn_location)

            # 獲取圖片中心的坐標
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

    def screenshot(self):
        # 截圖
        redeem_box_path = self.f.find_file_path(image_name=config.for_screenshot)
        # print(config.redeem_box)
        box_location = pyautogui.locateOnScreen(redeem_box_path, confidence=0.7)
        box_center = pyautogui.center(box_location)
        pyautogui.moveTo(box_center)
        pyautogui.click()
        pyautogui.press('f1')
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.5)

        # 截圖發群
        group_icon_path = self.f.find_file_path(image_name=config.group_name)
        icon_location = pyautogui.locateOnScreen(group_icon_path, confidence=0.7)
        pyautogui.moveTo(icon_location)
        pyautogui.click()
        pyautogui.hotkey('ctrl','v')
        # pyautogui.press('enter')

    def listen_code(self):
        # 截圖並保存
        screenshot = pyautogui.screenshot()
        croped_image = screenshot.crop((1250, 580, 1500, 1000))
        croped_image.save('1.png')

        print('111',pyautogui.hotkey('ctrl','v'))

        text = pytesseract.image_to_string(screenshot,config='--psm 8')
        print(text)

        pattern = r'^[A-Z0-9]{16}$'
        # pattern =  r'^[A-Z0-9]{4}[A-Z0-9]{6}[A-Z0-9]{5}$'
        match = re.search(pattern, text)
        if match:
            print('匹配',match.group())
        else:
            print('不匹配')



    def reload(self):
        btn_reload_path = self.f.find_file_path(image_name=config.reload)
        try:

            # 獲取圖片四角坐標 網頁縮放80%
            btn_location = pyautogui.locateOnScreen(btn_reload_path, confidence=0.7)
            # print(btn_location)

            # 獲取圖片中心的坐標
            img_center_point = pyautogui.center(btn_location)
            # print(img_center_point)

            # 鼠標移動到按鈕中心
            pyautogui.moveTo(img_center_point)
            # 雙擊間隔為1秒
            pyautogui.doubleClick(duration=1)

            time.sleep(0.5)

            # 按下Enter
            pyautogui.press('enter')

        except Exception as e:
            print('Not Found!')

s = Script()
# s.reload()
# s.screenshot()
s.listen_code()