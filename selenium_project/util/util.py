import platform
from io import BytesIO

import ddddocr
import win32api
import win32con
import win32gui
import win32print
from PIL import Image


class Util:
    picture_name = 'screenshot.png'  # 存储完整屏幕截图的文件名

    @staticmethod
    def take_qr_code(driver):
        # 启动 Chrome 浏览器并访问登录页面
        driver.get('http://localhost:8080/jpress/user/login')
        driver.maximize_window()

        # 获取当前操作系统的缩放率
        screen_scaling = Util.get_screen_scaling()
        print(screen_scaling)

        # 定位验证码图片元素并计算其位置和大小
        captcha = driver.find_element(value='captcha-img')
        top_left_x = captcha.location['x'] * screen_scaling  # 坐标需要乘以缩放率
        top_left_y = captcha.location['y'] * screen_scaling
        width = captcha.size['width'] * screen_scaling
        height = captcha.size['height'] * screen_scaling
        bottom_right_x = top_left_x + width
        bottom_right_y = top_left_y + height

        # 截取完整屏幕截图并裁剪出验证码部分，保存为图片文件
        driver.save_screenshot(Util.picture_name)

        # 保存矩形参数的元组
        # 定义一个矩形区域，左上角坐标为 (top_left_x, top_left_y)，右下角坐标为 (bottom_right_x, bottom_right_y)
        rectangle = (top_left_x, top_left_y, bottom_right_x, bottom_right_y)

        # 使用 PIL 库的 Image.open 方法打开名为 driver.picture_name 的图像，并对其进行裁剪
        image = Image.open(Util.picture_name).crop(rectangle)

        # 创建一个 BytesIO 对象，用于存储图像的二进制数据
        bytesIO = BytesIO()

        # 将裁剪后的图像保存到 BytesIO 对象中
        image.save(bytesIO, format='PNG')

        # 返回存储了图像二进制数据的 BytesIO 数据流
        return bytesIO.getvalue()

    @staticmethod
    def get_screen_scaling():
        """获取Windows缩放率"""
        if 'Windows' == platform.system():
            sX, sY = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)  # 获得屏幕分辨率X轴和Y轴
            hDC = win32gui.GetDC(0)
            x = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)  # 横向分辨率
            y = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)  # 纵向分辨率
            screen_scale_rate = round(y / sY, 2)  # 计算缩放比率
        else:
            screen_scale_rate = 1
        return screen_scale_rate  # 返回屏幕缩放比率

    @staticmethod
    def captcha_to_string(image_byte):
        ocr = ddddocr.DdddOcr()  # 初始化 OCR 工具
        identify_result = ocr.classification(image_byte)  # 使用 OCR 工具识别图片内容
        print(identify_result)  # 打印识别结果
        return identify_result  # 返回信息
