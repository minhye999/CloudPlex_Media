# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner

class Welcome(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        # self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        # self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        # self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    # Welcome Page 출력문구 확인
    def test_welcome_ui(self):
        driver = self.driver
        self.driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            # Web page Browser Title 출력 확인
            self.assertEqual("CloudPlex Media", driver.title)
            # Brand Logo 출력 확인
            self.driver.find_element_by_class_name("brand-logo")
            # Welcome Text 출력 확인
            self.assertEqual("Welcome!", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='You need to sign in a Megazone Accounts account to get started.'])[1]/preceding::h4[1]").text)
            # [Sign in]버튼 출력 확인
            self.assertEqual("Sign in with Megazone Accounts",
                             driver.find_element_by_link_text("Sign in with Megazone Accounts").text)
            # [Create Account]버튼 출력 확인
            self.assertEqual("Create account", driver.find_element_by_link_text("Create account").text)
        except:
            print('TEST FAIL : test_welcome_ui')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('../../../staging/V2/Test_Results/Screenshots/test_welcome_ui-%s.png' % now)
        else:
            print('TEST PASS : test_welcome_ui')

    # Sign in 기능 확인
    def test_signIn(self):
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            # [Sign in]버튼 클릭
            self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div[2]/form/div[1]/a').click()
            # ID 입력
            self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('media.qa.001@gmail.com')
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
            self.assertEqual("메가존", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='media.qa.001@gmail.com'])[1]/preceding::em[1]").text)
            self.assertEqual("media.qa.001@gmail.com", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='메가존'])[1]/following::small[1]").text)
            self.assertEqual("CloudPlex Media", driver.title)
            # self.assertEqual("Hi, 메가존", driver.find_element_by_xpath(
            #    "(.//*[normalize-space(text()) and normalize-space(.)='mcmtestowner@gmail.com'])[1]/following::h1[1]").text)
        except:
            print('TEST FAIL : test_signIn')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_signIn-%s.png' % now)
        else:
            print('TEST PASS : test_signIn')

    # Create Account Link 확인
    def test_createAccount(self):
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            # [Create Account]버튼 클릭
            self.driver.find_element_by_link_text("Create account").click()
            # 이동한 페이지 확인 (새창 이동 : Title)
            driver.switch_to.window(driver.window_handles[-1])  # 최근 열린 탭으로 전환 (새로 열린 탭으로 활성 탭 변경)
            time.sleep(3)  # 로딩 기다리기
            self.assertEqual(u"계정 만들기", driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='이메일'])[1]/preceding::h2[1]").text)
        except:
            print('TEST FAIL : test_createAccount')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_createAccount-%s.png' % now)
        else:
            print('TEST PASS : test_createAccount')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")


def suite():
    suite = unittest.TestSuite()
    suite.addTest(Welcome('test_welcome_ui'))
    suite.addTest(Welcome('test_signIn'))
    suite.addTest(Welcome('test_createAccount'))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())