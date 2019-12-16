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
        self.driver = webdriver.Chrome(executable_path="../../venv/webdriver/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
##################################################################################################################

    def test_checkProfile(self):  # Profile 확인 및 선택
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.moveMainPage(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            time.sleep(3)
            # Profile Text 확인
            self.assertEqual("Profile", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='hls with multiple audio manual'])[1]/following::h6[1]").text)
            # Profile 확인 (MPEG-Dash video profile)
            self.assertEqual("HLS video with multiple audio profile", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Profile'])[1]/following::span[1]").text)
            # Profile 링크 클릭
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Profile'])[1]/following::span[1]").click()

            #Profile Detail 팝업 출력 확인 (Title만 체크)
            #self.assertEqual("Profile Detail", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='(10)'])[1]/following::h5[1]").text)
            #self.assertEqual("Profile Detail", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='(10)'])[1]/following::h5[1]").text)
        except:
            print('TEST FAIL : checkProfile')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                'F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkProfile')

####################################################################################################################
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

if __name__ == "__main__":
    unittest.main()
