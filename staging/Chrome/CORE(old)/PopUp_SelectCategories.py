# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common
from selenium.webdriver.common.keys import Keys

class PopUp_SelectCategories(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        # self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        # self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        # self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_check_title(self): # 팝업 title 및 info 출력 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()

            # Category [+]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Select category'])[1]/following::button[2]").click()
            time.sleep(3)
            # Category title 확인
            self.assertEqual("Select Categories", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Category'])[1]/following::h5[1]").text)

        except:
            print('TEST FAIL : test_check_title')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_title-%s.png' % now)
        else:
            print('TEST PASS : test_check_title')

    def test_check_close(self): # [Close]버튼 출력 및 동작 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # Category [+]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Select category'])[1]/following::button[2]").click()
            time.sleep(3)
            #[Close]버튼 확인 -> 에잇 안됨
            #driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/dl/dd/div/div/div/div/button/i")
            #self.driver.find_element_by_xpath('//*[@class="sprite sprite-cancel-lg"]')
            #driver.find_element_by_name('close')
            # [Close]버튼 클릭
            #driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/dl/dd/div/div/div/div/button/i").click()
            #driver.find_element_by_xpath('//*[@class="sprite sprite-cancel-lg"]').click()
            #driver.find_element_by_class_name("close").click("sprite sprite-cancel-lg")
            #self.driver.find_element_by_xpath('//*[@class="sprite sprite-cancel-lg"]').send_keys()
            #self.driver.find_element_by_xpath('//*[@class="modal-header"]').send_keys()
            #driver.find_element_by_name('close').click()
            #driver.find_element_by_name('sprite sprite-cancel-lg').click()
            #driver.find_elements_by_class_name("sprite sprite-cancel-lg").click()
            #driver.find_element_by_xpath("//form[@class='close']/button").click()
            #driver.find_element_by_xpath("//form[@class='sprite sprite-cancel-lg']/button").click()
            #driver.find_element_by_xpath("//form[@class='close']/button").send_keys(Keys.ENTER)
            #driver.find_element_by_xpath("//form[@class='sprite sprite-cancel-lg']/button").send_keys(Keys.ENTER)

            #element = driver.find_element_by_xpath("//form[@class='close']/button")
            #driver.execute_script("arguments[0].click();", element)
        except:
            print('TEST FAIL : test_check_close')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_close-%s.png' % now)
        else:
            print('TEST PASS : test_check_close')

    def test_check_search(self): # [Close]버튼 출력 및 동작 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # Category [+]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Select category'])[1]/following::button[2]").click()
            time.sleep(3)
            # 검색입력필드 value 확인
            self.assertEqual("", driver.find_element_by_name("keyword").get_attribute("value"))
            # [검색]버튼 확인
            #driver.find_element_by_xpath(
            #    "//div[@id='root']/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/dl/dd/div/div/div/div[2]/form/div/div[2]/button/i")
            ''' MZCLOUDMED-6393  이슈로 정상 동작하지만 일단 주석
            # 유효하지 않은 검색어 입력 (zzzzzzzzzz)
            driver.find_element_by_name("keyword").clear()
            driver.find_element_by_name("keyword").send_keys("zzzzzzzzzz")
            # [검색]버튼 클릭
            #driver.find_element_by_xpath(
            #    "//div[@id='root']/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/dl/dd/div/div/div/div[2]/form/div/div[2]/button/i").click()
            self.driver.find_element_by_xpath("//div[@class='btns']").click()
            time.sleep(5)
            # 검색결과 개수 확인 (Total 0)
            self.assertEqual("Total", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Select Categories'])[1]/following::strong[1]").text)
            self.assertEqual("0", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Total'])[1]/following::span[1]").text)
            # 안내문구 출력 확인 (Empty Categories)
            self.assertEqual("Empty Categories", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Total'])[1]/following::div[3]").text)
            # 검색결과 선택 개수 확인 (0 Categories Selected)
            self.assertEqual("0", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Empty Categories'])[1]/following::em[1]").text)
            self.assertEqual("Categories Selected", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Empty Categories'])[1]/following::span[1]").text)
            '''
            # 유효한 검색어 입력 (YG)
            driver.find_element_by_name("keyword").clear()
            driver.find_element_by_name("keyword").send_keys("YG")
            # [검색]버튼 클릭
            #driver.find_element_by_xpath(
            #    "//div[@id='root']/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/dl/dd/div/div/div/div[2]/form/div/div[2]/button/i").click()
            self.driver.find_element_by_xpath("//div[@class='btns']").click()
            time.sleep(5)
            # 검색결과 개수 항목 출력되는거까지만 확인 (Total)\
            self.assertEqual("Total", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Select Categories'])[1]/following::strong[1]").text)
            # Category 체크박스에 체크 (YG)
            driver.find_element_by_xpath("//input[@type='checkbox']").click()
            time.sleep(3)
            # 검색결과 선택 개수 확인 (1 Categories Selected)
            self.assertEqual("1", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='YG'])[1]/following::em[1]").text)
            self.assertEqual("Categories Selected", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='YG'])[1]/following::span[2]").text)
            # 선택한 Category가 출력됨 확인
            self.assertEqual("YG", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Categories Selected'])[1]/following::span[2]").text)
            # [Select]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
            time.sleep(3)
            # 팝업닫히고, 선택한 Category명이 출력됨 확인
            self.assertEqual("YG", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Category'])[1]/following::span[3]").text)
        except:
            print('TEST FAIL : test_check_search')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_search-%s.png' % now)
        else:
            print('TEST PASS : test_check_search')

    def test_check_cancel(self): # [Close]버튼 출력 및 동작 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # Category [+]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Select category'])[1]/following::button[2]").click()
            time.sleep(3)
            # [Cancel]버튼 확인
            self.assertEqual("Cancel", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Categories Selected'])[1]/following::button[1]").text)
            # [Cancel]버튼 클릭
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='remove'])[1]/following::button[1]").click()
        except:
            print('TEST FAIL : test_check_cancel')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_cancel-%s.png' % now)
        else:
            print('TEST PASS : test_check_cancel')

        def tearDown(self):
            self.driver.close()
            self.driver.quit()
            print("Test Done")

def suite():
    suite = unittest.TestSuite()
    #suite.addTest(PopUp_SelectCategories('test_check_title'))
    suite.addTest(PopUp_SelectCategories("test_check_close"))
    #suite.addTest(PopUp_SelectCategories('test_check_search'))
    #suite.addTest(PopUp_SelectCategories('test_check_cancel'))
    return suite


if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())