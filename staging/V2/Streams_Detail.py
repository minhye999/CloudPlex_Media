# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class Streams_Detail(unittest.TestCase):

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
            # 검증용 스트림 URL 불러오기 (stream명 : autotest)
            driver.get(
                "http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/live/streams/1577683663BmfZ")
            time.sleep(10)
            # Breadcrumb 확인 (Live > Streams > 1577683663BmfZ)
            self.driver.find_element_by_xpath('//div[@id="root"]/div/div/div[1]/div/div[1]/nav/ol/li[1]')
            self.assertEqual("Streams", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Live'])[2]/following::li[1]").text)
            self.assertEqual("1577683663BmfZ", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Streams'])[2]/following::li[1]").text)
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
            # 검증용 스트림 URL 불러오기 (stream명 : autotest)
            driver.get(
                "http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/live/streams/1577683663BmfZ")
            time.sleep(10)
            # Title 확인 (autotest)
            self.assertEqual("autotest", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::span[1]").text)
        except:
            print('TEST FAIL : checkTitle')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkTitle')

    def test_checkStreamOverview(self):  # Stream Overview 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # 검증용 스트림 URL 불러오기 (stream명 : autotest)
            driver.get(
                "http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/live/streams/1577683663BmfZ")
            time.sleep(10)
            # Stream Overview Title 확인
            self.assertEqual("Stream Overview", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Delete'])[1]/following::h4[1]").text)

            # Streams ID 텍스트 및 해당 ID 확인
            self.assertEqual("Streams ID", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Stream Overview'])[1]/following::strong[1]").text)
            self.assertEqual("1577683663BmfZ", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Streams ID'])[1]/following::span[1]").text)

            # Status 텍스트 및 해당 상태 확인
            self.assertEqual("Status", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Streams ID'])[1]/following::strong[1]").text)
            self.assertEqual("ACTIVE", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Status'])[1]/following::span[2]").text)

            # Channel 텍스트 및 해당 채널 확인
            self.assertEqual("Channel", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='ACTIVE'])[1]/following::strong[1]").text)
            self.assertEqual("channel1", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channel'])[1]/following::span[1]").text)

            # Listing 텍스트 및 해당 리스팅 확인
            self.assertEqual("Listing", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='channel1'])[1]/following::strong[1]").text)
            self.assertEqual("list1", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Listing'])[1]/following::span[1]").text)

            # Owner 텍스트 및 해당 owner확인
            self.assertEqual("Owner", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='list1'])[1]/following::strong[1]").text)
            self.assertEqual("이선애", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Owner'])[1]/following::span[2]").text)

            # Created 텍스트 및 해당 일자 확인
            self.assertEqual("Created at", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='(rosa@mz.co.kr)'])[1]/following::strong[1]").text)
            self.assertEqual("2019-12-30 14:27:44", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created at'])[1]/following::span[1]").text)

        except:
            print('TEST FAIL : checkStreamOverview')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkStreamOverview')

    def test_checkInput(self):  # Input 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # 검증용 스트림 URL 불러오기 (stream명 : autotest)
            driver.get(
                "http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/live/streams/1577683663BmfZ")
            time.sleep(10)
            # Input 타이틀 확인
            self.driver.find_element_by_xpath(
                '//div[@id="root"]/div/div/div[1]/div/div[2]/div[2]/div/div/div/h4/span')
            # Type 항목명 확인
            self.assertEqual("Type", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Inputs'])[1]/following::strong[1]").text)
            # Type 설정값 - RTMP(PUSH) 확인
            self.assertEqual("RTMP(PUSH)",driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Type'])[1]/following::span[1]").text)
            # Security 항목명 확인
            self.assertEqual("Security", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='RTMP(PUSH)'])[1]/following::strong[1]").text)
            # Whitelist to Request 항목명 확인
            self.assertEqual("Whitelist to Request", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Security'])[1]/following::strong[1]").text)
            # Whitelist to Request 설정값 - Anywhere 확인
            self.assertEqual("Anywhere", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Whitelist to Request'])[1]/following::p[1]").text)

        except:
            print('TEST FAIL : checkInput')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkInput')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Streams_Detail('test_checkBreadcrumb'))
    suite.addTest(Streams_Detail("test_checkTitle"))
    suite.addTest(Streams_Detail("test_checkStreamOverview"))
    suite.addTest(Streams_Detail("test_checkInput"))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())