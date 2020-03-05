# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class Streams_Create(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_checkBreadcrumb(self):  # Breadcrumb 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Streams] 메뉴로 이동
            driver.find_element_by_link_text("Streams").click()
            # [Create Streams]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Streams'])[3]/following::strong[1]").click()
            # Breadcrumb 확인 (Live > Streams)
            self.assertEqual("Live", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Create Streams'])[1]/following::li[1]").text)
            self.assertEqual("Streams", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Live'])[2]/following::li[1]").text)
            time.sleep(10)
        except:
            print('TEST FAIL : checkBreadcrumb')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkBreadcrumb')

    def test_checkTitle(self):  # Title 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Streams] 메뉴로 이동
            driver.find_element_by_link_text("Streams").click()
            # [Create Streams]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Streams'])[3]/following::strong[1]").click()
            # Title 확인 (Create Streams)
            self.assertEqual("Create Streams", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::h3[1]").text)
            time.sleep(10)
        except:
            print('TEST FAIL : checkTitle')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkTitle')

    def test_checkName(self):  # Name입력
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Streams] 메뉴로 이동
            driver.find_element_by_link_text("Streams").click()
            # [+Create streams] 버튼  클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Streams'])[3]/following::strong[1]").click()
            # 항목명 확인 (Name)
            self.assertEqual("Name", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Streams'])[2]/following::strong[1]").text)
            # 필수값 표시 확인 (*)
            self.assertEqual("*", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Name'])[1]/following::span[1]").text)
            time.sleep(3)
            # Name 입력필드 value 확인
            driver.find_element_by_xpath("//input[@value='']").click()
            # Name 입력 (create rtmp)
            driver.find_element_by_xpath("//input[@value='']").clear()
            driver.find_element_by_xpath("//input[@value='']").send_keys("create rtmp")
            time.sleep(10)

        except:
            print('TEST FAIL : checkName')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkName')

    def test_checkType(self):  # Type선택
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
            # 항목명 확인 (Type)
            self.assertEqual("Type", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::strong[1]").text)
            time.sleep(3)
            # 필수값 표시 확인 (*)
            self.assertEqual("*", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Type'])[1]/following::span[1]").text)
            time.sleep(3)
            # Default 선택값 확인 (RTMP(PUSH))
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div[1]/div/div[2]/div/form/div[2]/div[2]/div/div/div[1]/label/input").is_selected()
            # Type 확인 (RTMP(PUSH))
            self.assertEqual("RTMP(PUSH)", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='*'])[2]/following::span[1]").text)
            time.sleep(3)
            # Type 확인 (RTP(PUSH))
            self.assertEqual("RTP(PUSH)", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='RTMP(PUSH)'])[1]/following::span[1]").text)
            time.sleep(10)

        except:
            print('TEST FAIL : checkType')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkType')

    def test_checkSecurity(self):  # Security 확인 및 선택
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
            # 항목명 확인 (Security)
            self.assertEqual("Security", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='RTP(PUSH)'])[1]/following::strong[1]").text)
            # 필수값 표시 확인 (*)
            self.assertEqual("*", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Security'])[1]/following::span[1]").text)
            # Whitelist to Request 항목명 확인
            self.assertEqual("Whitelist to Request", driver.find_element_by_xpath(
                "(.// *[normalize-space(text()) and normalize - space(.)='*'])[3] / following::strong[1]").text)
            # [i]아이콘 확인
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/form/div[3]/div[2]/div/div/div/label/div/i").text()
            # [i]아이콘 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[2]/div/form/div[3]/div[2]/div/div/div/label/div/i").click()
            # info 내용 확인(Whitelist rules)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Whitelist to Request'])[1]/following::strong[1]").text()
            # Whitelist 입력필드 value 확인
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[2]/div/form/div[3]/div[2]/div/div/div[2]/div/div/textarea").click()
            # Whitelist 입력 (0.0.0.0/0)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/form/div[3]/div[2]/div/div/div[2]/div/div/textarea").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='xxx.xxx.xxx.xxx/yy'])[1]/following::textarea[1]").clear()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='xxx.xxx.xxx.xxx/yy'])[1]/following::textarea[1]").send_keys(
                "0.0.0.0/0")
            time.sleep(3)
            # [Select whitelist used]버튼 확인
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Anywhere'])[1]/following::button[1]")
            # [Select whitelist used]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Anywhere'])[1]/following::button[1]").click()
            time.sleep(3)
            # [Select whitelist used]팝업 타이틀 확인
            self.assertEqual("Select whitelist used", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::h5[1]").text)
            time.sleep(3)
            # [Select whitelist used]팝업에서 리스트 선택(최상위 항목 체크박스 클릭)
            driver.find_element_by_xpath("//input[@value='0']").click()
            # [Select]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
            time.sleep(3)
            # Anywhere 항목 확인
            self.assertEqual("Anywhere", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='xxx.xxx.xxx.xxx/yy'])[1]/following::span[1]").text)
            # Anywhere 항목 체크
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='xxx.xxx.xxx.xxx/yy'])[1]/following::span[1]").click()
            # Whitelist 입력박스 및 [Select whitelist used]버튼 비활성 처리 확인 (xpath, div class모두 안찍혀 케이스 제외)
            #driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[2]/div/form/div[3]/div[2]/div/div/div[2]/div/div/textarea").click()
            #driver.find_element_by_xpath("//div[@id='root']/div/div/div[1]/div/div[2]/div/form/div[3]/div[2]/div/div/div[2]/div[2]/div[2]").click()
            time.sleep(10)

        except:
            print('TEST FAIL : checkSecurity')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkSecurity')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Streams_Create('test_checkBreadcrumb'))
    suite.addTest(Streams_Create("test_checkTitle"))
    suite.addTest(Streams_Create("test_checkName"))
    suite.addTest(Streams_Create("test_checkType"))
    suite.addTest(Streams_Create("test_checkSecurity"))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())