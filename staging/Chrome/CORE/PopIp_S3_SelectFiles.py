# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common
#import staging.Chrome.ProjectAd.Settings_Transcoding

class PopUp_S3_SelectFiles(unittest.TestCase):

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
            # [S3 files]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='- or -'])[1]/following::button[2]").click()
            # [i]아이콘 확인
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/h5/div/i")
            # [i]아이콘 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/h5/div/i").click()
            # Upload rules 내용 확인
            self.assertEqual("Upload rules", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='JPEG'])[1]/following::strong[1]").text)
            self.assertEqual("Maximum object size", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Upload rules'])[1]/following::p[1]").text)
            self.assertEqual("5 GB", driver.find_element_by_xpath(
                   "(.//*[normalize-space(text()) and normalize-space(.)='Upload rules'])[1]/following::div[2]").text)
            self.assertEqual("Supported URL patterns", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Upload rules'])[1]/following::p[2]").text)
            '''
            self.assertEqual(
                "https://s3.{region}.amazonaws.com/{bucket}/{filepath}https://{bucket}.s3.amazonaws.com/{filepath}s3://{bucket}/{filepath}",
                driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Upload rules'])[1]/following::div[3]").text)
            self.assertEqual("Supported file formats", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Upload rules'])[1]/following::p[3]").text)
            self.assertEqual(".3gp .3g2 .3gpp .asf .divx .flv .f4v .m2ts .ts .mts .m2t .m3u8 .mp3 .mp4 .m4v .m2v .mpeg .vob .m1v .avi .mpt .mpg .trp .264 .h264 .mov .mkv .wmv .dv .xvid .gxf .mxf .gxf_mpeg2 .mxf_mpeg2 .mxfhd .wav .y4m .raw .vmf .lch", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Upload rules'])[1]/following::div[4]").text)
            '''
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
            # [S3 files]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='- or -'])[1]/following::button[2]").click()
            # [X]버튼 확인
            driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/")
            # [X]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/button/span/i").click()
            # 팝업 닫히면, 다시 [S3 files]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='- or -'])[1]/following::button[2]").click()
        except:
            print('TEST FAIL : test_check_close')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_close-%s.png' % now)
        else:
            print('TEST PASS : test_check_close')

    def test_check_tab(self): # Local / S3 Files 탭 출력 및 동작 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # [S3 files]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='- or -'])[1]/following::button[2]").click()
            # Local Files 텍스트 출력 확인
            self.assertEqual("Local Files", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Upload rules'])[1]/following::strong[1]").text)
            # S3 Files 라디오버튼 On 확인
            self.assertEqual("on", driver.find_element_by_xpath("(//input[@name='selectFiles'])[2]").get_attribute(
                "value"))
            # S3 Files 텍스트 출력 확인
            self.assertEqual("S3 Files", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Upload rules'])[1]/following::strong[2]").text)
            # 파일 부재 시, 입력필드 value 확인
            self.assertEqual("", driver.find_element_by_xpath("(//input[@value=''])[2]").get_attribute("value"))
            # 파일 부재 시, 안내문구 확인(Please select a file to add.)
            self.assertEqual("Please select a file to add.", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Add'])[1]/following::span[1]").text)
        except:
            print('TEST FAIL : test_check_tab')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_tab-%s.png' % now)
        else:
            print('TEST PASS : test_check_tab')

    def test_check_cancel(self): # [Cancel]버튼 출력 및 동작 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # [S3 files]버튼 클릭
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='- or -'])[1]/following::button[2]").click()
            # [Cancel]버튼 출력 확인
            self.assertEqual("Cancel", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Add Files'])[1]/following::button[1]").text)
            # [Cancel]버튼 클릭
            # driver.find_element_by_xpath(
            #    "(.//*[normalize-space(text()) and normalize-space(.)='test_001.mp4'])[1]/following::button[2]").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Add Files'])[1]/following::button[1]").click()
            # 팝업닫히고, [S3 files]버튼 클릭하여 팝업 출력 확인
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='- or -'])[1]/following::button[2]").click()
        except:
            print('TEST FAIL : test_check_cancel')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_cancel-%s.png' % now)
        else:
            print('TEST PASS : test_check_cancel')

    def test_check_select(self): # 파일 Select 기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # [S3 files]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='- or -'])[1]/following::button[2]").click()
            # 경로 입력
            # [Add]버튼 클릭
            # 선택한 파일 확인
            # Selected files 영역에 선택한 파일 추가되었음을 확인 : Local 파일 아이콘 출력 확인
            # Selected files 영역에 선택한 파일 추가되었음을 확인 : 파일명 출력 확인
            # Selected files 영역에 선택한 파일 추가되었음을 확인 : 파일 사이즈 출력 확인
        except:
            print('TEST FAIL : test_check_select')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_select-%s.png' % now)
        else:
            print('TEST PASS : test_check_select')

        def tearDown(self):
            self.driver.close()
            self.driver.quit()
            print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(PopUp_S3_SelectFiles('test_check_title'))
    #suite.addTest(PopUp_S3_SelectFiles('test_check_close'))
    #suite.addTest(PopUp_S3_SelectFiles('test_check_tab'))
    suite.addTest(PopUp_S3_SelectFiles('test_check_cancel'))
    #suite.addTest(PopUp_S3_SelectFiles('test_check_select'))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())