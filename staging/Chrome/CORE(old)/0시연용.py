# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class Assets2(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_check_quickSearch_name(self):  # Name 검색 기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            time.sleep(3)
            # 항목명 확인 (Quick Search)
            self.assertEqual("Quick Search", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='+ Create Assets'])[1]/following::label[1]").text)
            # Advanced Search 전환 버튼 확인
            self.driver.find_element_by_xpath('//*[@class="sprite sprite-switch"]')
            # 입력필드 value 확인
            self.assertEqual("", driver.find_element_by_id("quick-search").get_attribute("value"))
            # [Search]버튼 확인
            self.assertEqual("Search", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").text)
            # [Reset]버튼 value 확인
            self.assertEqual("", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Search'])[1]/following::button[1]").get_attribute(
                "value"))
            # 유효한 검색어 입력 (Name) > [Search]버튼 클릭 > 검색결과 확인 (Name)
            driver.find_element_by_id("quick-search").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys("CALL ME BABY")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").click()
            self.assertEqual(u"EXO 엑소 'CALL ME BABY' MV", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='MP4'])[1]/following::p[1]").text)
        except:
            print('TEST FAIL : test_check_quickSearch_name')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_quickSearch_name-%s.png' % now)
        else:
            print('TEST PASS : test_check_quickSearch_name')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Assets2("test_check_quickSearch_name"))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())