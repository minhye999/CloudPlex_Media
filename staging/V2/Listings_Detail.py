# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class Listings_Detail(unittest.TestCase):

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
            # 검증용 Listing URL 불러오기 (listing명 : list1)
            driver.get(
                "http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/live/listings/1577690929yyeP")
            time.sleep(10)
            # Breadcrumb 확인 (Live > Listings > 1577690929yyeP)
            self.driver.find_element_by_xpath('//div[@id="root"]/div/div/div[1]/div/div[1]/nav/ol/li[1]')
            self.assertEqual("Listings", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Live'])[2]/following::li[1]").text)
            self.assertEqual("1577690929yyeP", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Listings'])[2]/following::li[1]").text)
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
            # 검증용 Listing URL 불러오기 (listing명 : list1)
            driver.get(
                "http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/live/listings/1577690929yyeP")
            time.sleep(10)
            # Title 확인 (list1)
            self.assertEqual("list1", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::span[1]").text)
        except:
            print('TEST FAIL : checkTitle')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkTitle')

    def test_checkListingsOverview(self):  # Listings Overview 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # 검증용 Listing URL 불러오기 (listing명 : list1)
            driver.get(
                "http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/live/listings/1577690929yyeP")
            time.sleep(10)
            # Listings Overview Title 확인
            self.assertEqual("Listings Overview", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Go to schedule'])[1]/following::h4[1]").text)

            # Listings ID 텍스트 및 해당 ID 확인
            self.assertEqual("Listings ID", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Listings Overview'])[1]/following::strong[1]").text)
            self.assertEqual("1577690929yyeP", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Listings ID'])[1]/following::span[1]").text)

            # Channel 텍스트 및 해당 채널 확인
            self.assertEqual("Channel", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Listings ID'])[1]/following::strong[1]").text)
            self.assertEqual("channel1 (1577691371Sc7v)", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channel'])[1]/following::span[1]").text)

            # Status 텍스트 및 해당 상태 확인
            self.assertEqual("Status", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='ACTIVE'])[1]/preceding::strong[1]").text)
            self.assertEqual("ACTIVE", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Status'])[1]/following::span[2]").text)

            # Owner 텍스트 및 해당 owner확인
            self.assertEqual("Owner", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='ACTIVE'])[1]/following::strong[1]").text)
            self.assertEqual("이선애", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Owner'])[1]/following::span[2]").text)

            # Created 텍스트 및 해당 일자 확인
            self.assertEqual("Created at", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='(rosa@mz.co.kr)'])[1]/following::strong[1]").text)
            self.assertEqual("2019-12-30 16:28:49", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created at'])[1]/following::span[1]").text)

        except:
            print('TEST FAIL : checkListingsOverview')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkListingsOverview')

    def test_checkInput(self):  # Input 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # 검증용 Listing URL 불러오기 (listing명 : list1)
            driver.get(
                "http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/live/listings/1577690929yyeP")
            time.sleep(10)
            # Input 타이틀 확인
            self.driver.find_element_by_xpath(
                '//div[@id="root"]/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/h4/span')
            # Streams 항목명 확인
            self.assertEqual("Streams", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Inputs'])[1]/following::strong[1]").text)
            # Streams 설정값 - RTMP(PUSH), autotest(1577683663BmfZ) 확인
            self.assertEqual("RTMP(PUSH)", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Streams'])[2]/following::span[1]").text)
            self.assertEqual("autotest", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='RTMP(PUSH)'])[1]/following::strong[1]").text)
            # File source 항목명 확인
            self.assertEqual("File source", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='autotest'])[1]/following::strong[1]").text)
            # File source 설정값 - MP4 확인
            self.assertEqual("MP4", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='File source'])[1]/following::span[1]").text)

        except:
            print('TEST FAIL : checkInput')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkInput')

    def test_checkSettings(self):  # Settings 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # 검증용 Listing URL 불러오기 (listing명 : list1)
            driver.get(
                "http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/live/listings/1577690929yyeP")
            time.sleep(10)
            # Settings 타이틀 확인
            self.driver.find_element_by_xpath(
                '//div[@id="root"]/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]/div/h4/span')
            # Timezone 항목명 확인
            self.assertEqual("Timezone", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Settings'])[1]/following::strong[1]").text)
            # Timezone 설정값 - (GMT+09:00) Seoul 확인
            self.assertEqual("(GMT+09:00) Seoul",driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Timezone'])[1]/following::div[1]").text)
            # Loop To Fill Lineup Duration 항목명 확인
            self.assertEqual("Loop To Fill Lineup Duration", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='(GMT+09:00) Seoul'])[1]/following::strong[1]").text)
            # Loop To Fill Lineup Duration 설정값 - Off 확인
            self.assertEqual("Off", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Loop To Fill Lineup Duration'])[1]/following::div[1]").text)

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
    suite.addTest(Listings_Detail('test_checkBreadcrumb'))
    suite.addTest(Listings_Detail("test_checkTitle"))
    suite.addTest(Listings_Detail("test_checkListingsOverview"))
    suite.addTest(Listings_Detail("test_checkInput"))
    suite.addTest(Listings_Detail("test_checkSettings"))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())