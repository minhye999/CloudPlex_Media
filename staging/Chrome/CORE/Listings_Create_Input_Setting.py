# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class Listings_Create_Input_Setting(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_checkInputStream(self):  # Stream 추가하여 생성
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
            # 그 외 필수값(Name_streamlist) 입력하고 [Create]버튼 클릭
            driver.find_element_by_xpath("//input[@value='']").click()
            driver.find_element_by_xpath("//input[@value='']").clear()
            driver.find_element_by_xpath("//input[@value='']").send_keys("streamlist")
            time.sleep(5)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
            time.sleep(5)
            # 생성된 Lineup편성 페이지의 타이틀 확인 (streamlist)
            self.assertEqual("streamlist", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::h3[1]").text)
            time.sleep(5)

        except:
            print('TEST FAIL : checkInputStream')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkInputStream')

    def test_checkLoopOff(self):  # LoopOff 설정하여 생성
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
            # 그 외 필수값(Name_loopoff) 입력하고 [Create]버튼 클릭
            driver.find_element_by_xpath("//input[@value='']").click()
            driver.find_element_by_xpath("//input[@value='']").clear()
            driver.find_element_by_xpath("//input[@value='']").send_keys("loopoff")
            time.sleep(5)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
            time.sleep(5)
            # 생성된 Lineup편성 페이지의 타이틀 확인 (loopoff)
            self.assertEqual("loopoff", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::h3[1]").text)
            time.sleep(5)

        except:
            print('TEST FAIL : checkLoopOff')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkLoopOff')

    def test_checkLoopOn(self):  # LoopOn 설정하여 생성
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
            # Individual settings 항목명 확인
            self.assertEqual("Individual settings", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Loop To Fill Lineup Duration'])[1]/following::strong[1]").text)
            time.sleep(3)
            # 라디오 버튼 클릭(Individual settings)
            driver.find_element_by_xpath("(//input[@name=''])[2]").click()
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
            # Loop to Fill Lineup Duration 설정값 - On 라디오 버튼 클릭
            driver.find_element_by_name("loopToFillLineupDuration").click()
            time.sleep(5)
            # 그 외 필수값(Name_loopon) 입력하고 [Create]버튼 클릭
            driver.find_element_by_xpath("//input[@value='']").click()
            driver.find_element_by_xpath("//input[@value='']").clear()
            driver.find_element_by_xpath("//input[@value='']").send_keys("loopon")
            time.sleep(5)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
            time.sleep(5)
            # 생성된 Lineup편성 페이지의 타이틀 확인 (loopon)
            self.assertEqual("loopon", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::h3[1]").text)
            time.sleep(5)

        except:
            print('TEST FAIL : checkLoopOn')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkLoopOn')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Listings_Create_Input_Setting('test_checkInputStream'))
    suite.addTest(Listings_Create_Input_Setting("test_checkLoopOff"))
    suite.addTest(Listings_Create_Input_Setting("test_checkLoopOn"))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())