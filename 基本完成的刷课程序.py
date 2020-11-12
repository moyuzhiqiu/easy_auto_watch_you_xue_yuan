from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import pyautogui
import time
from ctypes import *

#没有解决章节跳转会少看一章的问题，懒的解决了

pyautogui.FAILSAFE = True#保护措施，避免失控
pyautogui.PAUSE = 0.1 #为所有的PyAutoGUI函数增加延迟。默认延迟时间是0.1秒。
def get_color(x, y):
    gdi32 = windll.gdi32
    user32 = windll.user32
    hdc = user32.GetDC(None)  # 获取颜色值
    pixel = gdi32.GetPixel(hdc, x, y)  # 提取RGB值
    r = pixel & 0x0000ff
    g = (pixel & 0x00ff00) >> 8
    b = pixel >> 16
    return [r, g, b]

#优学院尝试
address1 = "https://www.baidu.com/link?url=U-9gG0GWkQ1KZ-aIqUUcYmPG7bMUu6DD4RzpxkNRtWf11LF5997TYiM6deA4PlfB&wd=&eqid=83a1ac9500002212000000055fabbdf9"
kejianposition = [251,391]
zhuanti1 =[1219,456]
weiwanchencolor = [234, 89, 71]
weiwanchenposition = [648,701]
weiwanchenexitposition = [824,705]

zuoticolor = [249, 131, 112]
zuotiposition = [501,242]

xiayiyeposition = [1350,966]
bofang = [927,588]

xiayizhangcolor = [234, 89, 71]

username = ""#账号
password = ""#密码

browser = webdriver.Chrome()#创建Chrome浏览器对象，在打开一个浏览器窗口
browser.get(address1)#通过浏览器向服务器发送URL请求
browser.set_window_size(1500,1000)

time.sleep(5)#这个网页加载多次，until无效，一次不能全部加载，需要强制等5s,校园网拉跨。

#wait = WebDriverWait(browser,30,0.5)

browser.find_element_by_class_name("login-btn-text").click()#打开登录界面
time.sleep(2)#我吐了这里也一样
browser.find_element_by_id("userLoginName").send_keys(username)#账号
browser.find_element_by_id("userPassword").send_keys(password)#密码
browser.find_element_by_css_selector("#loginForm > button").click()#登录

time.sleep(5)
browser.find_element_by_id("courseCard67117").click()#打开形式与政策
time.sleep(3)

pyautogui.moveTo(kejianposition[0],kejianposition[1])#打开课件
pyautogui.click()#定位不到直接点

time.sleep(5)

pyautogui.moveTo(zhuanti1[0],zhuanti1[1])#专题1，可改
pyautogui.click()
#手动，提前写好所有题目

time.sleep(10)#加载多次时间较长。
pyautogui.moveTo(bofang[0],bofang[1])
pyautogui.click()

for i in range(0,30):
    time.sleep(5)
    pyautogui.moveTo(xiayiyeposition[0],xiayiyeposition[1])
    pyautogui.click()

    lingshicolor = get_color(zuotiposition[0],zuotiposition[1])
#这里没有解决章节跳转会少看一章的问题
    pyautogui.moveTo(bofang[0], bofang[1])
    pyautogui.click()
    pyautogui.click()





