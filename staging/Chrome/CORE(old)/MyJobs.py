# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class MyJobs(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_check_myJobs(self):  # My Jobs 버튼 출력 및 이동 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [My Jobs]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Download Apps'])[1]/following::a[1]").click()
            # My Jobs 패널에서 Status 라벨(Complete) 확인
            self.assertEqual("COMPLETE", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='My Jobs'])[1]/following::span[2]").text)
            # Job ID 확인
            driver.find_element_by_link_text(
                "//div[@id='right-sidebar']/div/div/div/div/div[1]/div/div[1]/div/a")
            # Job ID 클릭
            driver.find_element_by_link_text(
                "//div[@id='right-sidebar']/div/div/div/div/div[1]/div/div[1]/div/a").click()
            # File Name 확인
            driver.find_element_by_xpath(
                "//div[@id='right-sidebar']/div/div/div/div/div[2]/div[1]/div/div/div/div/div/span")
            # My Jobs 패널에서 [X]버튼 클릭
            driver.find_element_by_xpath("//div[@id='right-sidebar']/span/i").click()

        except:
            print('TEST FAIL : check_myJobs')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/checkMyJobs-%s.png' % now)
        else:
            print('TEST PASS :check_myJobs')


    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(MyJobs("test_check_myJobs"))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())