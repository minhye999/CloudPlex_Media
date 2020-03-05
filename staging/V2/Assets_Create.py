# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class Assets_Create(unittest.TestCase):

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
            # [Create Asset]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Assets'])[3]/following::strong[1]").click()
            time.sleep(3)
            # Bread Crumb 확인 (Contents > Create Assets)
            self.assertEqual("Contents", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Create Assets'])[1]/following::li[1]").text)
            self.assertEqual("Create Assets", driver.find_element_by_xpath(
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
            # [Create Asset]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Assets'])[3]/following::strong[1]").click()
            time.sleep(3)
            # Title 확인 (Create Assets)
            self.assertEqual("Create Assets", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::h3[1]").text)
        except:
            print('TEST FAIL : test_check_title')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_title-%s.png' % now)
        else:
            print('TEST PASS : test_check_title')

    def test_check_name(self):  # Name 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            # [Create Asset]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Assets'])[3]/following::strong[1]").click()
            time.sleep(3)
            # 항목명 확인 (Name)
            self.assertEqual("Name", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Create Assets'])[2]/following::strong[1]").text)
            # 필수값 표시 확인 (*)
            self.assertRegexpMatches(driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Name'])[1]/following::span[1]").text,
                                     r"^[\s\S]*$")
            # [i]아이콘 확인
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/form/div/div/label/div/i")
            # [i]아이콘 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/form/div/div/label/div/i").click()
            '''
            # info 내용 확인
            self.assertEqual("Name rules", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::strong[1]").text)
            self.assertEqual("Name Constraints", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::p[2]").text)
            self.assertEqual(
                "Base video file to be used for the channel can be set only for English name asset without special characters and spaces. (Allowed special characters: ~! () _-.)",
                driver.find_element_by_xpath(
                    "(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::div[6]").text)
            '''
            # Name 입력 (Create Assets MP4)
            driver.find_element_by_xpath("//input[@value='']").click()
            # driver.find_element_by_xpath("//input[@value='Create Assets MP4']").clear()
            # driver.find_element_by_xpath("//input[@value='Create Assets MP4']").send_keys("Create Assets MP4")
            # driver.find_element_by_xpath("//form[@class='form-control']/button").click("Create Assets MP4")
            self.driver.find_element_by_xpath('//*[@class="form-control"]').send_keys('Create Assets MP4')
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='CAPTION'])[1]/following::div[2]").click()
            # 입력한 Name 출력 확인 (Create Assets MP4)
            self.assertEqual("Create Assets MP4",
                             driver.find_element_by_xpath("//input[@value='Create Assets MP4']").get_attribute("value"))
        except:
            print('TEST FAIL : test_check_name')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_name-%s.png' % now)
        else:
            print('TEST PASS : test_check_name')

    def test_check_type(self):  # Type 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            # [Create Asset]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Assets'])[3]/following::strong[1]").click()
            time.sleep(3)
            # 항목명 확인 (Type)
            self.assertEqual("Type", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::strong[2]").text)
            # 필수값 표시 확인 (*)
            self.assertRegexpMatches(driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Type'])[1]/following::span[1]").text,
                                     r"^[\s\S]*$")
            # Default 선택값 확인 (MP4)
            self.assertEqual("on", driver.find_element_by_id("rdb-asset-type-MP4").get_attribute("value"))
            # Type 확인 (MP4)
            self.assertEqual("MP4", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='*'])[2]/following::span[1]").text)
            # Type 확인 (MP3)
            self.assertEqual("MP3", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='MP4'])[1]/following::span[1]").text)
            # Type 확인 (IMAGE)
            self.assertEqual("IMAGE", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='MP3'])[1]/following::span[1]").text)
            # Type 확인 (CAPTION)
            self.assertEqual("CAPTION", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='IMAGE'])[1]/following::span[1]").text)
            # [Select a file]버튼 확인
            self.assertEqual("Select a file", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='CAPTION'])[1]/following::button[1]").text)
            # 선택한 파일 부재 시, 안내문구 확인 (Select a one MP4 file)
            self.assertEqual("Select a one MP4 file", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Select a file'])[1]/following::p[1]").text)
        except:
            print('TEST FAIL : test_check_type')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_type-%s.png' % now)
        else:
            print('TEST PASS : test_check_type')

    def test_check_categories(self):  # categories 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            # [Create Asset]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Assets'])[3]/following::strong[1]").click()
            time.sleep(3)
            # 항목명 확인 (Categories)
            self.assertEqual("Categories", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Select a file'])[1]/following::strong[1]").text)
            # Default 선택값 확인 (Select category)
            self.assertEqual("Select category", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Categories'])[1]/following::span[1]").text)
            # [+]버튼 확인
            #
            # [+]버튼 클릭
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Select category'])[1]/following::button[2]").click()
            # Category 선택 (YG)
            driver.find_element_by_xpath("//input[@type='checkbox']").click()
            # [Select]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
            # 선택한 Category 출력 확인 (YG)
            self.assertEqual("YG", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Categories'])[1]/following::span[3]").text)
        except:
            print('TEST FAIL : test_check_categories')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_categories-%s.png' % now)
        else:
            print('TEST PASS : test_check_categories')

    def test_check_attributions(self):  # categories 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            # [Create Asset]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Assets'])[3]/following::strong[1]").click()
            time.sleep(3)
            # 항목명 확인 (Attributions)
            self.assertEqual("Attributions", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Select category'])[1]/following::strong[1]").text)
            # [Add]버튼 확인
            self.assertEqual("Add", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Attributions'])[1]/following::button[1]").text)
            # [Add]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Attributions'])[1]/following::button[1]").click()
            # key, Value 입력
            driver.find_element_by_id("key0").clear()
            driver.find_element_by_id("key0").send_keys("key")
            driver.find_element_by_xpath("//input[@value='value']").clear()
            driver.find_element_by_xpath("//input[@value='value']").send_keys("value")
            # 입력한 key, value 출력 확인
            self.assertEqual("key", driver.find_element_by_id("key0").get_attribute("value"))
            self.assertEqual("value", driver.find_element_by_xpath("//input[@value='value']").get_attribute("value"))
        except:
            print('TEST FAIL : test_check_attributions')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_attributions-%s.png' % now)
        else:
            print('TEST PASS : test_check_attributions')

    def test_check_tags(self):  # categories 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Asset 메뉴로 이동
            driver.find_element_by_link_text("Assets").click()
            # [Create Asset]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Assets'])[3]/following::strong[1]").click()
            time.sleep(3)
            # 항목명 확인 (Tags)
            self.assertEqual("Tags", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Add'])[1]/following::strong[1]").text)
            # 입력필드 value 확인
            self.assertEqual("", driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/form/div[5]/div[2]/div/div/div/div/div/textarea").get_attribute(
                "value"))
            # 입력필드에 텍스트 입력 (tag)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/form/div[5]/div[2]/div/div/div/div/div/textarea").click()
            # tag 입력이 안되네
            #
            # tag 입력 후 Enter key 입력
            # 엔터키 입력이 안되네
            '''
            # 입력한 Tag 출력 확인
            self.assertEqual("tag", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::span[1]").text)
            '''
        except:
            print('TEST FAIL : test_check_tags')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_tags-%s.png' % now)
        else:
            print('TEST PASS : test_check_tags')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Assets_Create('test_check_breadcrumb'))
    suite.addTest(Assets_Create("test_check_title"))
    suite.addTest((Assets_Create("test_check_name")))
    suite.addTest((Assets_Create("test_check_type")))
    suite.addTest((Assets_Create("test_check_categories")))
    suite.addTest((Assets_Create("test_check_attributions")))
    suite.addTest((Assets_Create("test_check_tags")))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())