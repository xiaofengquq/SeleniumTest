import os.path  # 导入os.path模块
from time import sleep  # 导入sleep函数

import ddddocr  # 导入ddddocr模块
from PIL import Image  # 导入Image类
from selenium import webdriver  # 导入webdriver模块
from selenium.webdriver.common.by import By  # 导入By类


class HandleComplexCaptcha:
    picture_name1 = 'screenshot.png'  # 存储完整屏幕截图的文件名
    picture_name2 = '验证码.png'  # 存储验证码部分截图的文件名

    @classmethod
    def take_qr_code_and_login(cls):
        # 启动 Chrome 浏览器并访问登录页面
        driver = webdriver.Chrome()
        driver.get('http://localhost:8080/jpress/user/login')
        driver.maximize_window()

        # 定位验证码图片元素并计算其位置和大小
        captcha = driver.find_element(value='captcha-img')
        top_left_x = captcha.location['x']
        top_left_y = captcha.location['y']
        width = captcha.size['width']
        height = captcha.size['height']
        bottom_right_x = top_left_x + width
        bottom_right_y = top_left_y + height

        # 截取完整屏幕截图并裁剪出验证码部分，保存为图片文件
        driver.save_screenshot(cls.picture_name1)

        # 保存矩形参数的元组
        rectangle = (top_left_x, top_left_y, bottom_right_x, bottom_right_y)
        image = Image.open(cls.picture_name1).crop(rectangle)
        image.save(cls.picture_name2)

        captcha_string = cls.captcha_to_string()  # 获取验证码识别结果
        user = driver.find_element(By.NAME, 'user')  # 定位用户名输入框
        user.send_keys('admin')  # 输入用户名
        password = driver.find_element(By.NAME, 'pwd')  # 定位密码输入框
        password.send_keys('915366')  # 输入密码
        captcha = driver.find_element(By.NAME, 'captcha')  # 定位验证码输入框
        captcha.send_keys(captcha_string)  # 输入验证码
        sleep(3)
        login_button = driver.find_element(By.XPATH,
                                           '/html/body/div/div[2]/div/div[2]/div/form/div[4]/div/button')  # 定位登录按钮
        login_button.click()  # 点击登录按钮
        sleep(3)

    @staticmethod
    def captcha_to_string():
        current_path = os.path.abspath(__file__)  # 获取当前文件的绝对路径
        dir_path = os.path.dirname(current_path)  # 获取当前文件所在目录的路径
        captcha_path = os.path.join(dir_path, HandleComplexCaptcha.picture_name2)  # 拼接验证码图片的完整路径
        ocr = ddddocr.DdddOcr()  # 初始化 OCR 工具
        with open(f'{captcha_path}', 'rb') as f:  # 以二进制模式打开验证码图片文件
            img_bytes = f.read()  # 读取图片文件的字节内容
        res = ocr.classification(img_bytes)  # 使用 OCR 工具识别图片内容
        print(res)  # 打印识别结果
        return res  # 返回信息


if __name__ == '__main__':
    HandleComplexCaptcha.take_qr_code_and_login()  # 执行验证码识别和登录操作
