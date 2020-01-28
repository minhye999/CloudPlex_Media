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

    def test_check_detail_copy(self):  # Lineup Copy 출력 요소 확인 (과거 Lineup : "EXO 엑소 'Love Shot' MV")
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
            # Lineup Detail 패널 [Copy to] 버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div/div/button/i").click()
            time.sleep(3)
            # Copy 패널 출력요소 - 타이틀 : Lineup copy
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div/div/button/span/i")
            time.sleep(3)
            # [Cancel]버튼, [Save]버튼, [X]버튼
            self.assertEqual("Cancel", driver.find_element_by_xpath("(//button[@type='button'])[71]").text)
            time.sleep(5)
            self.assertEqual("Save", driver.find_element_by_xpath("(//button[@type='button'])[72]").text)
            time.sleep(5)
            driver.find_element_by_xpath("//div[@id='right-sidebar']/span/i").is_displayed()
            time.sleep(5)
            # Name*타이틀
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/h5")
            time.sleep(10)
            # Name 입력필드에 "Copy" 추가 입력
            driver.find_element_by_xpath("//input[@value='']").click()
            driver.find_element_by_xpath("//input[@value='']").clear()
            driver.find_element_by_xpath("//input[@value='']").send_keys("EXO 엑소 'Love Shot' MV_copy")
            time.sleep(10)
            # Schedule 타이틀
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div[2]/h5").text()
            # Schedule - Time
            driver.find_element_by_xpath("//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[2]/div/label/strong").text()
            # Schedule - Start time(*)
            driver.find_element_by_xpath("//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/label").text()
            # Schedule - End time(*)
            driver.find_element_by_xpath("//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[4]/label").text()
            # Schedule - Program Duration (00:03:29.189)
            driver.find_element_by_xpath("//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[2]/div/div[3]/div/ul/li/span").text()
            driver.find_element_by_xpath("//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[2]/div/div[3]/div/ul/li/strong").text()
            # Schedule - Contents Duration (00:03:29.189)
            driver.find_element_by_xpath(
                "//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[2]/div/div[3]/div/ul/li[2]/span").text()
            driver.find_element_by_xpath(
                "//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[2]/div/div[3]/div/ul/li[2]/strong").text()
            # Schedule - Repeat(checkbox)
            driver.find_element_by_xpath("//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[2]/div/div[4]/div/div/label/strong").text()
            driver.find_element_by_name("Recurrence").is_displayed()
            time.sleep(5)
            # Schedule - [편성 목록]아이콘 클릭
            driver.find_element_by_xpath(
                "//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/button").click()
            time.sleep(7)
            # 달력패널 날짜 선택 (현재 1월 기준, 2020-2-28 날짜 선택)
            driver.find_element_by_xpath(
                "//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/svg").click()
            time.sleep(7)
            driver.find_element_by_xpath(
                "//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[5]/td[6]").click()
            time.sleep(7)
            # Priority
            driver.find_element_by_xpath("//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[2]/div/div[5]/label/strong").text()
            # Program 타이틀
            driver.find_element_by_xpath("//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[3]/h5").text()
            # Program - Name
            driver.find_element_by_xpath("//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[3]/div/div/label/strong").text()
            driver.find_element_by_xpath("//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[3]/div/div/div").text()
            # Program - Description 텍스트명
            driver.find_element_by_xpath("//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[3]/div/div[2]/label/strong").text()
            time.sleep(3)
            # Program - Description (-)
            driver.find_element_by_xpath("//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[3]/div/div[2]/div").text()
            time.sleep(3)
            # Program - Attributions 텍스트명
            driver.find_element_by_xpath("//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[3]/div/div[3]/label/strong").text()
            # Program - Attributions (-)
            driver.find_element_by_xpath("//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[3]/div/div[3]/div").text()
            time.sleep(3)
            # Program - Media [MP4라벨]
            driver.find_element_by_xpath("//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[3]/div/div[4]/h6").text()
            driver.find_element_by_xpath("//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[3]/div/div[4]/div/span").text()
            time.sleep(7)
            # Lineup copy 패널 - Save 버튼 클릭
            driver.find_element_by_xpath("//div[@id='right-sidebar']/div/div/div/div/div/button[2]/strong").click()
            time.sleep(7)
            # [편성 목록]아이콘 클릭
            driver.find_element_by_css_selector("path").click()
            time.sleep(5)
            # 달력 패널에서 다음달로 이동하여, 생성한 미래날짜(2020-2-28)선택
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]").click()
            time.sleep(7)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[5]/td[6]").click()
            time.sleep(10)
            # 생성된 스케쥴 Name 확인 ("EXO 엑소 'Love Shot' MV_copy")
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div[9]").text()
            time.sleep(10)

        except:
            print('TEST FAIL : check_detail_copy')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_detail_copy')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Lineup_Detail('test_check_detail_copy'))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())