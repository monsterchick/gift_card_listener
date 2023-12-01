import os
import config


class File:
    def __init__(self):
        # 獲取 main.py 所在的目錄
        main_directory = os.path.dirname(os.path.realpath(__file__))

        # 設置工作目錄為 main.py 所在的目錄
        os.chdir(main_directory)


    def find_root_dir(self):
        '''
        :return: 返回項目根目錄
        '''
        root_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))
        # print('項目的根目錄：', root_dir)
        return root_dir

    def find_current_dir(self):
        '''
        :return: 返回當前工作目錄
        '''
        current_dir = os.getcwd()
        # print('當前工作目錄：', current_dir)
        return current_dir

    def find_file_path(self, image_name, dir_name=config.images_dir_name):
        '''
        :return: 返回文件的絕對路徑
        '''
        # 項目根目錄
        root_dir = self.find_root_dir()
        # print(root_dir)
        # print(image_name,dir_name)
        # path = os.path.join(root_dir, dir_name, image_name)
        # print('111',path)
        try:
            file_path = os.path.join(root_dir, dir_name, image_name)
            # print(file_path)
            print(os.path.join(root_dir, dir_name, image_name))

            if os.path.exists(file_path) == True:
                # print('文件或文件夾 存在')

                return file_path
            else:
                print('文件或文件夾不存在')
        except Exception as e:
            print('文件或文件夾不存在!')



# test
# f = File()
# f.find_file_path(image_name=config.img_apply_balance)
# f.find_root_dir()