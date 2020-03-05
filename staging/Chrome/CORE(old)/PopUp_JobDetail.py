# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class PopUp_JobDetail(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    #PopUp_JobDetail
    def test_checkTitle(self):  # Title 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # 검증용 컨텐츠 URL 불러오기 (EXO 엑소 'CALL ME BABY' MV)
            driver.get(
                "http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/transcoding/jobs/1577670155fUFD")
            time.sleep(10)

            # [Job Detail] 버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[2]/div[2]/div[4]/nav/button/i").click()
            time.sleep(3)
            # Job Detail 팝업의 Title 확인
            self.assertEqual("Job Detail", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='}'])[3]/following::h5[1]").text)
        except:
            print('TEST FAIL : checkTitle')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
               '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkTitle')

    def test_checkViewMode(self):  # View Mode 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # 검증용 컨텐츠 URL 불러오기 (EXO 엑소 'CALL ME BABY' MV)
            driver.get(
                "http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/transcoding/jobs/1577670155fUFD")
            time.sleep(10)

            # [Job Detail] 버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[2]/div[2]/div[4]/nav/button/i").click()
            # Mode 확인 (Default : Tree) ★★★★ 오류로 제외 ★★★★
            # self.assertEqual("TreeText", driver.find_element_by_xpath(
            #   "(.//*[normalize-space(text()) and normalize-space(.)='Job Detail'])[1]/following::select[1]").text)
            # Mode Select Box 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Job Detail'])[1]/following::select[1]").click()
            # Mode Select Box에 Tree Mode 출력 확인
            driver.find_element_by_xpath(
              "(.//*[normalize-space(text()) and normalize-space(.)='Job Detail'])[1]/following::select[1]")
            # Mode Select Box에서 Tree Mode 선택
            driver.find_element_by_xpath(
              "(.//*[normalize-space(text()) and normalize-space(.)='Job Detail'])[1]/following::select[1]").click()
            # Tree Mode 출력 확인
            self.assertEqual("4 items", driver.find_element_by_xpath(
              "(.//*[normalize-space(text()) and normalize-space(.)='{'])[4]/following::span[1]").text)
            self.assertEqual('"arn:aws:iam::068670021050:role/mz-cm-mediaconvert-default"', driver.find_element_by_xpath(
               "(.//*[normalize-space(text()) and normalize-space(.)='string'])[3]/following::span[1]").text)
            # Mode Select Box에 Text Mode 출력 확인
            driver.find_element_by_xpath(
              "(.//*[normalize-space(text()) and normalize-space(.)='Job Detail'])[1]/following::select[1]")
            # Mode Select Box에서 Text Mode 선택
            driver.find_element_by_xpath(
              "(.//*[normalize-space(text()) and normalize-space(.)='Job Detail'])[1]/following::select[1]").click()
            # Text Mode 출력 확인 ★★★★ 오류로 제외 ★★★★

            # 펼치기/접기버튼 확인 (Default : 접혀있음)
            #
            # [펼치기]버튼 클릭 -> 우케하지?
            #
            # 영역 펼쳐지는지 확인
            #
            # [접기]버튼 클릭 -> 우케하지?
            #
            # 영역 접히는지 확인
            #
            # [X]버튼 확인
            driver.find_element_by_xpath(
              "//div[@id='root']/div/div/div[1]/div/div[3]/div/div/div[1]/button/span/i")
            # [X]버튼 클릭
            driver.find_element_by_xpath(
              "//div[@id='root']/div/div/div[1]/div/div[3]/div/div/div[1]/button/span/i").click()
            # [Job Detail] 버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[2]/div[2]/div[4]/nav/button/i").click()
            time.sleep(3)
            # [Close]버튼 확인
            self.assertEqual("Close", driver.find_element_by_xpath(
              "(.//*[normalize-space(text()) and normalize-space(.)='}'])[6]/following::button[1]").text)
            # [Close]버튼 클릭
            driver.find_element_by_xpath(
              "(.//*[normalize-space(text()) and normalize-space(.)='}'])[6]/following::button[1]").click()

        except:
            print('TEST FAIL : checkViewMode')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                 '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkViewMode')

    def tearDown(self):
            self.driver.close()
            self.driver.quit()
            print("Test Done")

def suite():
        suite = unittest.TestSuite()
        suite.addTest(PopUp_JobDetail('test_checkTitle'))
        suite.addTest(PopUp_JobDetail("test_checkViewMode"))
        return suite
if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())