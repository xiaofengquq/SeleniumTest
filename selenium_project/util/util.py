import base64
import os
import pickle
import platform
import random
import string
import time
import traceback
import urllib
from io import BytesIO
from typing import Optional
from urllib.parse import unquote

import ddddocr
import requests
import win32api
import win32con
import win32gui
import win32print
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

mapping_tables = {
    'By.ID': By.ID,
    'By.XPATH': By.XPATH,
    'By.LINK_TEXT': By.LINK_TEXT,
    'By.PARTIAL_LINK_TEXT': By.PARTIAL_LINK_TEXT,
    'By.NAME': By.NAME,
    'By.TAG_NAME': By.TAG_NAME,
    'By.CSS_SELECTOR': By.CSS_SELECTOR
}


class Util:
    global mapping_tables
    # 构建截图文件夹的完整路径，使用 os.path.join 将当前文件的父目录的父目录与 'screenshots' 目录拼接而成
    folder_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'screenshots')

    # 获取当前时间
    current_time = time.strftime('%Y年%m月%d日 %H-%M-%S')
    print(f'当前时间：{current_time}')

    # 使用当前时间生成图片文件名，格式为 年-月-日 时-分-秒.png
    picture_name = current_time + '.png'

    # 构建完整的文件路径，将截图文件夹路径与图片文件名拼接而成
    full_name = os.path.join(folder_path, picture_name)

    @staticmethod
    def get_qr_code_string(driver: webdriver, element: Optional[WebElement] = None, by: str = '', value: str = '',
                           is_not_headless: bool = True):
        if element is not None:
            captcha = element
        else:
            try:
                captcha = driver.find_element(mapping_tables[by], value)
            except:
                raise Exception('未找到元素，请检查条件')
        # 最大化页面（防止获取到的坐标不对
        driver.maximize_window()

        # 如果无头
        if is_not_headless:
            # 获取当前操作系统的缩放率
            screen_scaling = Util.get_screen_scaling()
        else:
            screen_scaling = 1

        # 截取完整屏幕截图，保存为图片文件
        driver.save_screenshot(Util.full_name)

        # 定位验证码图片元素并计算其位置和大小
        # 坐标需要乘以缩放率！！！
        top_left_x = captcha.location['x'] * screen_scaling
        top_left_y = captcha.location['y'] * screen_scaling
        width = captcha.size['width'] * screen_scaling
        height = captcha.size['height'] * screen_scaling
        # 左顶点的x加上验证码的宽，等于右底点的x
        # 左顶点的y加上验证码的高，等于右底点的y
        bottom_right_x = top_left_x + width
        bottom_right_y = top_left_y + height

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
        # 获取缩放率还有一种更简单的方法
        # driver.execute_script("return window.devicePixelRatio")

        """获取Windows缩放率"""
        if 'Windows' == platform.system():
            sX, sY = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)  # 获得屏幕分辨率X轴和Y轴
            hDC = win32gui.GetDC(0)
            x = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)  # 横向分辨率
            y = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)  # 纵向分辨率
            screen_scaling = round(y / sY, 2)  # 计算缩放比率
        else:
            screen_scaling = 1
        # print(f'当前Windows系统缩放率: {screen_scaling}')
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
        random_chars = [random.choice(characters) for _ in range(int(length))]
        # 将随机字符列表连接成字符串
        random_str = ''.join(random_chars)
        # 返回生成的随机字符串
        return random_str

    @staticmethod
    def get_random_email(length):
        """
        生成指定长度的随机邮箱，包含字母和数字

        Args:
        length (int): 生成的随机邮箱用户名的长度

        Returns:
        str: 生成的随机邮箱
        """

        # 定义包含字母和数字的字符集
        characters = string.ascii_letters + string.digits
        # 从字符集中随机选择字符，循环指定长度次数
        random_chars = [random.choice(characters) for _ in range(int(length))]
        # 将随机字符列表连接成用户名
        random_str = ''.join(random_chars)
        # 返回生成的随机邮箱
        return random_str + '@gmail.com'

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

    @staticmethod
    def login(driver, username_str: str, password_str: str, is_captcha_present: bool):
        # .form-group 和 input[placeholder="请输入验证码"]是后代关系，所以用空格可以找到
        # .form-control 和 input[placeholder="请输入验证码"]是交集关系，所以连写可以找到
        # captcha_input_box_info = (By.CSS_SELECTOR, '.form-group input[placeholder="请输入验证码"]')

        # 定义验证码输入框、验证码图片和提交按钮的选择器
        captcha_input_box_info = (By.CSS_SELECTOR, 'input[placeholder="请输入验证码"].form-control')
        captcha_image_info = (By.CSS_SELECTOR, 'img[src="/jpress/commons/captcha"]')
        submit_button_info = (By.CSS_SELECTOR, '.btn.btn-primary.btn-block.btn-flat')
        # 如果页面中有验证码
        if is_captcha_present:
            try:
                # 找到验证码输入框并输入验证码
                captcha_input_box = driver.find_element(*captcha_input_box_info)
                captcha_image = driver.find_element(*captcha_image_info)
                captcha_input_box.send_keys(Util.get_qr_code_string(driver, captcha_image))

                # 输入用户名和密码
                driver.find_element(By.NAME, 'user').send_keys(username_str)
                driver.find_element(By.NAME, 'pwd').send_keys(password_str)

                # 点击提交按钮
                submit_button = driver.find_element(*submit_button_info)
                submit_button.click()
                time.sleep(1)

                # 如果ddddocr识别有误，再重试一次
                try:
                    alert = driver.switch_to.alert
                    if alert.text == '验证码不正确，请重新输入':
                        alert.accept()
                        captcha_input_box.clear()
                    captcha_image.click()
                    captcha_input_box.send_keys(Util.get_qr_code_string(driver, captcha_image))
                    submit_button.click()
                except:
                    print('验证码无误')
            except:
                # 如果出现异常，打印堆栈跟踪
                traceback.print_exc()
        else:
            try:
                # 如果没有验证码，直接输入用户名和密码并提交
                driver.find_element(By.NAME, 'user').send_keys(username_str)
                driver.find_element(By.NAME, 'pwd').send_keys(password_str)
                driver.find_element(*submit_button_info).click()
            except:
                # 如果出现异常，打印堆栈跟踪
                traceback.print_exc()


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options)
    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8080/jpress/user/register')
    captcha = driver.find_element(By.CSS_SELECTOR, 'img')
    # Util.get_qr_code_string(driver, captcha, is_not_headless=False)
    print(f'location: {captcha.location}')
    print(f'size: {captcha.size}')
