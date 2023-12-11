from time import *

from PIL import Image
from selenium import webdriver


def test():
    driver = webdriver.Chrome()
    driver.get('http://localhost:8080/jpress/user/login')
    driver.maximize_window()

    picture_name1 = strftime('%Y年%m月%d日 %H：%M：%S', localtime(time())) + '.png'
    captcha = driver.find_element(value='captcha-img')
    top_left_x = captcha.location['x']
    top_left_y = captcha.location['y']
    width = captcha.size['width']
    height = captcha.size['height']
    bottom_right_x = top_left_x + width
    bottom_right_y = top_left_y + height
    driver.save_screenshot(picture_name1)
    rectangle = (top_left_x, top_left_y, bottom_right_x, bottom_right_y)
    image = Image.open(picture_name1).crop(rectangle)
    picture_name2 = strftime('验证码.png')
    image.save(picture_name2)


if __name__ == '__main__':
    test()
