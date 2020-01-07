# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class Listings_Create(unittest.TestCase):

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
            # [Listings] 메뉴로 이동
            driver.find_element_by_link_text("Listings").click()
            # [Create Listings]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Listings'])[3]/following::strong[1]").click()
            # Breadcrumb 확인 (Live > Listings)
            self.assertEqual("Live", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Create listings'])[1]/following::li[1]").text)
            self.assertEqual("Listings", driver.find_element_by_xpath(
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
            # [Listings] 메뉴로 이동
            driver.find_element_by_link_text("Listings").click()
            # [Create Listings]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Listings'])[3]/following::strong[1]").click()
            # Title 확인 (Create Listings)
            self.assertEqual("Create Listings", driver.find_element_by_xpath(
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
            # [Listings] 메뉴로 이동
            driver.find_element_by_link_text("Listings").click()
            # [+Create Listings] 버튼  클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Listings'])[3]/following::strong[1]").click()
            # 항목명 확인 (Name)
            self.assertEqual("Name", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Listings'])[2]/following::strong[1]").text)
            # 필수값 표시 확인 (*)
            self.assertEqual("*", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Name'])[1]/following::span[1]").text)
            time.sleep(3)
            # Name 입력필드 value 확인
            driver.find_element_by_xpath("//input[@value='']").click()
            # Name 입력 (create list)
            driver.find_element_by_xpath("//input[@value='']").clear()
            driver.find_element_by_xpath("//input[@value='']").send_keys("create list")
            time.sleep(10)

        except:
            print('TEST FAIL : checkName')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkName')

    def test_checkInputs(self):  # Input 선택
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Listings] 메뉴로 이동
            driver.find_element_by_link_text("Listings").click()
            time.sleep(3)
            # [+Create Listings] 버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Listings'])[3]/following::strong[1]").click()
            time.sleep(3)
            # 항목명 확인 (Inputs)
            self.assertEqual("Inputs", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::strong[1]").text)
            time.sleep(3)
            # Stream 항목명 확인
            self.assertEqual("Stream", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Inputs'])[1]/following::strong[1]").text)
            time.sleep(3)
            # Stream [Add]버튼 확인
            self.assertEqual("Add", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Stream'])[1]/following::button[1]").text)
            time.sleep(3)
            # Stream [Add]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Stream'])[1]/following::button[1]").click()
            time.sleep(3)
            # Streams Select Box 내 안내문구, 펼치기 버튼 확인 (생성된 소스 있고, 선택안된 상태) -> 클릭 아이콘 출력으로 문구 확인불가
            #
            # Streams Select Box 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Stream'])[1]/following::button[1]").click()
            time.sleep(3)
            # Streams Select Box 패널 하단으로 스크롤 -> 스크롤 동작 확인 불가
            #
            # Streams Select Box 패널 내 Source 클릭 -> 리스트 최상단 소스로 선택하여 테스트
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='RTMP(PUSH)'])[1]/following::strong[1]").click()
            time.sleep(3)
            # Streams Select Box 내 선택한 Source 정보 확인 (Type 라벨, Streams name, ID, [X]버튼) -> 클릭 아이콘 출력으로 문구 확인불가
            #
            # 생성된 Streams Select Box [X]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/form/div[2]/div[2]/div/div/div[2]/div/button/i").click()
            time.sleep(3)
            # File source 항목명 확인
            self.assertEqual("File source", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Add'])[1]/following::strong[1]").text)
            # File source 설정값 - MP4 확인
            self.assertEqual("MP4", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='File source'])[1]/following::span[1]").text)
            time.sleep(10)

        except:
            print('TEST FAIL : checkInputs')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkInputs')

    def test_checkSettings(self):  # Settting 설정
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Listings] 메뉴로 이동
            driver.find_element_by_link_text("Listings").click()
            time.sleep(3)
            # [+Create Listings] 버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Listings'])[3]/following::strong[1]").click()
            time.sleep(3)
            # 항목명 확인 (Settings)
            self.assertEqual("Settings", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='MP4'])[1]/following::strong[1]").text)
            time.sleep(3)
            # Follow default values 항목명 확인
            self.assertEqual("Follow default values", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Settings'])[1]/following::strong[1]").text)
            time.sleep(3)
            # 라디오 버튼 Default 선택값 확인 (Follow default values)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div[1]/div/div[2]/div/form/div[3]/div[2]/div/div[1]/div[1]/div/label/input").is_selected()
            time.sleep(3)
            # Box내 Timezone 항목명 확인
            self.assertEqual("Timezone", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Follow default values'])[1]/following::strong[1]").text)
            time.sleep(3)
            # Box내 Timezone 설정값 - (GMT+09:00) Seoul 확인
            self.assertEqual("- (GMT+09:00) Seoul", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Timezone'])[1]/following::span[1]").text)
            # Box내 Loop To Fill Lineup Duration 항목명 확인
            self.assertEqual("Loop To Fill Lineup Duration", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Timezone'])[1]/following::strong[1]").text)
            time.sleep(3)
            # Box내 Loop To Fill Lineup Duration 설정값 - Off 확인
            self.assertEqual("- Off", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Loop To Fill Lineup Duration'])[1]/following::span[1]").text)
            # Individual settings 항목명 확인
            self.assertEqual("Individual settings", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Loop To Fill Lineup Duration'])[1]/following::strong[1]").text)
            time.sleep(3)
            # 라디오 버튼 확인(Individual settings)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div[1]/div/div[2]/div/form/div[3]/div[2]/div/div[1]/div[1]/div/label/input").is_displayed()
            # Timezone 항목명 확인
            self.assertEqual("Timezone", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Individual settings'])[1]/following::span[1]").text)
            time.sleep(3)
            # Timezone 설정값 - (GMT+09:00) Seoul 확인
            self.assertEqual("- (GMT+09:00) Seoul", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Timezone'])[1]/following::span[1]").text)
            # Loop to Fill Lineup Duration 항목명 확인
            self.assertEqual("Loop to Fill Lineup Duration", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='(GMT+09:00) Seoul'])[1]/following::span[1]").text)
            # Loop To Fill Lineup Duration 설정값 - On/ Off 항목 확인
            self.assertEqual("On", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Loop to Fill Lineup Duration'])[1]/following::span[1]").text)
            self.assertEqual("Off", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='On'])[1]/following::span[1]").text)
            time.sleep(10)

        except:
            print('TEST FAIL : checkSettings')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkSettings')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Listings_Create('test_checkBreadcrumb'))
    suite.addTest(Listings_Create("test_checkTitle"))
    suite.addTest(Listings_Create("test_checkName"))
    suite.addTest(Listings_Create("test_checkInputs"))
    suite.addTest(Listings_Create("test_checkSettings"))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())