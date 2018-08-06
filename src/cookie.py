'''
Created on 2018年3月8日

@author: Administrator
'''
#get_cookies() 获得所有 cookie 信息
#get_cookie(name) 返回特定 name 有 cookie 信息
#add_cookie(cookie_dict) 添加 cookie，必须有 name 和 value 值
#delete_cookie(name) 删除特定(部分)的 cookie 信息
#delete_all_cookies() 删除所有 cookie 信息


from selenium import  webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.gov.cn/")
'''
#获取cookie 信息
cookie = driver.get_cookies()

#将获取的cookie信息打印

print(cookie)

'''
#向cookie的name和value 添加会话信息
driver.add_cookie({"name":"key-aaa","value":"walue-bbb"})

#遍历cookies中的name和value信息打印，且 有上面添加的信息
