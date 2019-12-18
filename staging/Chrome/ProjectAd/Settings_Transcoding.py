# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class Settings_Transcoding(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_settings_transcoding_origin_enable(self):  # Create origin asset : Enable 설정
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Admin]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/nav/div[2]/div/ul/li[4]/div/div/button/i").click()
            # Admin 메뉴에서 [Project manager] 메뉴 선택
            driver.find_element_by_link_text("Project manager").click()
            time.sleep(3)
            # [Transcoding]탭 클릭
            driver.find_element_by_link_text("Transcoding").click()
            # [Create origin asset] : [Enable] 선택
            #driver.find_element_by_xpath("//input[@type='radio']").click()
            driver.find_element_by_xpath("(//input[@type='radio'])[2]").click()
            # [Save]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
            time.sleep(3)
        except:
            print('TEST FAIL : test_settings_transcoding_origin_enable')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_settings_transcoding_origin_enable-%s.png' % now)
        else:
            print('TEST PASS : test_settings_transcoding_origin_enable')

    def test_settings_transcoding_origin_disable(self):  # Create origin asset : Disable 설정
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Admin]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/nav/div[2]/div/ul/li[4]/div/div/button/i").click()
            # Admin 메뉴에서 [Project manager] 메뉴 선택
            driver.find_element_by_link_text("Project manager").click()
            time.sleep(3)
            # [Transcoding]탭 클릭
            driver.find_element_by_link_text("Transcoding").click()
            # [Create origin asset] : [Disable] 선택
            driver.find_element_by_xpath("(//input[@type='radio'])[2]").click()
            # [Save]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
            time.sleep(3)
        except:
            print('TEST FAIL : test_settings_transcoding_origin_disable')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_settings_transcoding_origin_enable-%s.png' % now)
        else:
            print('TEST PASS : test_settings_transcoding_origin_disable')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Settings_Transcoding('test_settings_transcoding_origin_enable'))
    suite.addTest(Settings_Transcoding('test_settings_transcoding_origin_disable'))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())