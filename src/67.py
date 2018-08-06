'''
Created on 2018年6月7日

@author: Administrator
'''
from selenium import webdriver
import time
#import unittest
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("知乎")
driver.find_element_by_id("su").click()
time.sleep(3)
'''
handle = driver.current_window_handle
print(handle)
    '''
driver.find_element_by_class_name("favurl").click()
'''
all_handle = driver.window_handles
print(all_handle)
'''
windows = driver.window_handles
driver.switch_to_window(windows[-1])
time.sleep(3)

time.sleep(5)
driver.find_element_by_xpath("//*[@id='root']/div/main/div/div[2]/div/div/div/div[1]/div/div[1]/div[2]/button[1]").click()
driver.find_element_by_name("username").send_keys("15088558058")
time.sleep(3)
driver.find_element_by_name("password").send_keys("fc678268")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[4]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/button").click()
