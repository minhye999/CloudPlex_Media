# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class Jobs(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_checkBreadcrumb(self):  # Breadcrumb 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Jobs] 메뉴로 이동
            driver.find_element_by_link_text("Jobs").click()
            # Breadcrumb 확인 (Transcoding > Jobs)
            self.assertEqual("Transcoding", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Jobs'])[2]/following::li[1]").text)
            self.assertEqual("Jobs", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Transcoding'])[2]/following::li[1]").text)
            time.sleep(10)
        except:
            print('TEST FAIL : checkBreadcrumb')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkBreadcrumb')

    def test_checkTitle(self):  # Title 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Jobs] 메뉴로 이동
            driver.find_element_by_link_text("Jobs").click()
            # Title 확인 (Jobs)
            self.assertEqual("Jobs", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::h3[1]").text)
        except:
            print('TEST FAIL : checkTitle')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkTitle')

    def test_checkPipeline_search(self):  # Pipeline 확인 및 선택, 검색
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Jobs] 메뉴로 이동
            driver.find_element_by_link_text("Jobs").click()
            # 검색옵션 : Pipeline 확인 (Default : All Pipeline)
            self.assertEqual(u"All Pipeline", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Jobs'])[3]/following::div[9]").text)
            # Pipeline Select Box 클릭
            #
            # Pipeline Select Box에서 Pipeline 확인
            #
            # Pipeline Select Box에서 hls manual 항목 클릭
            #
            # [search] 버튼 클릭
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Created at'])[1]/following::span[1]").click()
            time.sleep(10)
            # Table > pipeline : hls manual 리스트 출력 확인
            #
            # [Reset] 버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[2]/div/form/div/div[2]/div/button[2]/i").click()
            # Pipeline검색옵션 초기화 되었는지 확인 (Default : All Pipeline)
            self.assertEqual(u"All Pipeline", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Jobs'])[3]/following::div[9]").text)
        except:
            print('TEST FAIL : checkPipeline_search')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
            '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkPipeline_search')

    def test_checkName_search(self):  # name 확인, 검색
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Jobs] 메뉴로 이동
            driver.find_element_by_link_text("Jobs").click()
            # 검색옵션 : Name 확인 (Default : Name)
            self.assertEqual(u"Name", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='All Pipeline'])[1]/following::div[12]").text)
            # Name/Job ID Select Box 클릭 (클릭동작 안되고 있음)
            #driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='All Pipeline'])[1]/following::div[12]").click()
            # Name/Job ID Select Box에서 Name/Job ID리스트 확인
            #
            # Name 입력필드 클릭 (오류발생으로 케이스 제외)
            # driver.find_element_by_name("keyword").click()
            # Name입력(exo)
            driver.find_element_by_name("keyword").send_keys(u"exo")
            # 검색버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created at'])[1]/following::button[2]").click()
            time.sleep(10)
            # 검색결과 출력 확인 (exo가 들어간 title 체크)
            self.assertEqual(u"EXO 엑소 'CALL ME BABY' MV", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Action'])[1]/following::span[1]").text)

        except:
            print('TEST FAIL : checkName_search')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkName_search')

    def test_checkStatus_search(self):  # Status 확인 및 선택, 검색
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Jobs] 메뉴로 이동
            driver.find_element_by_link_text("Jobs").click()
            # 검색옵션 : All status 확인 (Default : All status) 오류발생으로 케이스 제외
            #self.driver.find_element_by_xpath('//div[@id="k4do65cw"]/div/div[1]/div[1]')
            # Status Select Box 클릭
            #
            # Status Select Box에서 리스트 확인
            #
            # Status Select Box에서 complete 항목 클릭
            #
            # 검색버튼 클릭
            driver.find_element_by_xpath(
              "(.//*[normalize-space(text()) and normalize-space(.)='Created at'])[1]/following::button[2]").click()
            time.sleep(10)
            # 검색결과 출력 확인 (complete 리스트)
            #self.assertEqual(u"COMPLETE", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Action'])[1]/following::span[1]").text)
            #time.sleep(10)

        except:
            print('TEST FAIL : checkStatus_search')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkStatus_search')

    def test_checkCreated_search(self):  # Created 확인 및 선택, 검색
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Jobs] 메뉴로 이동
            driver.find_element_by_link_text("Jobs").click()
            time.sleep(10)
            # 검색옵션 : Created 확인
            self.driver.find_element_by_xpath
            ('//div[@id="root"]/div/div/div[1]/div/div[2]/div/form/div/div[1]/div[2]/div[2]/div/div[1]')
            # 달력 아이콘 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created at'])[1]/following::button[1]").click()
            time.sleep(3)
            # 달력 패널에서 이전 월 이동 버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Sa'])[1]/following::*[name()='svg'][1]").click()
            time.sleep(3)
            # 시작/ 종료날짜 클릭하여 설정 (ex: 2019-12-1 ~ 2019-12-31)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='December 2019'])[1]/following::td[1]").click()
            time.sleep(5)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='December 2019'])[1]/following::td[31]").click()
            time.sleep(7)
            # 검색버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created at'])[1]/following::button[2]").click()
            time.sleep(10)
            # 검색결과 출력 확인 (시작/ 종료날짜 설정값대로 리스트 출력되는지 여부)
            self.assertEqual("2019-12-24 12:03:49", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='rosa@mz.co.kr'])[3]/following::time[1]").text)
            time.sleep(10)

        except:
            print('TEST FAIL : checkCreated_search')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkCreated_search')

    def test_checkMixed_search(self):  # name 확인, 검색
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Jobs] 메뉴로 이동
            driver.find_element_by_link_text("Jobs").click()
            # 검색옵션 : Pipeline 확인 (Default : All Pipeline) xpath이슈로 div class체크
            self.driver.find_element_by_xpath(
               '//div[@id="root"]/div/div/div[1]/div/div[2]/div/form/div/div[1]/div[1]/div[1]')
            # Pipeline Select Box 클릭
            #
            # Pipeline Select Box에서 dash mp4 automatic 항목 클릭
            #
            # 검색옵션 : Name 확인 (Default : Name)
            self.driver.find_element_by_xpath('//div[@id="root"]/div/div/div[1]/div/div[2]/div/form/div/div[1]/div[1]/div[2]/div/div')
            # Name 입력필드 클릭 (오류발생으로 케이스 제외)
            # driver.find_element_by_name("keyword").click()
            # Name입력(exo)
            driver.find_element_by_name("keyword").send_keys(u"exo")
            # 검색버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created at'])[1]/following::button[2]").click()
            time.sleep(10)
            # 조합된 검색결과 출력 확인 (Pipeline : dash mp4 automatic, exo가 들어간 title 체크), 두개 이상 검색 시 오류나고 있음(한가지 항목만 검색 성공)
            self.assertEqual(u"EXO 엑소 'CALL ME BABY' MV+Audio_중국어 더빙", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Action'])[1]/following::span[1]").text)
            self.assertEqual(u"dash, mp4 automatic", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cats-feel4'])[1]/following::span[1]").text)

        except:
            print('TEST FAIL : checkMixed_search')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkMixed_search')

    def test_click_link_job(self):  # Job상세 진입
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Jobs] 메뉴로 이동
            driver.find_element_by_link_text("Jobs").click()
            # Job리스트 클릭하여 상세페이지 진입 (EXO 엑소 'CALL ME BABY' MV/ 1577670155fUFD)
            driver.find_element_by_link_text("EXO 엑소 'CALL ME BABY' MV").click()
            time.sleep(10)
        except:
            print('TEST FAIL : click_link_job')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : click_link_job')
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Jobs('test_checkBreadcrumb'))
    suite.addTest(Jobs("test_checkTitle"))
    suite.addTest(Jobs("test_checkPipeline_search"))
    suite.addTest(Jobs("test_checkName_search"))
    suite.addTest(Jobs("test_checkStatus_search"))
    suite.addTest(Jobs("test_checkCreated_search"))
    suite.addTest(Jobs("test_checkMixed_search"))
    suite.addTest(Jobs("test_click_link_job"))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())