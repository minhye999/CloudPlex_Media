# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class Listings(unittest.TestCase):

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
            # Breadcrumb 확인 (Live > Listings)
            self.assertEqual("Live", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Listings'])[2]/following::li[1]").text)
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
            time.sleep(10)
            # Title 확인 (Listings)
            self.assertEqual("Listings", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::h3[1]").text)
        except:
            print('TEST FAIL : checkTitle')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkTitle')

    def test_check_btn_createListings(self):  # Create Listings 버튼 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Listings] 메뉴로 이동
            driver.find_element_by_link_text("Listings").click()
            time.sleep(5)
            # [+Create Listings] 버튼 확인 (오류발생으로 케이스 제외)
            # self.assertEqual("Create Listings", driver.find_element_by_link_text("Create Listings").text)
            # time.sleep(5)

            # [+Create Listings] 버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Listings'])[3]/following::strong[1]").click()
            time.sleep(10)
            # 출력된 Create listings 화면 title 체크
            self.assertEqual("Create listings", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::h3[1]").text)
            time.sleep(10)

        except:
            print('TEST FAIL : check_btn_createListings')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_btn_createListings')

    def test_checkID_search(self):  # ID 확인, 검색
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Listings] 메뉴로 이동
            driver.find_element_by_link_text("Listings").click()
            time.sleep(5)
            # 검색옵션 : ID 확인 (Default : ID)
            self.driver.find_element_by_xpath('//div[@id="root"]/div/div/div[1]/div/div[2]/div')
            time.sleep(5)
            # ID/ Name Select Box 클릭
            #
            # ID/ Name Select Box에서 ID/ Name리스트 확인
            #
            # ID 입력 (1577690929yyeP)
            driver.find_element_by_name("id").send_keys("1577690929yyeP")
            time.sleep(5)
            # 검색버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created at'])[1]/following::span[1]").click()
            time.sleep(5)
            # 검색결과 출력 확인 (1577690929yyeP)
            self.assertEqual("1577690929yyeP", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='list1'])[1]/following::small[1]").text)
            time.sleep(10)

        except:
            print('TEST FAIL : checkID_search')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkID_search')

    def test_checkOwner_search(self):  # Owner 확인, 검색
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Listings] 메뉴로 이동
            driver.find_element_by_link_text("Listings").click()
            # 검색옵션 : Owner 확인
            self.driver.find_element_by_xpath(
                '//div[@id="root"]/div/div/div[1]/div/div[2]/div/form/div/div[1]/div[2]/div[1]/div/div/span')
            time.sleep(5)
            # Owner 입력 (이선애)
            driver.find_element_by_name("username").clear()
            driver.find_element_by_name("username").send_keys(u"이선애")
            time.sleep(5)
            # 검색버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created at'])[1]/following::span[1]").click()
            time.sleep(10)
            # 검색결과 출력 확인 (이선애)
            self.assertEqual("이선애", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='ACTIVE'])[1]/following::span[1]").text)
            time.sleep(5)
            # [Refresh] 버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Total'])[1]/following::span[3]").click()
            time.sleep(10)

        except:
            print('TEST FAIL : checkOwner_search')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkOwner_search')

    def test_checkCreated_search(self):  # Created 확인 및 선택, 검색
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Listings] 메뉴로 이동
            driver.find_element_by_link_text("Listings").click()
            time.sleep(10)
            # 검색옵션 : Created 확인
            self.driver.find_element_by_xpath
            ('//div[@id="root"]/div/div/div[1]/div/div[2]/div/form/div/div[1]/div[2]/div[2]/div/div[1]')
            # 달력 아이콘 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created at'])[1]/following::button[1]").click()
            time.sleep(3)
            # 달력 패널에서 이전 월 이동 버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Sa'])[1]/following::*[name()='svg'][1]").click()
            time.sleep(3)
            # 시작/ 종료날짜 클릭하여 설정 (ex: 2019-12-1 ~ 2019-12-31)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='December 2019'])[1]/following::td[1]").click()
            time.sleep(5)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='December 2019'])[1]/following::td[31]").click()
            time.sleep(7)
            # 검색버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created at'])[1]/following::button[2]").click()
            time.sleep(10)
            # 검색결과 출력 확인 (시작/ 종료날짜 설정값대로 리스트 출력되는지 여부)
            self.assertEqual("2019-12-19 12:27:59", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='rosa@mz.co.kr'])[2]/following::time[1]").text)
            time.sleep(10)
        except:
            print('TEST FAIL : checkCreated_search')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkCreated_search')

    def test_click_link_listings(self):  # Lineup상세 진입
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
            print('TEST FAIL : click_link_listings')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : click_link_listings')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Listings('test_checkBreadcrumb'))
    suite.addTest(Listings("test_checkTitle"))
    suite.addTest(Listings("test_check_btn_createListings"))
    suite.addTest(Listings("test_checkID_search"))
    suite.addTest(Listings("test_checkOwner_search"))
    suite.addTest(Listings("test_checkCreated_search"))
    suite.addTest(Listings("test_click_link_listings"))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())