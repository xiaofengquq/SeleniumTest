import os
import pickle
import platform
import random
import string
import time
from io import BytesIO

import ddddocr
import win32api
import win32con
import win32gui
import win32print
from PIL import Image


class Util:
    # 构建截图文件夹的完整路径，使用 os.path.join 将当前文件的父目录的父目录与 'screenshots' 目录拼接而成
    folder_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'screenshots')

    # 使用当前时间生成图片文件名，格式为 年-月-日 时-分-秒.png
    picture_name = time.strftime('%Y年%m月%d日 %H-%M-%S') + '.png'

    # 构建完整的文件路径，将截图文件夹路径与图片文件名拼接而成
    full_name = os.path.join(folder_path, picture_name)

    @staticmethod
    def take_qr_code_string(driver, id_string):
        # 最大化页面（防止获取到的坐标不对
        driver.maximize_window()

        # 获取当前操作系统的缩放率
        screen_scaling = Util.get_screen_scaling()

        # 定位验证码图片元素并计算其位置和大小
        captcha = driver.find_element(value=id_string)

        # 坐标需要乘以缩放率！！！

        top_left_x = captcha.location['x'] * screen_scaling
        top_left_y = captcha.location['y'] * screen_scaling
        width = captcha.size['width'] * screen_scaling
        height = captcha.size['height'] * screen_scaling
        # 左顶点的x加上验证码的宽，等于右底点的x
        # 左顶点的y加上验证码的高，等于右底点的y
        bottom_right_x = top_left_x + width
        bottom_right_y = top_left_y + height

        # 截取完整屏幕截图，保存为图片文件
        driver.save_screenshot(Util.full_name)

        # 保存矩形参数的元组
        # 定义一个矩形区域，左上角坐标为 (top_left_x, top_left_y)，右下角坐标为 (bottom_right_x, bottom_right_y)
        rectangle = (top_left_x, top_left_y, bottom_right_x, bottom_right_y)

        # 使用 PIL 库的 Image.open 方法打开名为 Util.full_name 的图像，并对其进行裁剪
        image = Image.open(Util.full_name).crop(rectangle)

        # 创建一个 BytesIO 对象，用于存储图像的二进制数据
        bytesIO = BytesIO()

        # 将裁剪好的验证码流保存到 BytesIO 对象中
        image.save(bytesIO, format='PNG')

        # 返回验证码文本
        return Util.captcha_to_string(bytesIO.getvalue())

    @staticmethod
    def get_screen_scaling():
        """获取Windows缩放率"""
        if 'Windows' == platform.system():
            sX, sY = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)  # 获得屏幕分辨率X轴和Y轴
            hDC = win32gui.GetDC(0)
            x = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)  # 横向分辨率
            y = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)  # 纵向分辨率
            screen_scaling = round(y / sY, 2)  # 计算缩放比率
        else:
            screen_scaling = 1
        print(f'当前Windows系统缩放率: {screen_scaling}')
        return screen_scaling  # 返回屏幕缩放比率

    @staticmethod
    def captcha_to_string(image_byte):
        ocr = ddddocr.DdddOcr()  # 初始化 OCR 工具
        identify_result = ocr.classification(image_byte)  # 使用 OCR 工具识别图片内容
        print(f'ocr识别验证码结果: {identify_result}')  # 打印识别结果
        return identify_result  # 返回信息

    @staticmethod
    def get_random_str(length):
        """
        生成指定长度的随机字符串，包含字母和数字

        Args:
        length (int): 生成的随机字符串的长度

        Returns:
        str: 生成的随机字符串
        """

        # 定义包含字母和数字的字符集
        characters = string.ascii_letters + string.digits
        # 从字符集中随机选择字符，循环指定长度次数
        random_chars = [random.choice(characters) for _ in range(length)]
        # 将随机字符列表连接成字符串
        random_str = ''.join(random_chars)
        # 返回生成的随机字符串
        return random_str

    @staticmethod
    def save_cookie(driver, path):
        """
        保存浏览器的 cookies 到指定文件

        Args:
        driver: 浏览器驱动对象
        path (str): 要保存 cookies 的文件路径

        Returns:
        None
        """

        # 获取浏览器的 cookies
        cookies = driver.get_cookies()
        # 打印 cookies
        print(f'cookies: {cookies}')
        # 使用 'with' 语句打开文件，以二进制写入模式
        with open(path, 'wb') as f:
            # 使用 pickle.dump 将 cookies 对象保存到文件中
            pickle.dump(cookies, f)

    @staticmethod
    def load_cookies(path):
        """
        从指定文件中加载 cookies 对象

        Args:
        path (str): 包含 cookies 对象的文件路径

        Returns:
        object: 从文件中加载的 cookies 对象
        """
        # 以二进制读取模式打开文件
        with open(path, 'rb') as file_handle:
            # 使用 pickle.load 从文件中加载 cookies 对象
            cookies = pickle.load(file_handle)
        # 返回加载的 cookies 对象
        return cookies


if __name__ == '__main__':
    picture_name = time.strftime('%Y年%m月%d日 %H-%M-%S') + '.png'  # 存储完整屏幕截图的文件名
    print(picture_name)
