# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class CreateJob(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_check_breadcrumb(self):  # Breadcrumb 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴 클릭
            driver.find_element_by_link_text("Create Job").click()
            # Breadcrumb 확인 (Transcoding > Create Job)
            self.assertEqual("Transcoding", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Create Job'])[2]/following::li[1]").text)
            self.assertEqual("Create Job", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Transcoding'])[2]/following::li[1]").text)
        except:
            print('TEST FAIL : check_breadcrumb')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_breadcrumb')

    def test_check_title(self):  # Title 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴 클릭
            driver.find_element_by_link_text("Create Job").click()
            # Title 확인 (Create Job)
            self.assertEqual("Create Job", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::h3[1]").text)
        except:
            print('TEST FAIL : check_title')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_title')

    def test_check_pipeline(self):  # Pipeline 확인 및 선택
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # Pipeline Text 확인
            self.assertEqual("Pipeline", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Create Job'])[3]/following::h6[1]").text)
            # Pipeline 확인 (Default : hls with multiple audio manual)
            self.assertEqual("hls with multiple audio manual", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Pipeline'])[1]/following::div[5]").text)
            # Pipeline Select Box 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Pipeline'])[1]/following::div[4]").click()
            # Pipeline Select Box에서 Pipeline 확인
            #
            # [Pipeline Detail] 버튼 확인
            self.assertEqual("", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='hls with multiple audio manual'])[1]/following::button[1]").get_attribute(
                "value"))
            # [Pipeline Detail] 버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[2]/div/div/div/div/button/i").click()
            time.sleep(3)
            # Pipeline Detail 팝업 출력 확인 (Title만 체크)
            self.assertEqual("Pipeline Detail", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='hls with multiple audio manual'])[1]/following::h5[1]").text)
        except:
            print('TEST FAIL : check_pipeline')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_pipeline')

    def test_check_pipelineDetailPopUp(self):  # Pipeline Detail 팝업 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            CreateJob.test_check_pipeline(self) # Pipeline Detail 팝업 호출
            # Pipeline Detail 팝업의 Title 확인
            self.assertEqual("Pipeline Detail", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='hls with multiple audio manual'])[1]/following::h5[1]").text)
        except:
            print('TEST FAIL : check_pipelineDetailPopUp')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_pipelineDetailPopUp')

    def test_check_profile(self):  # Profile 확인 및 선택
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # Pipeline Select Box 활성화
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='dash, mp4 automatic'])[1]/following::*[name()='svg'][1]").click()
            # Pipeline 선택 ("dash, mp4 automatic")
            driver.find_element_by_id("react-select-47-option-2").click()
            # Profile Text 확인
            self.assertEqual("Profile", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='dash, mp4 automatic'])[1]/following::h6[1]").text)
            # Profile 확인 (MPEG-Dash video profile)
            self.assertEqual("MPEG-Dash video profile", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Profile'])[1]/following::span[1]").text)
            # Profile 링크 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Pipeline'])[1]/following::div[5]").click()
            # [Profile Detail] 버튼 확인
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Profile'])[1]/following::span[1]")
            # [Profile Detail] 버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Profile'])[1]/following::span[1]").click()
            time.sleep(3)
            # Profile Detail 팝업 출력 확인 (Title만 체크)
            self.assertEqual("Profile Detail", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='(3)'])[1]/following::h5[1]").text)
        except:
            print('TEST FAIL : check_profile')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_profile')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(CreateJob('test_check_breadcrumb'))
    suite.addTest(CreateJob("test_check_title"))
    suite.addTest(CreateJob("test_check_pipeline"))
    suite.addTest(CreateJob("test_check_pipelineDetailPopUp"))
    suite.addTest(CreateJob("test_check_profile"))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())