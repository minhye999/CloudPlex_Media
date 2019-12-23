# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class Assets_Create_Mp4(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_check_type_local(self):  # Type : MP4 > Local File 확인
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
            # Type 선택 (MP4)
            driver.find_element_by_id("rdb-asset-type-MP4").click()
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
        except:
            print('TEST FAIL : test_check_type_local')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_type_local-%s.png' % now)
        else:
            print('TEST PASS : test_check_type_local')

    def test_check_type_s3(self):  # Type : MP3 > S3 File 확인
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
            # Type 선택 (MP4)
            driver.find_element_by_id("rdb-asset-type-MP4").click()
            # [Select a file]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='CAPTION'])[1]/following::button[1]").click()
            # [S3 Files] 라디오버튼 선택
            driver.find_element_by_xpath("(//input[@name='selectFiles'])[2]").click()
            # path 입력필드 클릭
            driver.find_element_by_xpath("(//input[@value=''])[2]").click()
            # 유효한 경로 입력 (https://mz-cm-stg-transcoding-input.s3.ap-northeast-2.amazonaws.com/testdata/test_001.mp4) -> 대박임 모달 뒤에 동일한 class가 있어서 type으로 해결
            #driver.find_element_by_xpath(
            #    "//input[@value='https://mz-cm-stg-transcoding-input.s3.ap-northeast-2.amazonaws.com/testdata/test_001.mp4']").clear()
            #driver.find_element_by_xpath(
            #    "//input[@value='https://mz-cm-stg-transcoding-input.s3.ap-northeast-2.amazonaws.com/testdata/test_001.mp4']").send_keys(
            #    "https://mz-cm-stg-transcoding-input.s3.ap-northeast-2.amazonaws.com/testdata/test_001.mp4")
            #self.driver.find_element_by_xpath('//*[@class="form-control"]').send_keys(
            #    'https://mz-cm-stg-transcoding-input.s3.ap-northeast-2.amazonaws.com/testdata/test_001.mp4')
            self.driver.find_element_by_xpath('//*[@type="url"]').send_keys(
                'https://mz-cm-stg-transcoding-input.s3.ap-northeast-2.amazonaws.com/testdata/test_001.mp4')
            # [Add]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Please select a file to add.'])[1]/preceding::button[1]").click()
            time.sleep(3)
            # [Select]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
            # 선택한 파일 출력 확인 (경로+파일명)
            self.assertEqual(
                "https://mz-cm-stg-transcoding-input.s3.ap-northeast-2.amazonaws.com/testdata/test_001.mp4",
                driver.find_element_by_xpath(
                    "(.//*[normalize-space(text()) and normalize-space(.)='CAPTION'])[1]/following::span[3]").text)
            # 선택한 파일 출력 확인 (파일 사이즈)
            self.assertEqual("- 5.82 MB", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='https://mz-cm-stg-transcoding-input.s3.ap-northeast-2.amazonaws.com/testdata/test_001.mp4'])[1]/following::span[1]").text)
        except:
            print('TEST FAIL : test_check_type_s3')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_type_s3-%s.png' % now)
        else:
            print('TEST PASS : test_check_type_s3')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest((Assets_Create_Mp4("test_check_type_local")))
    suite.addTest((Assets_Create_Mp4("test_check_type_s3")))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())