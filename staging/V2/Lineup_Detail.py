# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class Lineup_Detail(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_check_lineupTab_detail(self):  # Lineup Detail - lineup탭 출력 요소 확인 (과거 Lineup : "EXO 엑소 'Love Shot' MV")
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Listings] 메뉴로 이동
            driver.find_element_by_link_text("Listings").click()
            time.sleep(5)
            # Listings 리스트 클릭하여 Lineup편성 페이지 진입 (list1 / 1577690929yyeP)
            driver.find_element_by_link_text("list1").click()
            time.sleep(10)
            # [편성 목록]아이콘 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Listings Detail'])[1]/following::*[name()='svg'][1]").click()
            time.sleep(3)
            # 달력 패널에서 날짜 선택 (2020-1-3)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='January 2020'])[1]/following::td[6]").click()
            time.sleep(3)
            # [i]버튼 확인
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div[11]/div/span/span/i")
            # [i]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div[11]/div/span/span/i").click()
            # Lineup Detail 패널 Title 확인
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div/h4/span")
            time.sleep(3)
            # Lineup Detail 패널 [Copy to] 버튼 확인
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div/div/button/i")
            time.sleep(3)
            # Lineup Detail 패널 [Delete] 버튼 확인(과거 lineup이므로 비활성 상태로 존재)
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div/div/button[2]/i")
            time.sleep(3)
            # Lineup Detail 패널 X버튼 확인
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div/div/button/span/i")
            time.sleep(3)
            # Lineup Detail 패널 Player 확인
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]")
            time.sleep(3)
            # Lineup Detail 패널 Lineup탭 확인
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/nav/a/span")
            time.sleep(3)
            # Lineup탭 출력 요소 확인 - Name* 타이틀, 입력박스
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/h5")
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div/div")
            time.sleep(3)
            # Lineup탭 출력 요소 확인 - Schedule 타이틀, Time, Start~End, Mark in~out
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div[2]/h5")
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/label/strong")
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/span")
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[3]/span")
            time.sleep(3)
            # Lineup탭 출력 요소 확인 - Priority 타이틀, 아이콘/ Medium 텍스트
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div[3]/h5")
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div[3]/div/div/span/i")
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div[3]/div/div/span[2]")
            time.sleep(3)

        except:
            print('TEST FAIL : check_lineupTab_detail')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_lineupTab_detail')

    def test_check_programTab_detail(self):  # Lineup Detail - program탭 출력 요소 확인 (과거 Lineup : "EXO 엑소 'Love Shot' MV")
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Listings] 메뉴로 이동
            driver.find_element_by_link_text("Listings").click()
            time.sleep(5)
            # Listings 리스트 클릭하여 Lineup편성 페이지 진입 (list1 / 1577690929yyeP)
            driver.find_element_by_link_text("list1").click()
            time.sleep(10)
            # [편성 목록]아이콘 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Listings Detail'])[1]/following::*[name()='svg'][1]").click()
            time.sleep(3)
            # 달력 패널에서 날짜 선택 (2020-1-3)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='January 2020'])[1]/following::td[6]").click()
            time.sleep(3)
            # [i]버튼 확인
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div[11]/div/span/span/i").is_displayed()
            time.sleep(3)
            # [i]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div[11]/div/span/span/i").click()
            time.sleep(3)
            # Lineup Detail 패널 Title 확인
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div/h4/span")
            time.sleep(3)
            # Lineup Detail 패널 [Copy to] 버튼 확인
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div/div/button/i")
            time.sleep(3)
            # Lineup Detail 패널 [Delete] 버튼 확인(과거 lineup이므로 비활성 상태로 존재)
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div/div/button[2]/i")
            time.sleep(3)
            # Lineup Detail 패널 X버튼 확인
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div/div/button/span/i")
            time.sleep(3)
            # Lineup Detail 패널 Player 확인
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]")
            time.sleep(3)
            # Lineup Detail 패널 Program탭 확인
            driver.find_element_by_link_text("Program").is_displayed()
            time.sleep(3)
            # Lineup Detail 패널 Program탭 클릭
            driver.find_element_by_link_text("Program").click()
            time.sleep(3)
            # Program탭 출력 요소 확인 - Name 타이틀, 입력박스
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div/label/strong")
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div/div")
            time.sleep(3)
            # Program탭 출력 요소 확인 - Description 타이틀, 입력박스
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/label/strong")
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div")
            time.sleep(3)
            # Program탭 출력 요소 확인 - Attribution 타이틀, 입력박스
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[3]/label/strong")
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[3]/div")
            time.sleep(3)
            # Program탭 출력 요소 확인 - Attribution 타이틀, 입력박스
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[3]/label/strong")
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[3]/div")
            time.sleep(3)
            # Program탭 출력 요소 확인 - Media 타이틀, MP4라벨
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[4]/h6")
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[4]/div/span")
            time.sleep(3)
            # Program탭 출력 요소 확인 - Posters 타이틀, 입력박스
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[5]/h6")
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[5]/div")
            time.sleep(3)
            # Lineup Detail 패널 X버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div/div/button/span/i").click()
            time.sleep(3)

        except:
            print('TEST FAIL : check_programTab_detail')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_programTab_detail')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Lineup_Detail('test_check_lineupTab_detail'))
    suite.addTest(Lineup_Detail('test_check_programTab_detail'))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())