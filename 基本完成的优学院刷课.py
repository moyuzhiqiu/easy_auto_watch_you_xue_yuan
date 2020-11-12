from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import pyautogui
import time
#优学院尝试
address1 = "https://www.baidu.com/link?url=U-9gG0GWkQ1KZ-aIqUUcYmPG7bMUu6DD4RzpxkNRtWf11LF5997TYiM6deA4PlfB&wd=&eqid=83a1ac9500002212000000055fabbdf9"

username = ""#账号
password = ""#密码

browser = webdriver.Chrome()#创建Chrome浏览器对象，在打开一个浏览器窗口
browser.get(address1)#通过浏览器向服务器发送URL请求

time.sleep(5)#这个网页加载多次，until无效，一次不能全部加载，需要强制等5s,校园网拉跨。

#wait = WebDriverWait(browser,30,0.5)

browser.find_element_by_class_name("login-btn-text").click()#打开登录界面
time.sleep(5)#我吐了这里也一样
browser.find_element_by_id("userLoginName").send_keys(username)#账号
browser.find_element_by_id("userPassword").send_keys(password)#密码
browser.find_element_by_css_selector("#loginForm > button").click()#登录

time.sleep(5)
browser.find_element_by_id("courseCard67117").click()#打开形式与政策
time.sleep(5)

pyautogui.moveTo(x=119, y=390)#打开课件
pyautogui.click()#定位不到直接点

time.sleep(5)

pyautogui.moveTo(x=846, y=769)#专题7，可改
pyautogui.click()
#手动，提前写好所有题目

time.sleep(10)#加载多次时间较长。

for i in range(0,30):
    pyautogui.moveTo(x=479, y=592)
    pyautogui.click()
    time.sleep(600)#时间设计
    pyautogui.moveTo(x=828, y=990)
    pyautogui.click()#看10分钟点下一个，可优化



#雅尔课堂尝试 解决不了答题问题
#browser.find_eleme  nt_by_id("phone").send_keys("")#账号密码
#browser.find_element_by_id("pwd").send_keys("")



#browser.find_element_by_id("phoneLoginBtn").click()#登录

#time.sleep(3)
#first_windows = browser.current_window_handle
#browser.refresh()

#browser.get("https://mooc1-1.chaoxing.com/visit/stucoursemiddle?courseid=210613687&clazzid=33473943&vc=1&cpi=157130123")


#出现新窗口，切换

#all_windows = browser.window_handles
#for handle in all_windows:
   # if handle != first_windows:
       # browser.switch_to.window(handle)
       # print("跳转")
#time.sleep(1)
#browser.refresh()
#browser.get(address2)#进入第二个
#browser.find_element_by_css_selector("#video > div.vjs-poster")#播放

#time.sleep(30)#等待登录
#刷新浏览器
#browser.refresh()
#设置浏览器的大小
#browser.set_window_size(1400,800)


#element1 = browser.find_element_by_css_selector("#video > button > span.vjs-icon-placeholder")#播放按钮
#element1.click()#开始播放
#element2 = browser.find_element_by_css_selector("#userLoginName")#用户名
#element2.click()