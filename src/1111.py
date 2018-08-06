'''
Created on 2018年7月2日

@author: Administrator
'''
from selenium import webdriver
import unittest,time


class souhutest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.sohu.com/"
    
    def test_souhu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        time.sleep(6)
        driver.find_element_by_link_text("登录狐友").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/ul/li[1]").click()
        time.sleep(2)
        driver.find_element_by_class_name("user-input").send_keys("15088558058")
        time.sleep(2)
        driver.find_element_by_class_name("password-input").send_keys("fc678268")
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div[2]/input").click()

    def close_alert_and_get_its_test(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text()
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
                return alert_text
        finally:self.accept_next_alert = True
        

    def tearDown(self):
        self.driver.quit()

if __name__ == '_main_':

        unittest.main()
      
       
   
        
        
        
        
    
    