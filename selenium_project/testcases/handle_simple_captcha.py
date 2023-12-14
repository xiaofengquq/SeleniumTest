from selenium import webdriver
from time import sleep
from PIL import Image
import pytesseract


class HandleSimpleCaptcha:
    picture_name1 = 'screenshot.png'  # 存储完整屏幕截图的文件名
    picture_name2 = '验证码.png'  # 存储验证码部分截图的文件名

    @classmethod
    def take_qr_code(cls):
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
        rectangle = (top_left_x, top_left_y, bottom_right_x, bottom_right_y)
        image = Image.open(cls.picture_name1).crop(rectangle)
        image.save(cls.picture_name2)
        driver.quit()
        sleep(3)

    @staticmethod
    def qr_code_to_string():
        # 从图片文件中提取验证码文字并打印
        # pytesseract.image_to_string只能处理简单验证码，复杂验证码无法解析
        image = Image.open(HandleSimpleCaptcha.picture_name2)
        string = pytesseract.image_to_string(image)
        print(string)


if __name__ == '__main__':
    # 获取验证码图片
    HandleSimpleCaptcha.take_qr_code()
    # 提取文字
    HandleSimpleCaptcha.qr_code_to_string()
