# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class Videos(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_check_breadcrumb(self):  # Bread Crumb 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome") # 스테이지
        #driver.get("http://mz-cm-console-dev.s3-website.ap-northeast-2.amazonaws.com/") #개발
        #driver.get("https://console.media.megazone.io/welcome") #운영

        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # Bread Crumb 확인 (Contents > Videos)
            self.assertEqual("Contents", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Videos'])[2]/following::li[1]").text)
            self.assertEqual("Videos", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Contents'])[2]/following::li[1]").text)
        except:
            print('TEST FAIL : test_check_breadcrumb')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_breadcrumb-%s.png' % now)
        else:
            print('TEST PASS : test_check_breadcrumb')

    def test_check_title(self):  # Title 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # Title 확인 (Videos)
            self.assertEqual("Videos", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::h3[1]").text)
        except:
            print('TEST FAIL : test_check_title')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_title-%s.png' % now)
        else:
            print('TEST PASS : test_check_title')

    def test_check_quickSearch_name(self):  # Name 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # 항목명 확인 (Quick Search)
            self.assertEqual("Quick Search", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Videos'])[3]/following::label[1]").text)
            # Advanced Search 전환 버튼 확인
            self.driver.find_element_by_xpath('//*[@class="sprite-switch"]')
            # 입력필드 value 확인
            self.assertEqual("", driver.find_element_by_id("quick-search").get_attribute("value"))
            # [Search]버튼 확인
            self.assertEqual("Search", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").text)
            # [Refresh]버튼 value 확인
            self.assertEqual("", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Search'])[1]/following::button[1]").get_attribute("value"))
            # 유효한 검색어 입력 (Name) > [Search]버튼 클릭 > 검색결과 확인 (Name)
            driver.find_element_by_id("quick-search").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys("CALL ME BABY")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").click()
            self.assertEqual(u"EXO 엑소 'CALL ME BABY' MV", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::p[1]").text)
        except:
            print('TEST FAIL : test_check_quickSearch_name')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_quickSearch_name-%s.png' % now)
        else:
            print('TEST PASS : test_check_quickSearch_name')

    def test_check_quickSearch_id(self):  # ID 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # 유효한 검색어 입력 (ID) > [Search]버튼 클릭 > 검색결과 확인 (ID)
            driver.find_element_by_id("quick-search").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys("1576551212ICoH")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").click()
            self.assertEqual("1576551212ICoH", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::p[2]").text)
        except:
            print('TEST FAIL : test_check_quickSearch_id')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_quickSearch_id-%s.png' % now)
        else:
            print('TEST PASS : test_check_quickSearch_id')

    def test_check_quickSearch_jobJd(self):  # Job ID 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # 유효한 검색어 입력 (Job ID) > [Search]버튼 클릭 > 검색결과 확인 (JobID)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_id("quick-search").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys("1576550912NUDt")
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button/i").click()
            self.assertEqual("1576551212ICoH", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::p[2]").text)
        except:
            print('TEST FAIL : test_check_quickSearch_jobJd')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_quickSearch_jobJd-%s.png' % now)
        else:
            print('TEST PASS : test_check_quickSearch_jobJd')

    def test_check_quickSearch_owner(self):  # Owner 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # [List View]로 전환 > 유효한 검색어 입력 (Owner) > [Search]버튼 클릭 > 검색결과 확인 (Owner : 이선애)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_id("quick-search").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys(u"이선애")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::button[2]").click()
            self.assertEqual(u"이선애", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='-'])[1]/following::span[1]").text)
            self.assertEqual("rosa@mz.co.kr", driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='이선애'])[1]/following::small[1]").text)
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Search'])[1]/following::button[1]").click()
            # 유효한 검색어 입력 (Owner) > [Search]버튼 클릭 > 검색결과 확인 (Owner : rosa@mz.co.kr)
            driver.find_element_by_id("quick-search").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys("rosa@mz.co.kr")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::button[2]").click()
            self.assertEqual(u"이선애", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='-'])[1]/following::span[1]").text)
            self.assertEqual("rosa@mz.co.kr", driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='이선애'])[1]/following::small[1]").text)
        except:
            print('TEST FAIL : test_check_quickSearch_owner')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_quickSearch_owner-%s.png' % now)
        else:
            print('TEST PASS : test_check_quickSearch_owner')

    def test_check_quickSearch_tags(self):  # Tags 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # 유효한 검색어 입력 (Tags) > [Search]버튼 클릭 > 검색결과 확인 (Tags)
            driver.find_element_by_id("quick-search").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys(u"자동화테스트")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").click()
            self.assertEqual("1576551212ICoH", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cats12-dash'])[1]/following::small[1]").text)
        except:
            print('TEST FAIL : test_check_quickSearch_tags')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_quickSearch_tags-%s.png' % now)
        else:
            print('TEST PASS : test_check_quickSearch_tags')

    def test_check_advancedSearch_name(self):  # Name 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # [Advanced Search]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div/div/button/i").click()
            # 항목명 확인 (Advanced Search)
            self.assertEqual("Advanced Search", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Videos'])[3]/following::label[1]").text)
            # Quick Search 전환 버튼 출력 확인
            self.driver.find_element_by_xpath('//*[@class="sprite sprite-switch"]')
            # [Reset]버튼 확인
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='FLAC (bit)'])[1]/following::span[1]").click()
            # 항목명 + 입력필드 value 확인 (Name)
            self.assertEqual("Name", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Advanced Search'])[1]/following::label[1]").text)
            self.assertEqual("", driver.find_element_by_xpath("//input[@value='']").get_attribute("value"))
           # 유효한 검색어 입력 (Name) > [Search]버튼 클릭 > 검색결과 확인 (Name : CALL ME BABY)
            driver.find_element_by_xpath("//input[@value='']").click()
            driver.find_element_by_xpath("//input[@value='CALL ME BABY']").clear()
            driver.find_element_by_xpath("//input[@value='CALL ME BABY']").send_keys("CALL ME BABY")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='FLAC (bit)'])[1]/following::button[1]").click()
            self.assertEqual(u"EXO 엑소 'CALL ME BABY' MV", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='MP4'])[1]/following::p[1]").text)
        except:
            print('TEST FAIL : test_check_advancedSearch_name')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_advancedSearch_name-%s.png' % now)
        else:
            print('TEST PASS : test_check_advancedSearch_name')

    def test_check_advancedSearch_id(self):  # id 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # [Advanced Search]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div/div/button/i").click()
            # 항목명 + 입력필드 value 확인 (ID)
            self.assertEqual("ID", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Name'])[1]/following::label[1]").text)
            self.assertEqual("", driver.find_element_by_xpath("//input[@value='']").get_attribute("value"))
            # 유효한 검색어 입력 (ID) > [Search]버튼 클릭 > 검색결과 확인 (ID : 1576550945AK5a)
            driver.find_element_by_xpath("//input[@value='1576551212ICoH']").clear()
            driver.find_element_by_xpath("//input[@value='1576551212ICoH']").send_keys("1576551212ICoH")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='FLAC (bit)'])[1]/following::span[1]").click()
            self.assertEqual("1576551212ICoH", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::p[2]").text)
        except:
            print('TEST FAIL : test_check_advancedSearch_id')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_advancedSearch_id-%s.png' % now)
        else:
            print('TEST PASS : test_check_advancedSearch_id')

    def test_check_advancedSearch_owner(self):  # owner 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # [Advanced Search]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div/div/button/i").click()
            # 항목명 + 입력필드 value 확인 (Owner)
            self.assertEqual("Owner", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='ID'])[1]/following::label[1]").text)
            self.assertEqual("", driver.find_element_by_xpath("//input[@value='']").get_attribute("value"))
            # [List View] 전환 > 유효한 검색어 입력 (Owner) > [Search]버튼 클릭 > 검색결과 확인 (Owner : 이선애)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_xpath("(//input[@value=''])[3]").click()
            driver.find_element_by_xpath(u"//input[@value='이선애']").clear()
            driver.find_element_by_xpath(u"//input[@value='이선애']").send_keys(u"이선애")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='FLAC (bit)'])[1]/following::span[1]").click()
            self.assertEqual(u"이선애", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='-'])[4]/following::span[1]").text)
            self.assertEqual("rosa@mz.co.kr", driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='이선애'])[1]/following::small[1]").text)
            # [Reset]버튼 클릭
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Search'])[1]/following::button[1]").click()

            # 유효한 검색어 입력 (Owner) > [Search]버튼 클릭 > 검색결과 확인 (Owner : rosa@mz.co.kr)
            driver.find_element_by_xpath("(//input[@value=''])[4]").click()
            driver.find_element_by_xpath("//input[@value='rosa@mz.co.kr']").clear()
            driver.find_element_by_xpath("//input[@value='rosa@mz.co.kr']").send_keys("rosa@mz.co.kr")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='FLAC (bit)'])[1]/following::span[1]").click()
            self.assertEqual(u"이선애", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='-'])[4]/following::span[1]").text)
            self.assertEqual("rosa@mz.co.kr", driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='이선애'])[1]/following::small[1]").text)
        except:
            print('TEST FAIL : test_check_advancedSearch_owner')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_advancedSearch_owner-%s.png' % now)
        else:
            print('TEST PASS : test_check_advancedSearch_owner')

    def test_check_advancedSearch_description(self):  # id 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # [Advanced Search]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div/div/button/i").click()
            # 항목명 + 입력필드 value 확인 (Description)
            self.assertEqual("Description", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Owner'])[1]/following::label[1]").text)
            self.assertEqual("", driver.find_element_by_xpath("(//input[@value=''])[4]").get_attribute("value"))
            # 유효한 검색어 입력 (Description) > [Search]버튼 클릭 > 검색결과 확인 (Description : 엑소노래 )
            driver.find_element_by_xpath("(//input[@value=''])[4]").click()
            driver.find_element_by_xpath(u"//input[@value='엑소노래']").clear()
            driver.find_element_by_xpath(u"//input[@value='엑소노래']").send_keys(u"엑소노래")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='FLAC (bit)'])[1]/following::span[1]").click()
            self.assertEqual("1576551212ICoH", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::p[2]").text)
        except:
            print('TEST FAIL : test_check_advancedSearch_description')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_advancedSearch_description-%s.png' % now)
        else:
            print('TEST PASS : test_check_advancedSearch_description')

    def test_check_advancedSearch_status(self):  # status 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # [Advanced Search]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div/div/button/i").click()
            # 항목명 + 셀렉트박스 Default 선택 값 확인 (Status)
            self.assertEqual("Status", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Owner'])[1]/following::label[1]").text)
            self.assertEqual("All Status", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Status'])[1]/following::div[4]").text)
            # [List View] 전환 > Status 선택 (Inactive) > [Search]버튼 클릭 > 검색결과 확인 (Inactive)
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::button[1]").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Status'])[1]/following::div[4]").click()
            driver.find_element_by_id("react-select-13-option-2").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='FLAC (bit)'])[1]/following::span[1]").click()
            self.assertEqual("INACTIVE", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created'])[2]/following::span[2]").text)
            # [Reset]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()

            # [List View] 전환 > Status 선택 (Active) > [Search]버튼 클릭 > 검색결과 확인 (Active)
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::button[1]").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Status'])[1]/following::div[3]").click()
            driver.find_element_by_id("react-select-13-option-1").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='FLAC (bit)'])[1]/following::span[1]").click()
            self.assertEqual("ACTIVE", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Created'])[2]/following::span[2]").text)
        except:
            print('TEST FAIL : test_check_advancedSearch_status')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_advancedSearch_status-%s.png' % now)
        else:
            print('TEST PASS : test_check_advancedSearch_status')

    def test_check_advancedSearch_duration(self):  # Duration 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # [Advanced Search]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div/div/button/i").click()
            # 항목명 + 입력필드 value 확인 (Duration)
            self.assertEqual("Duration", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='All Status'])[1]/following::label[1]").text)
            self.assertEqual("__:__:__",
                             driver.find_element_by_xpath("//input[@value='__:__:__']").get_attribute("value"))
            # [List View] 전환 > 유효한 검색어 입력 (Duration : 00:03:56 ~ 00:03:56) > [Search]버튼 클릭 > 검색결과 확인 (Duration : 00:03:56)
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::button[1]").click()
            driver.find_element_by_xpath("//input[@value='__:__:__']").click()
            driver.find_element_by_xpath("//input[@value='00:03:56']").clear()
            driver.find_element_by_xpath("//input[@value='00:03:56']").send_keys("00:03:56")
            driver.find_element_by_xpath("(//input[@value='00:03:56'])[2]").clear()
            driver.find_element_by_xpath("(//input[@value='00:03:56'])[2]").send_keys("00:03:56")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='FLAC (bit)'])[1]/following::span[1]").click()
            self.assertEqual("00:03:56", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Created'])[2]/following::td[2]").text)
        except:
            print('TEST FAIL : test_check_advancedSearch_duration')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_advancedSearch_duration-%s.png' % now)
        else:
            print('TEST PASS : test_check_advancedSearch_duration')

    def test_check_advancedSearch_create(self):  # Create 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # [Advanced Search]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div/div/button/i").click()
            # 항목명 + 입력필드 value 확인 (Created)
            self.assertEqual("Created", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='~'])[1]/following::label[1]").text)
            self.assertEqual("", driver.find_element_by_id("startDate").get_attribute("value"))
            self.assertEqual("", driver.find_element_by_id("endDate").get_attribute("value"))
            # [List View] 전환 > 유효한 검색어 입력 (Created : 2019-12-17 ~ 2019-12-17) > [Search]버튼 클릭 > 검색결과 확인 (Created : 2019-12-17)
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::button[1]").click()
            driver.find_element_by_id("startDate").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='December 2019'])[1]/following::td[17]").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='December 2019'])[1]/following::td[17]").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='FLAC (bit)'])[1]/following::span[1]").click()
            self.assertEqual("1576551212ICoH", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::p[2]").text)
        except:
            print('TEST FAIL : test_check_advancedSearch_create')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_advancedSearch_create-%s.png' % now)
        else:
            print('TEST PASS : test_check_advancedSearch_create')

    def test_check_advancedSearch_categories(self):  # Categories 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # [Advanced Search]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div/div/button/i").click()
            # 항목명 + 입력필드 value 확인 (Categories)
            self.assertEqual("Categories", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created'])[1]/following::label[1]").text)
            self.assertEqual("Select category", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Categories'])[1]/following::span[1]").text)
            self.assertEqual("", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Select category'])[1]/following::button[2]").get_attribute(
                "value"))
            # [List View] 전환 > Categories 선택 (YG) > [Search]버튼 클릭 > 검색결과 확인 (YG)
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::button[1]").click()
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div/div[2]/div[3]/div/div/div/div/div[3]/button/i").click()
            time.sleep(5)
            driver.find_element_by_xpath("//input[@type='checkbox']").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::span[1]").click()
            self.assertEqual("YG", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='ACTIVE'])[1]/following::td[1]").text)
        except:
            print('TEST FAIL : test_check_advancedSearch_categories')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_advancedSearch_categories-%s.png' % now)
        else:
            print('TEST PASS : test_check_advancedSearch_categories')

    def test_check_advancedSearch_tags(self):  # Tags 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # [Advanced Search]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div/div/button/i").click()
            # 항목명 + 셀렉트박스 Default 선택 값 확인 (Tags)
            self.assertEqual("Tags", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Select category'])[1]/following::label[1]").text)
            self.assertEqual("", driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div/div[2]/div[3]/div[2]/div/div/div/div/textarea").get_attribute(
                "value"))
            ''' Tag 입력 후 엔터키 적용이 관건이당
            # 유효한 검색어 입력 (Tags) > [Search]버튼 클릭 > 검색결과 확인 (Tags : 자동화테스트)
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='FLAC (bit)'])[1]/following::span[1]").click()
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='자동화테스트'])[1]/following::span[1]").click()
            self.assertEqual("1576551212ICoH", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::p[2]").text)
            '''
        except:
            print('TEST FAIL : test_check_advancedSearch_tags')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_advancedSearch_tags-%s.png' % now)
        else:
            print('TEST PASS : test_check_advancedSearch_tags')

    def test_check_advancedSearch_custom(self):  # Custom Field 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # [Advanced Search]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div/div/button/i").click()
            # 항목명 + 입력필드 value 확인 (앨범)
            self.assertEqual(u"앨범", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::strong[1]").text)
            self.assertEqual("", driver.find_element_by_xpath("(//input[@value=''])[10]").get_attribute("value"))
           # 유효한 검색어 입력 (앨범) > [Search]버튼 클릭 > 검색결과 확인 (앨범 : The 2nd Album 'EXODUS' -> EXODUS)
            driver.find_element_by_xpath("//input[@value='EXODUS']").clear()
            driver.find_element_by_xpath("//input[@value='EXODUS']").send_keys("EXODUS")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='FLAC (bit)'])[1]/following::span[1]").click()
            self.assertEqual(u"EXO 엑소 'CALL ME BABY' MV", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='MP4'])[1]/following::p[1]").text)
        except:
            print('TEST FAIL : test_check_advancedSearch_custom')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_advancedSearch_custom-%s.png' % now)
        else:
            print('TEST PASS : test_check_advancedSearch_custom')

    def test_check_count(self):  # Video Count 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # 유효한 검색어 입력 (ID) > [Search]버튼 클릭 > 검색결과 확인 (count : 1)
            driver.find_element_by_id("quick-search").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys("1576551212ICoH")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").click()
            self.assertEqual("1", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Total'])[1]/following::span[1]").text)
        except:
            print('TEST FAIL : test_check_count')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_count-%s.png' % now)
        else:
            print('TEST PASS : test_check_count')

    '''
    def test_check_paging(self):  # Paging 기능 확인 -> 어떻게 확인하면 좋을지 생각필요
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # 유효한 검색어 입력 (ID) > [Search]버튼 클릭 > 검색결과 확인 (ID)

        except:
            print('TEST FAIL : test_check_paging')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_paging-%s.png' % now)
        else:
            print('TEST PASS : test_check_paging')
    '''

    def test_check_listView(self):  # ID 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # List View 전환
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            # 유효한 검색어 입력 (ID) > [Search]버튼 클릭
            driver.find_element_by_id("quick-search").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys("1576551212ICoH")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").click()
            # 컬럼 및 데이터 확인 (Videos)
            self.assertEqual("Videos", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::th[1]").text)
            # 썸네일 체크 방법이 없다 (이미지로 체크해야할듯)
            self.assertEqual("EXO 엑소 'CALL ME BABY' MV", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created'])[2]/following::span[1]").text)
            self.assertEqual("1576551212ICoH", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created'])[2]/following::small[1]").text)
            # 컬럼 및 데이터 확인 (Duration)
            self.assertEqual("Duration", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Videos'])[4]/following::th[1]").text)
            self.assertEqual("00:03:56", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created'])[2]/following::td[2]").text)
            # 컬럼 및 데이터 확인 (Status)
            self.assertEqual("Status", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Duration'])[2]/following::th[1]").text)
            self.assertEqual("ACTIVE", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created'])[2]/following::span[2]").text)
            # 컬럼 및 데이터 확인 (Category)
            self.assertEqual("Category", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Status'])[2]/following::th[1]").text)
            self.assertEqual("세훈, 찬열", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='ACTIVE'])[1]/following::td[1]").text)
            # 컬럼 및 데이터 확인 (Owner)
            self.assertEqual("Owner", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Category'])[1]/following::th[1]").text)
            self.assertEqual("이선애", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='-'])[3]/following::span[1]").text)
            self.assertEqual("rosa@mz.co.kr", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Megazone (Owner)'])[1]/following::small[1]").text)
            # 컬럼 및 데이터 확인 (Created)
            self.assertEqual("Created", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Owner'])[2]/following::th[1]").text)
            self.assertEqual("2019-12-17 11:53:32", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='mcmtestowner@gmail.com'])[1]/following::time[1]").text)
        except:
            print('TEST FAIL : test_check_listView')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_listView-%s.png' % now)
        else:
            print('TEST PASS : test_check_listView')

    def test_check_thumbnailView(self):  # ID 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # Thumbnail View 전환
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button[2]/i").click()
            # 유효한 검색어 입력 (ID) > [Search]버튼 클릭 > 검색결과 확인 (ID)
            driver.find_element_by_id("quick-search").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys("1576551212ICoH")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").click()
            # 컬럼 및 데이터 확인 (Videos)
            self.assertEqual("Videos", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::th[1]").text)
            # 썸네일 체크 방법이 없다 (이미지로 체크해야할듯)
            #
            # 데이터 확인 (Name)
            self.assertEqual("EXO 엑소 'CALL ME BABY' MV", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::p[1]").text)
            # 데이터 확인 (ID)
            self.assertEqual("1576551212ICoH", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::p[2]").text)
        except:
            print('TEST FAIL : test_check_thumbnailView')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_thumbnailView-%s.png' % now)
        else:
            print('TEST PASS : test_check_thumbnailView')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Videos('test_check_breadcrumb'))
    suite.addTest(Videos("test_check_title"))
    suite.addTest((Videos("test_check_quickSearch_name")))
    suite.addTest((Videos("test_check_quickSearch_id")))
    suite.addTest((Videos("test_check_quickSearch_jonId")))
    suite.addTest((Videos("test_check_quickSearch_owner")))
    suite.addTest((Videos("test_check_quickSearch_tags")))
    suite.addTest((Videos("test_check_advancedSearch_name")))
    suite.addTest((Videos("test_check_advancedSearch_id")))
    suite.addTest((Videos("test_check_advancedSearch_owner")))
    suite.addTest((Videos("test_check_advancedSearch_description")))
    suite.addTest((Videos("test_check_advancedSearch_status")))
    suite.addTest((Videos("test_check_advancedSearch_duration")))
    suite.addTest((Videos("test_check_advancedSearch_create")))
    suite.addTest((Videos("test_check_advancedSearch_categories")))
    suite.addTest((Videos("test_check_advancedSearch_tags")))
    suite.addTest((Videos("test_check_advancedSearch_custom")))
    suite.addTest((Videos("test_check_count")))
    suite.addTest((Videos("test_check_paging")))
    suite.addTest((Videos("test_check_listView")))
    suite.addTest((Videos("test_check_thumbnailView")))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())