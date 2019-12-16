# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import HtmlTestRunner
import sys
import logging
import time
from datetime import datetime
import Test_Staging.Common

class FNB(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_checkLinkTerms(self):  # Terms & Conditions 링크 확인 및 이동
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            Test_Staging.Common.moveMainPage(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Terms & Conditions 링크 출력 확인
            self.assertEqual("Terms & Conditions", driver.find_element_by_link_text("Terms & Conditions").text)
            # Terms & Conditions 링크 클릭
            driver.find_element_by_link_text("Terms & Conditions").click()
            time.sleep(3)
            # Terms & Conditions 페이지 이동 (새창) http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/policy
            #
        except:
            print('TEST FAIL : checkLinkTerms')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                'F:/PyCharm/Project/CloudPlex_Media/Test_Staging/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkLinkTerms')

    def test_checkCopyright(self):  # Copyright 확인 및 Megazone Corp 이동
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            Test_Staging.Common.moveMainPage(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Copyright 출력 확인
            self.assertEqual(u"Copyright © 2019. Megazone Corp. All rights reserved.", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Terms & Conditions'])[1]/following::span[1]").text)
            # Megazone Corp. 링크 확인
            self.assertEqual("Megazone Corp.", driver.find_element_by_link_text("Megazone Corp.").text)
            # Megazone Corp. 링크 클릭
            driver.find_element_by_link_text("Megazone Corp.").click()
            time.sleep(3)
            # Megazone Corp.으로 페이지 이동 (새창) https://www.mz.co.kr/
            #
        except:
            print('TEST FAIL : checkCopyright')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                'F:/PyCharm/Project/CloudPlex_Media/Test_Staging/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkCopyright')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(FNB('test_checkLinkTerms'))
    suite.addTest(FNB("test_checkCopyright"))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="F:/PyCharm/Project/CloudPlex_Media/Test_Staging/Test_Results/Reports")
    runner.run(suite())