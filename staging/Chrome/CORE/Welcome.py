# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common


class Welcome(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    # Web page Title 확인
    def test_checkBrowserTitle(self):
        driver = self.driver
        self.driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            self.assertEqual("CloudPlex Media", driver.title)
        except:
            print('TEST FAIL : checkBrowserTitle')
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Screenshots/test_Title-%s.png' % now)
        else:
            print('TEST PASS : checkBrowserTitle')

    # Logo 확인
    def test_checkBrandLogo(self):
        driver = self.driver
        self.driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            self.driver.find_element_by_class_name("brand-logo")
        except:
            print('TEST FAIL : checkBrandLogo')
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Screenshots/test_Title-%s.png' % now)
        else:
            print('TEST PASS : checkBrandLogo')

    # Welcome Text 확인
    def test_checkTxtWelcome(self):
        driver = self.driver
        self.driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            self.assertEqual("Welcome!", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='You need to sign in a Megazone Accounts account to get started.'])[1]/preceding::h4[1]").text)
        except:
            print('TEST FAIL : Welcome!')
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Screenshots/test_Welcome-%s.png' % now)
        else:
            print('TEST PASS : Welcome!')

    # Sign in Button 확인
    def test_checkBtnSign(self):
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            self.assertEqual("Sign in with Megazone Accounts",
                             driver.find_element_by_link_text("Sign in with Megazone Accounts").text)
        except:
            print('TEST FAIL : Sign in with Megazone Accounts')
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Screenshots/test_Sign-%s.png' % now)
        else:
            print('TEST PASS : Sign in with Megazone Accounts')

    # Create Account Link 확인
    def test_checkLinkCreateAccount(self):
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            self.assertEqual("Create account", driver.find_element_by_link_text("Create account").text)
        except:
            print('TEST FAIL : Create account')
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Screenshots/test_CreateAccount-%s.png' % now)
        else:
            print('TEST PASS : Create account')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Welcome('test_checkBrowserTitle'))
    suite.addTest(Welcome('test_checkBrandLogo'))
    suite.addTest(Welcome('test_checkTxtWelcome'))
    suite.addTest(Welcome('test_checkBtnSign'))
    suite.addTest(Welcome('test_checkLinkCreateAccount'))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Reports")
    runner.run(suite())