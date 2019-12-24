# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class Assets(unittest.TestCase):

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
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            time.sleep(3)
            # Bread Crumb 확인 (Contents > Assets)
            self.assertEqual("Contents", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Assets'])[2]/following::li[1]").text)
            self.assertEqual("Assets", driver.find_element_by_xpath(
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
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            time.sleep(3)
            # Title 확인 (Assets)
            self.assertEqual("Assets", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::h3[1]").text)
        except:
            print('TEST FAIL : test_check_title')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_title-%s.png' % now)
        else:
            print('TEST PASS : test_check_title')

    def test_check_btn_createAssets(self):  # Name 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            time.sleep(3)
            # [Create Assets]버튼 확인
            self.assertEqual("+ Create Assets", driver.find_element_by_link_text("+ Create Assets").text)
            # [Create Assets]버튼 클릭
            driver.find_element_by_link_text("+ Create Assets").click()
            # Create Assets 페이지로 이동 확인 (Title 체크)
            self.assertEqual("Create Assets", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::h3[1]").text)
        except:
            print('TEST FAIL : test_check_btn_createAssets')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_btn_createAssets-%s.png' % now)
        else:
            print('TEST PASS : test_check_btn_createAssets')

    def test_check_quickSearch_name(self):  # Name 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            time.sleep(3)
            # 항목명 확인 (Quick Search)
            self.assertEqual("Quick Search", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='+ Create Assets'])[1]/following::label[1]").text)
            # Advanced Search 전환 버튼 확인
            self.driver.find_element_by_xpath('//*[@class="sprite sprite-switch"]')
            # 입력필드 value 확인
            self.assertEqual("", driver.find_element_by_id("quick-search").get_attribute("value"))
            # [Search]버튼 확인
            self.assertEqual("Search", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").text)
            # [Refresh]버튼 value 확인
            self.assertEqual("", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Search'])[1]/following::button[1]").get_attribute(
                "value"))
            # 유효한 검색어 입력 (Name) > [Search]버튼 클릭 > 검색결과 확인 (Name)
            driver.find_element_by_id("quick-search").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys("CALL ME BABY")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").click()
            self.assertEqual(u"EXO 엑소 'CALL ME BABY' MV", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='MP4'])[1]/following::p[1]").text)
        except:
            print('TEST FAIL : test_check_quickSearch_name')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_quickSearch_name-%s.png' % now)
        else:
            print('TEST PASS : test_check_quickSearch_name')

    def test_check_quickSearch_id(self):  # Name 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            time.sleep(3)
            # 유효한 검색어 입력 (ID) > [Search]버튼 클릭 > 검색결과 확인 (ID)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Download Apps'])[1]/following::div[1]").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys("1576550945AK5a")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").click()
            self.assertEqual("1576550945AK5a", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='MP4'])[1]/following::p[2]").text)
        except:
            print('TEST FAIL : test_check_quickSearch_id')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_quickSearch_id-%s.png' % now)
        else:
            print('TEST PASS : test_check_quickSearch_id')

    def test_check_quickSearch_jobJd(self):  # Name 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            time.sleep(3)
            # 유효한 검색어 입력 (Job ID) > [Search]버튼 클릭 > 검색결과 확인 (JobID)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::div[2]").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys("1576550912NUDt")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").click()
            self.assertEqual("1576550945AK5a", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='MP4'])[1]/following::p[2]").text)
            # 유효한 검색어 입력 (Owner) > [Search]버튼 클릭 > 검색결과 확인 (Owner)
            # 추후에 자동화 테스트용 계정을 생성해서 그 아이만 조회되도록 해야할 것 같음
            # 유효한 검색어 입력 (Tags) > [Search]버튼 클릭 > 검색결과 확인 (Tags)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='+ Create Assets'])[1]/following::div[2]").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys(u"자동화테스트")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").click()
            self.assertEqual("1576550945AK5a", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='MP4'])[1]/following::p[2]").text)
        except:
            print('TEST FAIL : test_check_quickSearch_jobJd')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_quickSearch_jobJd-%s.png' % now)
        else:
            print('TEST PASS : test_check_quickSearch_jobJd')

    def test_check_quickSearch_owner(self):  # Name 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            time.sleep(3)
            # 유효한 검색어 입력 (Owner) > [Search]버튼 클릭 > 검색결과 확인 (Owner)
            # 추후에 자동화 테스트용 계정을 생성해서 그 아이만 조회되도록 해야할 것 같음
            # 유효한 검색어 입력 (Tags) > [Search]버튼 클릭 > 검색결과 확인 (Tags)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='+ Create Assets'])[1]/following::div[2]").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys(u"자동화테스트")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").click()
            self.assertEqual("1576550945AK5a", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='MP4'])[1]/following::p[2]").text)
        except:
            print('TEST FAIL : test_check_quickSearch_owner')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_quickSearch_owner-%s.png' % now)
        else:
            print('TEST PASS : test_check_quickSearch_owner')

    def test_check_quickSearch_tags(self):  # Name 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            time.sleep(3)
            # 유효한 검색어 입력 (Tags) > [Search]버튼 클릭 > 검색결과 확인 (Tags)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='+ Create Assets'])[1]/following::div[2]").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys(u"자동화테스트")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").click()
            self.assertEqual("1576550945AK5a", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='MP4'])[1]/following::p[2]").text)
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
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            time.sleep(3)
            # [Advanced Search]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div/div/button/i").click()
            # 항목명 확인 (Advanced Search)
            self.assertEqual("Advanced Search", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='+ Create Assets'])[1]/following::label[1]").text)
            # Quick Search 전환 버튼 출력 확인
            self.driver.find_element_by_xpath('//*[@class="sprite sprite-switch"]')
            # [Refresh]버튼 확인
            self.assertEqual("", driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div/textarea").get_attribute(
                "value"))
            # 항목명 + 입력필드 value 확인 (Name)
            self.assertEqual("Name", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Advanced Search'])[1]/following::label[1]").text)
           # 유효한 검색어 입력 (Name) > [Search]버튼 클릭 > 검색결과 확인 (Name : CALL ME BABY)
            driver.find_element_by_xpath("//input[@value='']").click()
            driver.find_element_by_xpath("//input[@value='CALL ME BABY']").clear()
            driver.find_element_by_xpath("//input[@value='CALL ME BABY']").send_keys("CALL ME BABY")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::button[1]").click()
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
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            time.sleep(3)
            # [Advanced Search]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div/div/button/i").click()
            # 항목명 + 입력필드 value 확인 (ID)
            self.assertEqual("ID", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Name'])[1]/following::label[1]").text)
            self.assertEqual("", driver.find_element_by_xpath("(//input[@value=''])[2]").get_attribute("value"))
            # 유효한 검색어 입력 (ID) > [Search]버튼 클릭 > 검색결과 확인 (ID : 1576550945AK5a)
            driver.find_element_by_xpath("(//input[@value=''])[2]").click()
            driver.find_element_by_xpath("//input[@value='1576550945AK5a']").clear()
            driver.find_element_by_xpath("//input[@value='1576550945AK5a']").send_keys("1576550945AK5a")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::span[1]").click()
            self.assertEqual("1576550945AK5a", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='MP4'])[1]/following::p[2]").text)
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()
        except:
            print('TEST FAIL : test_check_advancedSearch_id')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_advancedSearch_id-%s.png' % now)
        else:
            print('TEST PASS : test_check_advancedSearch_id')

    def test_check_advancedSearch_jobId(self):  # Jon ID 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            time.sleep(3)
            # [Advanced Search]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div/div/button/i").click()
            # 항목명 + 입력필드 value 확인 (Job ID)
            self.assertEqual("Job Id", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='ID'])[1]/following::label[1]").text)
            self.assertEqual("", driver.find_element_by_xpath("(//input[@value=''])[3]").get_attribute("value"))
            # 유효한 검색어 입력 (ID) > [Search]버튼 클릭 > 검색결과 확인 (ID : 1576550945AK5a)
            driver.find_element_by_xpath("(//input[@value=''])[2]").click()
            driver.find_element_by_xpath("//input[@value='1576550945AK5a']").clear()
            driver.find_element_by_xpath("//input[@value='1576550945AK5a']").send_keys("1576550945AK5a")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::span[1]").click()
            self.assertEqual("1576550945AK5a", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='MP4'])[1]/following::p[2]").text)
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()
        except:
            print('TEST FAIL : test_check_advancedSearch_jobId')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_advancedSearch_jobId-%s.png' % now)
        else:
            print('TEST PASS : test_check_advancedSearch_jobId')

    def test_check_advancedSearch_owner(self):  # owner 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            time.sleep(3)
            # [Advanced Search]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div/div/button/i").click()
            # 항목명 + 입력필드 value 확인 (Owner)
            self.assertEqual("Owner", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Job Id'])[1]/following::label[1]").text)
            self.assertEqual("", driver.find_element_by_xpath("(//input[@value=''])[4]").get_attribute("value"))
            # [List View] 전환 > 유효한 검색어 입력 (Owner) > [Search]버튼 클릭 > 검색결과 확인 (Owner : 이선애)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_xpath("(//input[@value=''])[4]").click()
            driver.find_element_by_xpath(u"//input[@value='이선애']").clear()
            driver.find_element_by_xpath(u"//input[@value='이선애']").send_keys(u"이선애")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::span[1]").click()
            self.assertEqual(u"이선애", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='-'])[3]/following::span[1]").text)
            self.assertEqual("rosa@mz.co.kr", driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='이선애'])[1]/following::small[1]").text)
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()
            # [List View] 전환 > 유효한 검색어 입력 (Owner) > [Search]버튼 클릭 > 검색결과 확인 (Owner : rosa@mz.co.kr)
            driver.find_element_by_xpath("(//input[@value=''])[4]").click()
            driver.find_element_by_xpath("//input[@value='rosa@mz.co.kr']").clear()
            driver.find_element_by_xpath("//input[@value='rosa@mz.co.kr']").send_keys("rosa@mz.co.kr")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::span[1]").click()
            self.assertEqual(u"이선애", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='-'])[3]/following::span[1]").text)
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

    def test_check_advancedSearch_status(self):  # status 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            time.sleep(3)
            # [Advanced Search]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div/div/button/i").click()
            # 항목명 + 셀렉트박스 Default 선택 값 확인 (Status)
            self.assertEqual("Status", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Owner'])[1]/following::label[1]").text)
            self.assertEqual("All Status", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Status'])[1]/following::div[4]").text)
            # [List View] 전환 > Status 선택 (Inactive) > [Search]버튼 클릭 > 검색결과 확인 (Inactive)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Status'])[1]/following::div[3]").click()
            driver.find_element_by_id("react-select-14-option-2").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::span[1]").click()
            self.assertEqual("INACTIVE", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='-'])[2]/following::span[1]").text)
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()

            # [List View] 전환 > Status 선택 (Active) > [Search]버튼 클릭 > 검색결과 확인 (Active)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Status'])[1]/following::div[3]").click()
            driver.find_element_by_id("react-select-14-option-1").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::span[1]").click()
            self.assertEqual("ACTIVE", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='-'])[2]/following::span[1]").text)
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()
        except:
            print('TEST FAIL : test_check_advancedSearch_status')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_advancedSearch_status-%s.png' % now)
        else:
            print('TEST PASS : test_check_advancedSearch_status')

    def test_check_advancedSearch_mediaType(self):  # Media Type 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            time.sleep(3)
            # [Advanced Search]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div/div/button/i").click()
            # 항목명 + 셀렉트박스 Default 선택 값 확인 (Media Type)
            self.assertEqual("Media Type", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='All Ingest Type'])[1]/following::label[1]").text)
            self.assertEqual("All Ingest Type", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Ingest Type'])[1]/following::div[4]").text)
            # [List View] 전환 > Media Type 선택 (Video) > [Search]버튼 클릭 > 검색결과 확인 (VIDEO))
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Media Type'])[1]/following::div[3]").click()
            driver.find_element_by_id("react-select-16-option-1").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::span[1]").click()
            self.assertEqual("VIDEO", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created'])[2]/following::td[2]").text)
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()

            # [List View] 전환 > Media Type 선택 (Audio) > [Search]버튼 클릭 > 검색결과 확인 (AUDIO))
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Media Type'])[1]/following::div[3]").click()
            driver.find_element_by_id("react-select-16-option-2").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::span[1]").click()
            self.assertEqual("AUDIO", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Create Assets MP3'])[1]/following::td[1]").text)
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()

            # [List View] 전환 > Media Type 선택 (Image) > [Search]버튼 클릭 > 검색결과 확인 (IMAGE))
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Media Type'])[1]/following::div[4]").click()
            driver.find_element_by_id("react-select-16-option-3").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::button[1]").click()
            self.assertEqual("IMAGE", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created'])[2]/following::td[2]").text)
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()

            # [List View] 전환 > Media Type 선택 (Text) > [Search]버튼 클릭 > 검색결과 확인 (TEXT))
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Media Type'])[1]/following::div[4]").click()
            driver.find_element_by_id("react-select-16-option-4").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::span[1]").click()
            self.assertEqual("TEXT", driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='일본어 자막'])[1]/following::td[1]").text)
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()
        except:
            print('TEST FAIL : test_check_advancedSearch_mediaType')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_advancedSearch_mediaType-%s.png' % now)
        else:
            print('TEST PASS : test_check_advancedSearch_mediaType')

    def test_check_advancedSearch_ingestType(self):  # Ingest Type 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            time.sleep(3)
            # [Advanced Search]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div/div/button/i").click()
            # 항목명 + 셀렉트박스 Default 선택 값 확인 (Ingest Type)
            self.assertEqual("Ingest Type", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='All Status'])[1]/following::label[1]").text)
            self.assertEqual("All Media Types", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Media Type'])[1]/following::div[3]").text)
            # [List View] 전환 > Ingest Type 선택 (Transcoded) > [Search]버튼 클릭 > 검색결과 확인 (TRANSCODED))
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Ingest Type'])[1]/following::div[4]").click()
            driver.find_element_by_id("react-select-15-option-1").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::span[1]").click()
            self.assertEqual("TRANSCODED", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='THUMBNAILS'])[1]/following::td[1]").text)
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()

            # [List View] 전환 > Ingest Type 선택 (Direct) > [Search]버튼 클릭 > 검색결과 확인 (DIRECT))
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Ingest Type'])[1]/following::div[3]").click()
            driver.find_element_by_id("react-select-15-option-2").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::button[1]").click()
            self.assertEqual("DIRECT", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='MP4'])[1]/following::td[1]").text)
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()

            # [List View] 전환 > Ingest Type 선택 (Remote) > [Search]버튼 클릭 > 검색결과 확인 (REMOTE))
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Ingest Type'])[1]/following::div[3]").click()
            driver.find_element_by_id("react-select-15-option-3").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::span[1]").click()
            self.assertEqual("REMOTE", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='IMAGE'])[2]/following::td[1]").text)
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()

            # [List View] 전환 > Ingest Type 선택 (Remote) > [Search]버튼 클릭 > 검색결과 확인 (REMOTE)) -> 현재 제공하지 않으므로 검색결과 부재시 안내문구 출력 (Empty Asset List.)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Ingest Type'])[1]/following::div[3]").click()
            driver.find_element_by_id("react-select-21-option-4").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::span[1]").click()
            self.assertEqual("Empty Asset List.", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created'])[2]/following::td[1]").text)
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()
        except:
            print('TEST FAIL : test_check_advancedSearch_ingestType')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_advancedSearch_ingestType-%s.png' % now)
        else:
            print('TEST PASS : test_check_advancedSearch_ingestType')

    def test_check_advancedSearch_type(self):  # Type 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            time.sleep(3)
            # [Advanced Search]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div/div/button/i").click()
            # 항목명 + 셀렉트박스 Default 선택 값 확인 (Type)
            self.assertEqual("Type", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='All Media Types'])[1]/following::label[1]").text)
            self.assertEqual("All Types", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Type'])[1]/following::div[4]").text)
            # [List View] 전환 > Type 선택 (MP4) > [Search]버튼 클릭 > 검색결과 확인 (MP4)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Type'])[1]/following::div[4]").click()
            driver.find_element_by_id("react-select-23-option-1").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::span[1]").click()
            self.assertEqual("MP4", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='VIDEO'])[1]/following::td[1]").text)
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()

            # [List View] 전환 > Type 선택 (HLS) > [Search]버튼 클릭 > 검색결과 확인 (HLS)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Type'])[1]/following::div[4]").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='All Types'])[1]/following::div[7]").click()
            driver.find_element_by_id("react-select-23-option-2").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::span[1]").click()
            self.assertEqual("HLS", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='VIDEO'])[1]/following::td[1]").text)
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()

            # [List View] 전환 > Type 선택 (DASH) > [Search]버튼 클릭 > 검색결과 확인 (DASH)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Type'])[1]/following::div[4]").click()
            driver.find_element_by_id("react-select-23-option-3").click()
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button/i").click()
            self.assertEqual("DASH", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='VIDEO'])[1]/following::td[1]").text)
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()

            # [List View] 전환 > Type 선택 (MP3) > [Search]버튼 클릭 > 검색결과 확인 (MP3)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Type'])[1]/following::div[4]").click()
            driver.find_element_by_id("react-select-23-option-4").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::span[1]").click()
            self.assertEqual("MP3", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='AUDIO'])[1]/following::td[1]").text)
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()

            # [List View] 전환 > Type 선택 (THUMBNAILS) > [Search]버튼 클릭 > 검색결과 확인 (THUMBNAILS)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Type'])[1]/following::div[4]").click()
            driver.find_element_by_id("react-select-23-option-5").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::button[1]").click()
            self.assertEqual("THUMBNAILS", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='IMAGE'])[1]/following::td[1]").text)
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()

            # [List View] 전환 > Type 선택 (IMAGE) > [Search]버튼 클릭 > 검색결과 확인 (IMAGE)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Type'])[1]/following::div[3]").click()
            driver.find_element_by_id("react-select-23-option-6").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::span[1]").click()
            self.assertEqual("IMAGE", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='IMAGE'])[2]/following::td[1]").text)
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()

            # [List View] 전환 > Type 선택 (THUMBNAILS) > [Search]버튼 클릭 > 검색결과 확인 (THUMBNAILS)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Type'])[1]/following::div[4]").click()
            driver.find_element_by_id("react-select-23-option-5").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::button[1]").click()
            self.assertEqual("THUMBNAILS", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='IMAGE'])[1]/following::td[1]").text)
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()

            # [List View] 전환 > Type 선택 (CAPTION) > [Search]버튼 클릭 > 검색결과 확인 (CAPTION)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Type'])[1]/following::div[4]").click()
            driver.find_element_by_id("react-select-23-option-7").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::span[1]").click()
            self.assertEqual("CAPTION", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='TEXT'])[1]/following::td[1]").text)
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()
        except:
            print('TEST FAIL : test_check_advancedSearch_type')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_advancedSearch_type-%s.png' % now)
        else:
            print('TEST PASS : test_check_advancedSearch_type')

    def test_check_advancedSearch_duration(self):  # Duration 검색기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            time.sleep(3)
            # [Advanced Search]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div/div/button/i").click()
            # 항목명 + 입력필드 value 확인 (Duration)
            self.assertEqual("Duration", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='All Types'])[1]/following::label[1]").text)
            self.assertEqual("__:__:__",
                             driver.find_element_by_xpath("//input[@value='__:__:__']").get_attribute("value"))
            # [List View] 전환 > 유효한 검색어 입력 (Duration : 00:03:56 ~ 00:03:56) > [Search]버튼 클릭 > 검색결과 확인 (Duration : 00:03:56)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_xpath("//input[@value='__:__:__']").click()
            driver.find_element_by_xpath("//input[@value='00:03:56']").clear()
            driver.find_element_by_xpath("//input[@value='00:03:56']").send_keys("00:03:56")
            driver.find_element_by_xpath("(//input[@value='00:03:56'])[2]").clear()
            driver.find_element_by_xpath("(//input[@value='00:03:56'])[2]").send_keys("00:03:56")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::button[1]").click()
            self.assertEqual("00:03:56", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='DIRECT'])[1]/following::td[1]").text)
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
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            time.sleep(3)
            # [Advanced Search]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div/div/button/i").click()
            # 항목명 + 입력필드 value 확인 (Created)
            self.assertEqual("Categories", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created'])[1]/following::label[1]").text)
            self.assertEqual("Select category", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Categories'])[1]/following::span[1]").text)
            ''' Create 검색 Defect으로 확인불가
            # [List View] 전환 > 유효한 검색어 입력 (Created : 2019-12-17 ~ 2019-12-17) > [Search]버튼 클릭 > 검색결과 확인 (Created : 2019-12-17)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_id("startDate").click()
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='December 2019'])[1]/following::td[17]").click()
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='December 2019'])[1]/following::td[17]").click()
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::button[1]").click()
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()
            '''
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
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            time.sleep(3)
            # [Advanced Search]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div/div/button/i").click()
            # 항목명 + 입력필드 value 확인 (Categories)
            self.assertEqual("Created", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='~'])[1]/following::label[1]").text)
            self.assertEqual("", driver.find_element_by_id("startDate").get_attribute("value"))
            self.assertEqual("", driver.find_element_by_id("endDate").get_attribute("value"))
            # [List View] 전환 > Categories 선택 (YG) > [Search]버튼 클릭 > 검색결과 확인 (YG)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div[2]/div[2]/button/i").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Select category'])[1]/following::button[2]").click()
            time.sleep(5)
            driver.find_element_by_xpath("//input[@type='checkbox']").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::span[1]").click()
            self.assertEqual("YG", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='ACTIVE'])[1]/following::td[1]").text)
            # [Refresh]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div[2]/div/button[2]/i").click()
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
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            time.sleep(3)
            # [Advanced Search]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/form/div/div/div/button/i").click()
            # 항목명 + 셀렉트박스 Default 선택 값 확인 (Tags)
            self.assertEqual("Tags", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Select category'])[1]/following::label[1]").text)
            self.assertEqual("", driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/form/div/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div/textarea").get_attribute(
                "value"))
            ''' Tag 입력 후 엔터키 적용이 관건이당
            # 유효한 검색어 입력 (Tags) > [Search]버튼 클릭 > 검색결과 확인 (Tags : 자동화테스트)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::textarea[1]").clear()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::textarea[1]").send_keys(
                u"자동화테스트")
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='자동화테스트'])[1]/following::span[1]").click()
            # 
            '''
        except:
            print('TEST FAIL : test_check_advancedSearch_tags')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_advancedSearch_tags-%s.png' % now)
        else:
            print('TEST PASS : test_check_advancedSearch_tags')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    #suite.addTest(Assets('test_check_breadcrumb'))
    #suite.addTest(Assets("test_check_title"))
    #suite.addTest((Assets("test_check_btn_createAssets")))
    suite.addTest((Assets("test_check_quickSearch_name")))
    suite.addTest((Assets("test_check_quickSearch_id")))
    suite.addTest((Assets("test_check_quickSearch_jonId")))
    suite.addTest((Assets("test_check_quickSearch_owner")))
    suite.addTest((Assets("test_check_quickSearch_tags")))
    suite.addTest((Assets("test_check_advancedSearch_name")))
    suite.addTest((Assets("test_check_advancedSearch_id")))
    suite.addTest((Assets("test_check_advancedSearch_jobId")))
    suite.addTest((Assets("test_check_advancedSearch_owner")))
    suite.addTest((Assets("test_check_advancedSearch_status")))
    suite.addTest((Assets("test_check_advancedSearch_mediaType")))
    suite.addTest((Assets("test_check_advancedSearch_ingestType")))
    suite.addTest((Assets("test_check_advancedSearch_type")))
    suite.addTest((Assets("test_check_advancedSearch_duration")))
    suite.addTest((Assets("test_check_advancedSearch_create")))
    suite.addTest((Assets("test_check_advancedSearch_categories")))
    suite.addTest((Assets("test_check_advancedSearch_tags")))
    #suite.addTest((Assets("test_check_attributions")))
    #suite.addTest((Assets("test_check_tags")))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())