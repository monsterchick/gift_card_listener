import os
import pytesseract  # 文字識別
import config
from module import file_operator
import pyautogui  # 鼠標鍵盤控制





def redeem_card(image_path):
    '''
    :param image_path: 圖片的絕對路徑
    :return: 激活卡操作
    '''

    # 點擊 “Apply to your balance” 按鈕



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



