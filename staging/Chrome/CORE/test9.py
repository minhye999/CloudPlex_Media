# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import sys
import logging
import time
from datetime import datetime

class test(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
##################################################################################################################

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
            self.driver.save_screenshot(
                'F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Screenshots/test_Title-%s.png' % now)
        else:
            print('TEST PASS : check_title')

####################################################################################################################
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

if __name__ == "__main__":
    unittest.main()
