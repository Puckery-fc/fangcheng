'''
Created on 2018年4月18日

@author: Administrator
'''
from selenium import webdriver
base = webdriver.Chrome()
base.get("http://150.138.118.94:9080/wmc/")
base.find_element_by_id("ACCOUNT").send_keys("liuyong")
base.find_element_by_id("PASSWORD").send_keys("123456")
base.find_element_by_id("COMPANY").send_keys("zyhxkl")
base.find_element_by_css_selector("[type~='submit']").click()