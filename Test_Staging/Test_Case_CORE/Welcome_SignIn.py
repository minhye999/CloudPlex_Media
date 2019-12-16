# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import HtmlTestRunner
import sys
import logging
import time
from datetime import datetime
import Test_Staging.Common

class Welcome_SignIn(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    # [Sign in with Megazone Accounts] Button Click > 이동한 page에서 input ID > [다음] Button Click > input PASSWORD > [Log In] Button Click
    def test_signIn(self):
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div[2]/form/div[1]/a').click()
            self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('mcmtestowner@gmail.com')
            self.driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div/div/div[2]/div[4]/button').click()
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('Megazone1!')
            self.driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='로그인'])[1]/following::strong[1]").click()
            time.sleep(3)
        except:
            print('TEST FAIL : signIn')
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('F:/PyCharm/Project/CloudPlex_Media/Test_Staging/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : signIn')

    # [Sign in with Megazone Accounts] Button Click > 이동한 page에서 input ID > [다음] Button Click > input PASSWORD > [Log In] Button Click
    def test_signInAfter(self):
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            self.assertEqual("Megazone (Owner)", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='mcmtestowner@gmail.com'])[1]/preceding::em[1]").text)
            self.assertEqual("mcmtestowner@gmail.com", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Megazone (Owner)'])[1]/following::small[1]").text)
            self.assertEqual("CloudPlex Media", driver.title)
            self.assertEqual("Hi, Megazone (Owner)", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='mcmtestowner@gmail.com'])[1]/following::h1[1]").text)
        except:
            print('TEST FAIL : signInAfter')
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('F:/PyCharm/Project/CloudPlex_Media/Test_Staging/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : signInAfter')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Welcome_SignIn('test_signIn'))
    suite.addTest(Welcome_SignIn('test_signInAfter'))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="F:/PyCharm/Project/CloudPlex_Media/Test_Staging/Test_Results/Reports")
    runner.run(suite())