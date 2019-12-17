# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class test(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
##################################################################################################################

    def test_check_img_logo(self):  # Service Logo 출력 및 링크 이동 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Service Logo 확인
            #self.driver.find_element_by_xpath("//div[@class='navbar-brand brand-logo']") -> 요것도 안되네
            driver.find_element_by_xpath("//img[@alt='logo']")
            # Jobs Page로 이동
            driver.find_element_by_link_text("Jobs").click()
            time.sleep(3)
            # Brand Logo 클릭
            driver.find_element_by_xpath("//img[@alt='logo']").click()
            time.sleep(3)
            # Main Page로 이동 확인 (Create Jobs Title 확인)
            self.assertEqual("Create Job", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::h3[1]").text)
        except:
            print('TEST FAIL : check_img_logo')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_img_logo')

####################################################################################################################
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

if __name__ == "__main__":
    unittest.main()
