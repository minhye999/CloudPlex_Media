# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class Assets_Create_Caption(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_check_type_caption_local(self):  # Type : IMAGE > Local File 확인
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
            # Type 선택 (CAPTION)
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::div[2]").click()
            time.sleep(3)
            # 항목명 확인 (Kind)
            self.assertEqual("Kind", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='CAPTION'])[1]/following::strong[1]").text)
            # Default 값 확인 (Select Kind)
            self.assertEqual("Select Kind", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Kind'])[1]/following::div[6]").text)
            # Kind 선택 (Caption)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Select Kind'])[1]/following::*[name()='svg'][1]").click()
            driver.find_element_by_id("react-select-4-option-0").click()
            # 선택한 Kind 확인 (Caption)
            self.assertEqual("Caption", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Kind'])[1]/following::div[6]").text)
            # [Select a file]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='CAPTION'])[1]/following::button[1]").click()
            # [Add files]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Please select a file to add.'])[1]/following::label[1]").click()
            # Local file 선택
            #
            # [Select]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
            # 선택한 파일 출력 확인
            #
            # 항목명 확인 (Label)
            self.assertEqual("Label", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Select a file'])[1]/following::div[2]").text)
            # Label value 확인
            self.assertEqual("", driver.find_element_by_xpath("(//input[@value=''])[3]").get_attribute("value"))
            # Label 선택
            driver.find_element_by_xpath("//input[@value='label']").clear()
            driver.find_element_by_xpath("//input[@value='label']").send_keys("label")
            # 선택한 Label 출력 확인
            self.assertEqual("label", driver.find_element_by_xpath("//input[@value='label']").get_attribute("value"))
            # 항목명 확인 (Language)
            self.assertEqual("", driver.find_element_by_xpath("(//input[@value=''])[3]").get_attribute("value"))
            # Language value 확인 (Select Language)
            self.assertEqual("Language", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Label'])[1]/following::strong[1]").text)
            # Language 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Language'])[1]/following::div[4]").click()
            # Language 선택 (Korean - Korea)
            driver.find_element_by_id("react-select-5-option-81").click()
            # 선택한 Language 출력 확인 (Korean - Korea)
            self.assertEqual("Korean - Korea", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Language'])[1]/following::div[5]").text)
        except:
            print('TEST FAIL : test_check_type_caption_local')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_type_caption_local-%s.png' % now)
        else:
            print('TEST PASS : test_check_type_caption_local')

    def test_check_type_caption_s3(self):  # Type : IMAGE > S3 File 확인
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
            # Type 선택 (CAPTION)
            driver.find_element_by_id("rdb-asset-type-CAPTION").click()
            time.sleep(3)
            # 항목명 확인 (Kind)
            self.assertEqual("Kind", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='CAPTION'])[1]/following::strong[1]").text)
            #driver.find_element_by_class_name(("Kind").text)
            #self.driver.find_element_by_xpath("//div[@class='Kind']")
            # Default 값 확인 (Select Kind)
            self.assertEqual("Select Kind", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Kind'])[1]/following::div[6]").text)
            '''
            # Kind 선택 (Caption) 
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Kind'])[1]/following::div[5]").click()
            time.sleep(3)
            driver.find_element_by_id("react-select-2-option-0").click()
            # 선택한 Kind 확인 (Caption)
            self.assertEqual("Caption", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Kind'])[1]/following::div[6]").text)
            '''
            # [Select a file]버튼 출력 확인
            #self.assertEqual("Select a file", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Caption'])[1]/following::button[1]").text)
            # 안내문구 출력 확인 (Select one caption file)
            self.assertEqual("Select one caption file.", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Select a file'])[1]/following::p[1]").text)
            # [Select a file]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Caption'])[1]/following::button[1]").click()
            # [S3 Files] 라디오버튼 선택
            driver.find_element_by_xpath("(//input[@name='selectFiles'])[2]").click()
            # path 입력필드 클릭
            driver.find_element_by_xpath("(//input[@value=''])[2]").click()
            # 유효한 경로 입력 (https://mz-cm-stg-transcoding-input.s3.ap-northeast-2.amazonaws.com/testdata/test_002_Chinese.vtt)
            self.driver.find_element_by_xpath('//*[@type="url"]').send_keys(
                'https://mz-cm-stg-transcoding-input.s3.ap-northeast-2.amazonaws.com/testdata/test_002_Chinese.vtt')
            # [Add]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Please select a file to add.'])[1]/preceding::button[1]").click()
            time.sleep(3)
            # [Select]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
            # 선택한 파일 출력 확인 (경로+파일명)
            self.assertEqual(
                "https://mz-cm-stg-transcoding-input.s3.ap-northeast-2.amazonaws.com/testdata/test_002_Chinese.vtt",
                driver.find_element_by_xpath(
                    "(.//*[normalize-space(text()) and normalize-space(.)='Caption'])[1]/following::span[4]").text)
            # 선택한 파일 출력 확인 (파일 사이즈)
            self.assertEqual("- 2.50 KB", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='https://mz-cm-stg-transcoding-input.s3.ap-northeast-2.amazonaws.com/testdata/test_002_Chinese.vtt'])[1]/following::span[1]").text)
            # 항목명 확인 (Label)
            self.assertEqual("Label", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Select a file'])[1]/following::div[2]").text)
            # Label value 확인
            self.assertEqual("", driver.find_element_by_xpath("(//input[@value=''])[3]").get_attribute("value"))
            # Label 선택
            driver.find_element_by_xpath("//input[@value='label']").clear()
            driver.find_element_by_xpath("//input[@value='label']").send_keys("label")
            # 선택한 Label 출력 확인
            self.assertEqual("label", driver.find_element_by_xpath("//input[@value='label']").get_attribute("value"))
            # 항목명 확인 (Language)
            self.assertEqual("", driver.find_element_by_xpath("(//input[@value=''])[3]").get_attribute("value"))
            # Language value 확인 (Select Language)
            self.assertEqual("Language", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Label'])[1]/following::strong[1]").text)
            # Language 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Language'])[1]/following::div[4]").click()
            # Language 선택 (Korean - Korea)
            driver.find_element_by_id("react-select-5-option-81").click()
            # 선택한 Language 출력 확인 (Korean - Korea)
            self.assertEqual("Korean - Korea", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Language'])[1]/following::div[5]").text)
        except:
            print('TEST FAIL : test_check_type_caption_s3')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_type_caption_s3-%s.png' % now)
        else:
            print('TEST PASS : test_check_type_caption_s3')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest((Assets_Create_Caption("test_check_type_caption_local")))
    suite.addTest((Assets_Create_Caption("test_check_type_caption_s3")))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())