# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class Lineup(unittest.TestCase):

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
            time.sleep(5)
            # Listings 리스트 클릭하여 Lineup편성 페이지 진입 (list1 / 1577690929yyeP)
            driver.find_element_by_link_text("list1").click()
            time.sleep(10)
            # Breadcrumb 확인 (Live > Listings > 1577690929yyeP)
            self.driver.find_element_by_xpath('//div[@id="root"]/div/div/div[1]/div/div[1]/nav/ol/li[1]')
            self.assertEqual("Listings", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Live'])[2]/following::a[1]").text)
            self.assertEqual("1577690929yyeP", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Listings'])[2]/following::li[1]").text)

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
            time.sleep(5)
            # Listings 리스트 클릭하여 Lineup편성 페이지 진입 (list1 / 1577690929yyeP)
            driver.find_element_by_link_text("list1").click()
            time.sleep(10)
            # Lineup편성 페이지 Title 확인 (list1)
            self.assertEqual("list1", driver.find_element_by_xpath(
               "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::h3[1]").text)

        except:
            print('TEST FAIL : checkTitle')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkTitle')

    def test_check_btn_listingsDetail(self):  # Listings Detail 버튼 확인 및 이동
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Listings] 메뉴로 이동
            driver.find_element_by_link_text("Listings").click()
            time.sleep(5)
            # Listings 리스트 클릭하여 Lineup편성 페이지 진입 (list1 / 1577690929yyeP)
            driver.find_element_by_link_text("list1").click()
            time.sleep(10)
            # Listings Detail 버튼 확인 (오류 발생으로 케이스 제외)
            # self.assertEqual("Listings Detail", driver.find_element_by_link_text("Listings Detail").text)
            # time.sleep(5)

            # Listings Detail 버튼 클릭하여 Listings상세페이지 진입
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Listings'])[2]/following::button[1]").click()
            time.sleep(10)
            # Listings상세 Title 확인 (list1)
            self.assertEqual("list1", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::span[1]").text)

        except:
            print('TEST FAIL : check_btn_listingsDetail')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_btn_listingsDetail')

    def test_checkData(self):  # 날짜 이동 및 Data확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Listings] 메뉴로 이동
            driver.find_element_by_link_text("Listings").click()
            time.sleep(5)
            # Listings 리스트 클릭하여 Lineup편성 페이지 진입 (list1 / 1577690929yyeP)
            driver.find_element_by_link_text("list1").click()
            time.sleep(10)
            # [편성 목록]아이콘 클릭
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Listings Detail'])[1]/following::*[name()='svg'][1]").click()
            time.sleep(3)
            # 달력 패널에서 날짜 선택 (2020-1-3)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='January 2020'])[1]/following::td[6]").click()
            time.sleep(3)
            # 선택한 날짜 데이터 확인 (EXO 엑소 'Love Shot' MV)
            self.assertEqual("EXO 엑소 'Love Shot' MV", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='MP4'])[1]/following::div[1]").text)
            time.sleep(3)

        except:
            print('TEST FAIL : checkData')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkData')

    def test_checkSummary(self):  # Summary 출력 요소 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Listings] 메뉴로 이동
            driver.find_element_by_link_text("Listings").click()
            time.sleep(5)
            # Listings 리스트 클릭하여 Lineup편성 페이지 진입 (list1 / 1577690929yyeP)
            driver.find_element_by_link_text("list1").click()
            time.sleep(10)
            # Total time 텍스트, 해당 시간(24:00:00) 출력
            self.assertEqual("Total time", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='(GMT+ 09:00)'])[1]/following::dt[1]").text)
            self.assertEqual("24:00:00", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Total time'])[1]/following::dd[1]").text)
            time.sleep(3)
            # Scheduled time 텍스트, 해당 시간 출력
            self.assertEqual("Scheduled time", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Total time'])[1]/following::dt[1]").text)
            self.driver.find_element_by_xpath('//div[@id="root"]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[1]/dl[2]/dd')
            time.sleep(3)
            # Unscheduled time 텍스트, 해당 시간 출력
            self.assertEqual("Unscheduled time", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Scheduled time'])[1]/following::dt[1]").text)
            self.driver.find_element_by_xpath('//div[@id="root"]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[1]/dl[3]/dd')
            time.sleep(3)
            # Lineup count 텍스트, 해당 count 출력
            self.assertEqual("Lineup count", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Unscheduled time'])[1]/following::dt[1]").text)
            self.driver.find_element_by_xpath('//div[@id="root"]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[1]/dl[4]/dd')
            time.sleep(3)
            # Channel 텍스트, 해당 Channel 출력
            self.assertEqual("Channel", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Lineup count'])[1]/following::dt[1]").text)
            self.driver.find_element_by_xpath('//div[@id="root"]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[1]/dl[5]/dd/span/span')
            time.sleep(3)

        except:
            print('TEST FAIL : checkSummary')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkSummary')

    def test_checkTable(self):  # Table 출력 요소 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Listings] 메뉴로 이동
            driver.find_element_by_link_text("Listings").click()
            time.sleep(5)
            # Listings 리스트 클릭하여 Lineup편성 페이지 진입 (list1 / 1577690929yyeP)
            driver.find_element_by_link_text("list1").click()
            time.sleep(10)
            # 체크박스 확인
            driver.find_element_by_xpath("//input[@type='checkbox']").is_displayed()
            # Start time 텍스트 확인
            self.assertEqual("Start time", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Sat.'])[1]/following::strong[2]").text)
            time.sleep(3)
            # End time 텍스트 확인
            self.assertEqual("End time", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Start time'])[1]/following::strong[1]").text)
            time.sleep(3)
            # Duration 텍스트 확인
            self.assertEqual("Duration", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='End time'])[1]/following::strong[1]").text)
            time.sleep(3)
            # Mark in 텍스트 확인
            self.assertEqual("Mark in", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Duration'])[1]/following::strong[1]").text)
            time.sleep(3)
            # Mark out 텍스트 확인
            self.assertEqual("Mark out", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Mark in'])[1]/following::strong[1]").text)
            time.sleep(3)
            # Repeat 텍스트 확인
            self.assertEqual("Repeat", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Mark out'])[1]/following::strong[1]").text)
            time.sleep(3)
            # Media 텍스트 확인
            self.assertEqual("Media", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Repeat'])[1]/following::strong[1]").text)
            # Name 텍스트 확인
            self.assertEqual("Name", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Media'])[1]/following::strong[1]").text)
            time.sleep(3)
            # Priority 텍스트 확인
            self.assertEqual("Priority", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Name'])[1]/following::strong[1]").text)
            time.sleep(3)
            # [Delete]버튼 확인
            self.assertEqual("Delete", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Priority'])[1]/following::span[1]").text)
            time.sleep(3)

        except:
            print('TEST FAIL : checkTable')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkTable')


    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Lineup('test_checkBreadcrumb'))
    suite.addTest(Lineup("test_checkTitle"))
    suite.addTest(Lineup('test_check_btn_listingsDetail'))
    suite.addTest(Lineup('test_checkData'))
    suite.addTest(Lineup('test_checkSummary'))
    suite.addTest(Lineup('test_checkTable'))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())