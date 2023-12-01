# 進行文字識別
txt_apply = pytesseract.image_to_string(image_path)
print(txt_apply)

# 截圖
screenshot = pyautogui.screenshot()

# 獲取當前時間
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
# print(current_datetime)

# 要保存的文件路徑
file_name = current_datetime + '.png'
record_location = os.path.join(self.f.find_root_dir(), config.trans_record_name, file_name)
# print(record_location)

screenshot.save(fp=record_location)