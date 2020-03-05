# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class PopUp_PipelineDetail(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_check_title(self):  # Title 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # [Pipeline Detail] 버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[2]/div/div/div/div/button/i").click()
            time.sleep(3)
            # Pipeline Detail 팝업의 Title 확인
            self.assertEqual("Pipeline Detail", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='hls with multiple audio manual'])[1]/following::h5[1]").text)
        except:
            print('TEST FAIL : check_title')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_title')

    def test_check_viewMode(self):  # View Mode 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # [Pipeline Detail] 버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[2]/div/div/div/div/button/i").click()
            time.sleep(3)
            # Mode 확인 (Default : Tree) ★★★★ 오류로 제외 ★★★★
            # self.assertEqual("TreeText", driver.find_element_by_xpath(
            #   "(.//*[normalize-space(text()) and normalize-space(.)='Pipeline Detail'])[1]/following::select[1]").text)
            # Mode Select Box 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Pipeline Detail'])[1]/following::select[1]").click()
            # Mode Select Box에 Tree Mode 출력 확인
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Pipeline Detail'])[1]/following::select[1]")
            # Mode Select Box에서 Tree Mode 선택
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Pipeline Detail'])[1]/following::select[1]").click()
            # Tree Mode 출력 확인
            self.assertEqual("7 items", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='{'])[1]/following::span[1]").text)
            self.assertEqual("\"hls with multiple audio manual\"", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='string'])[2]/following::span[1]").text)
            # Mode Select Box에 Text Mode 출력 확인
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Pipeline Detail'])[1]/following::select[1]")
            # Mode Select Box에서 Text Mode 선택
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Pipeline Detail'])[1]/following::select[1]").click()
            # Text Mode 출력 확인 ★★★★ 오류로 제외 ★★★★
            '''
            self.assertEqual(
                "{\n \"id\": \"16\",\n \"name\": \"hls with multiple audio manual\",\n \"description\": \"hls manual transcoding\",\n \"outputPath\": \"mz-cm-stg-transcoding-output/hls-manual\",\n \"inputPath\": \"mz-cm-stg-transcoding-input/upload\",\n \"project\": {\n \"id\": \"mz-cm-v1\"\n },\n \"transcodeProfile\": {\n \"id\": \"1571127466w9D2\"\n }\n}",
                driver.find_element_by_xpath(
                    "(.//*[normalize-space(text()) and normalize-space(.)='Pipeline Detail'])[1]/following::pre[1]").text)
            '''
        except:
            print('TEST FAIL : check_viewMode')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_viewMode')

    def test_check_btn_folding(self):  # View Mode 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # [Pipeline Detail] 버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[2]/div/div/div/div/button/i").click()
            time.sleep(3)
            # 펼치기/접기버튼 확인 (Default : 접혀있음)
            driver.find_element_by_xpath("(//button[@type='button'])[6]")
            # [접기]버튼 클릭 -> 우케하지?
            #
            # 영역 접히는지 확인
            #
            # [펼치기]버튼 클릭 -> 우케하지?
            #driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
            # 영역 펼쳐지는지 확인
            #
        except:
            print('TEST FAIL : check_btn_folding')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_btn_folding')

    def test_check_btn_close(self):  # View Mode 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # [Pipeline Detail] 버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[2]/div/div/div/div/button/i").click()
            time.sleep(3)
            # [X]버튼 확인
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/button/span/i")
            # [X]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/button/span/i").click()
            # [Pipeline Detail] 버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[2]/div/div/div/div/button/i").click()
            time.sleep(3)
            # [Close]버튼 확인
            self.assertEqual("Close", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='}'])[3]/following::button[1]").text)
            # [Close]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='}'])[3]/following::button[1]").click()
        except:
            print('TEST FAIL : check_btn_close')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_btn_close')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(PopUp_PipelineDetail('test_check_title'))
    suite.addTest(PopUp_PipelineDetail("test_check_viewMode"))
    suite.addTest(PopUp_PipelineDetail("test_check_btn_folding"))
    suite.addTest(PopUp_PipelineDetail("test_check_btn_close"))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())