# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class PopUp_Publish(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_check_title(self):  # Publish 기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # DASH Video 상세 페이지로 이동 (ID : 1578039655b2n5)
            driver.find_element_by_id("quick-search").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys("1578039655b2n5")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").click()
            time.sleep(3)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::p[1]").click()
            time.sleep(3)
            # [Publish]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Videos'])[2]/following::button[1]").click()
            time.sleep(3)
            # 팝업 Title 확인
            self.assertEqual("Publish", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::h5[1]").text)
            # [X]버튼 확인
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/div/div/div/div/button/span/i").click()
            # [X]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Videos'])[2]/following::button[1]").click()
            # [Publish]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Videos'])[2]/following::span[1]").click()
            # Video 항목명, Data 확인
            self.assertEqual("Video", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Publish'])[1]/following::h6[1]").text)
            self.assertEqual(u"자동화 테스트 - 001(1578039655b2n5)", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Video'])[1]/following::p[1]").text)
            # to Publish 항목명, Data 확인
            self.assertEqual("to Publish", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='(1578039655b2n5)'])[1]/following::h6[1]").text)
            self.driver.find_element_by_xpath("//div/span/i[@class='sprite sprite-youtube']")
            self.driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Facebook'])[1]/following::span[1]")
            self.assertEqual("Youtube", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Facebook'])[1]/following::strong[1]").text)
            # to Publish 기능 확인
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Facebook'])[1]/following::span[1]").click()
            time.sleep(3)
            # 배포 확인
            self.driver.find_element_by_xpath("//div/span/i[@class=':after']") #문제로다
            # Embed Code 항목명, Data 확인
            self.assertEqual("Embed Code", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Instagram'])[1]/following::h6[1]").text)
            self.assertRegexpMatches(driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Embed Code'])[1]/following::textarea[1]").text,
                                     "^<iframe width=\"560\" height=\"315\" src=\"https://mz-cm-demo-site\\.s3\\.amazonaws\\.com/player/index\\.html[\\s\\S]userId=c8a51623-8745-475a-8728-efdec2a6811c&jobId=1578039552JyMx&src=https%3A%2F%2Fs3\\.ap-northeast-2\\.amazonaws\\.com%2Fmz-cm-stg-transcoding-output%2Fmz-cm-v1%2Fassets%2F1578039574hFld%2Ftest_001_mp4\\.mp4&isEncrypted=\" frameborder=\"0\" allow=\"accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>$")
            # Embed Code [Copy] 버튼 확인
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/div/div/div/div[2]/div[3]/button/i")
            # Embed Code [Copy] 버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/div/div/div/div[2]/div[3]/button/i").click()
            # Paste를 어떻게 확인할지 생각해보자
        except:
            print('TEST FAIL : test_check_title')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_title-%s.png' % now)
        else:
            print('TEST PASS : test_check_title')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(PopUp_Publish('test_check_title'))
    suite.addTest(PopUp_Publish("test_check_viewMode"))
    suite.addTest(PopUp_Publish("test_check_btn_folding"))
    suite.addTest(PopUp_Publish("test_check_btn_close"))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())