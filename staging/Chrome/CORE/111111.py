# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common


class Gnb(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        # self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        # self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        # self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_channel_stop(self):  # Service Logo 출력 및 링크 이동 확인
        driver = self.driver
        driver.get("https://console.media.stg.continuum.co.kr/welcome")
           # self.assertEqual("Welcome!", driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div[2]/h4').text)

        #if driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div[2]/h4').text) == "Welcome!":
        if driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div[2]/h4').text == "Welcome!":
        #if "Welcome!" == "Welcome!":
            print("성공")
        else:
            print("실패")
        '''
        try:
            print(type(driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div[2]/h4').text))
            print(driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div[2]/h4').text)
        except:
            print('TEST FAIL : 실패당')
        else:
            print('TEST PASS : 성공이당')
            '''
def tearDown(self):
    self.driver.close()
    self.driver.quit()
    print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Gnb('test_channel_stop'))

    return suite


if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())