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

    # Web page Browser Title 확인
    def test_check_title(self):
        driver = self.driver
        self.driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            # Web page Browser Title 출력 확인
            self.assertEqual("CloudPlex Media", driver.title)
        except:
            print('TEST FAIL : check_title')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Screenshots/test_Title-%s.png' % now)
        else:
            print('TEST PASS : check_title')

    # Brand Logo 확인
    def test_check_logo(self):
        driver = self.driver
        self.driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            # Brand Logo 출력 확인
            self.driver.find_element_by_class_name("brand-logo")
        except:
            print('TEST FAIL : check_logo')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Screenshots/test_Title-%s.png' % now)
        else:
            print('TEST PASS : check_logo')

    # Welcome Text 확인
    def test_check_welcome(self):
        driver = self.driver
        self.driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            # Welcome Text 출력 확인
            self.assertEqual("Welcome!", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='You need to sign in a Megazone Accounts account to get started.'])[1]/preceding::h4[1]").text)
        except:
            print('TEST FAIL : check_welcome')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Screenshots/test_Welcome-%s.png' % now)
        else:
            print('TEST PASS : check_welcome')

    # Sign in Button 출력 및 이동 확인
    def test_check_btn_signIn(self):
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            # [Sign in]버튼 확인
            self.assertEqual("Sign in with Megazone Accounts",
                             driver.find_element_by_link_text("Sign in with Megazone Accounts").text)
            # [Sign in]버튼 클릭
            self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div[2]/form/div[1]/a').click()
            # ID 입력
            self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('mcmtestowner@gmail.com')
            # [다음]버튼 클릭
            self.driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div/div/div[2]/div[4]/button').click()
            time.sleep(3)
            # PW 입력
            self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('Megazone1!')
            # [로그인]버튼 클릭
            self.driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='로그인'])[1]/following::strong[1]").click()
            # 로그인되었는지 확인 (Stage / Project / Name / Email)
            time.sleep(3)
            self.assertEqual("Megazone (Owner)", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='mcmtestowner@gmail.com'])[1]/preceding::em[1]").text)
            self.assertEqual("mcmtestowner@gmail.com", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Megazone (Owner)'])[1]/following::small[1]").text)
            self.assertEqual("CloudPlex Media", driver.title)
            self.assertEqual("Hi, Megazone (Owner)", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='mcmtestowner@gmail.com'])[1]/following::h1[1]").text)
        except:
            print('TEST FAIL : check_btn_signIn')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Screenshots/test_Sign-%s.png' % now)
        else:
            print('TEST PASS : check_btn_signIn')

    # Create Account Link 확인
    def test_check_link_createAccount(self):
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            # [Create Account]버튼 확인
            self.assertEqual("Create account", driver.find_element_by_link_text("Create account").text)
            # [Create Account]버튼 클릭
            self.driver.find_element_by_link_text("Create account").click()
            # 이동한 페이지 확인 (Title)
            # 이슈있어 확인불가
        except:
            print('TEST FAIL : check_link_createAccount')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Screenshots/test_CreateAccount-%s.png' % now)
        else:
            print('TEST PASS : check_link_createAccount')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Welcome('test_check_title'))
    suite.addTest(Welcome('test_check_logo'))
    suite.addTest(Welcome('test_check_welcome'))
    suite.addTest(Welcome('test_check_btn_signIn'))
    suite.addTest(Welcome('test_check_link_createAccount'))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Reports")
    runner.run(suite())