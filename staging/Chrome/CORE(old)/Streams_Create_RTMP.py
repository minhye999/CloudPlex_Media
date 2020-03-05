# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class Streams_Create_RTMP(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_check_input_whitelist(self):  # whitelist 입력하여 생성
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Streams] 메뉴로 이동
            driver.find_element_by_link_text("Streams").click()
            time.sleep(3)
            # [+Create streams] 버튼  클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Streams'])[3]/following::strong[1]").click()
            time.sleep(3)
            # Type 선택 (RTMP(PUSH))
            driver.find_element_by_name("streamTypes").click()
            time.sleep(10)
            # Security > Whitelist 입력 (0.0.0.0/0)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/form/div[3]/div[2]/div/div/div[2]/div/div/textarea").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='xxx.xxx.xxx.xxx/yy'])[1]/following::textarea[1]").clear()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='xxx.xxx.xxx.xxx/yy'])[1]/following::textarea[1]").send_keys(
                "0.0.0.0/0")
            time.sleep(3)
            # 그 외 필수값(Name_rtmp1) 입력하고 [Create]버튼 클릭
            driver.find_element_by_xpath("//input[@value='']").click()
            driver.find_element_by_xpath("//input[@value='']").clear()
            driver.find_element_by_xpath("//input[@value='']").send_keys("rtmp1")
            time.sleep(5)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
            time.sleep(5)
            # 생성한 Stream상세 페이지의 타이틀 확인 (rtmp1)
            self.assertEqual("rtmp1", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::span[1]").text)
            time.sleep(5)


        except:
            print('TEST FAIL : check_input_whitelist')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_input_whitelist')

    def test_check_anywhere_whitelist(self):  # anywhere 클릭하여 생성
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Streams] 메뉴로 이동
            driver.find_element_by_link_text("Streams").click()
            # [+Create streams] 버튼  클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Streams'])[3]/following::strong[1]").click()
            # Type 선택 (RTMP(PUSH))
            driver.find_element_by_name("streamTypes").click()
            time.sleep(10)
            # Anywhere 항목 체크
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='xxx.xxx.xxx.xxx/yy'])[1]/following::span[1]").click()
            # 그 외 필수값(Name_rtmp2) 입력하고 [Create]버튼 클릭
            driver.find_element_by_xpath("//input[@value='']").click()
            driver.find_element_by_xpath("//input[@value='']").clear()
            driver.find_element_by_xpath("//input[@value='']").send_keys("rtmp2")
            time.sleep(5)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
            time.sleep(5)
            # 생성한 Stream상세 페이지의 타이틀 확인 (rtmp2)
            self.assertEqual("rtmp2", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::span[1]").text)
            time.sleep(5)

        except:
            print('TEST FAIL : check_anywhere_whitelist')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_anywhere_whitelist')

    def test_check_select_whitelist(self):  # whitelist 리스트 선택하여 생성
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Streams] 메뉴로 이동
            driver.find_element_by_link_text("Streams").click()
            # [+Create streams] 버튼  클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Streams'])[3]/following::strong[1]").click()
            # Type 선택 (RTMP(PUSH))
            driver.find_element_by_name("streamTypes").click()
            time.sleep(10)
            # [Select whitelist used]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Anywhere'])[1]/following::button[1]").click()
            time.sleep(3)
            # [Select whitelist used]팝업에서 리스트 선택(최상위 항목 체크박스 클릭, 스테이지 서버의 경우 32.32.32.32/10)
            driver.find_element_by_xpath("//input[@value='0']").click()
            # [Select]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
            time.sleep(3)
            # 그 외 필수값(Name_rtmp3) 입력하고 [Create]버튼 클릭
            driver.find_element_by_xpath("//input[@value='']").click()
            driver.find_element_by_xpath("//input[@value='']").clear()
            driver.find_element_by_xpath("//input[@value='']").send_keys("rtmp3")
            time.sleep(5)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
            time.sleep(5)
            # 생성한 Stream상세 페이지의 타이틀 확인 (rtmp3)
            self.assertEqual("rtmp3", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::span[1]").text)
            time.sleep(5)

        except:
            print('TEST FAIL : check_select_whitelist')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_select_whitelist')
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Streams_Create_RTMP('test_check_input_whitelist'))
    suite.addTest(Streams_Create_RTMP("test_check_anywhere_whitelist"))
    suite.addTest(Streams_Create_RTMP("test_check_select_whitelist"))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())