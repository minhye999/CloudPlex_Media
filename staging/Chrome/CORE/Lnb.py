# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class Lnb(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_check_menu_dashboard(self): # Dashboard 메뉴 확인 및 이동
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self) # Project Main page로 이동하는 공통 모듈 호출
            # Dashboard 메뉴 출력 확인
            self.assertEqual("Dashboard", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Download Apps'])[1]/following::span[1]").text)
            # Dashboard 메뉴 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Download Apps'])[1]/following::span[1]").click()
            time.sleep(3)
            # Dashboard 메뉴로 이동 확인
        except:
            print('TEST FAIL : check_menu_dashboard')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_menu_dashboard')

    def test_check_menu_transcoding(self):  # Transcoding 메뉴 확인 및 이동
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Transcoding 메뉴 출력 확인
            self.assertEqual("Transcoding", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Dashboard'])[1]/following::span[1]").text)
            # Transcoding 메뉴 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Dashboard'])[1]/following::span[1]").click()
            time.sleep(3)
            # Transcoding 메뉴로 이동 확인 (Breadcrumb : Transcoding > Jobs)
            self.assertEqual("Transcoding", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Jobs'])[2]/following::li[1]").text)
            # Transcoding 메뉴로 이동 확인 (Breadcrumb : Transcoding > Jobs)
            self.assertEqual("Jobs", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Transcoding'])[2]/following::li[1]").text)
        except:
            print('TEST FAIL : check_menu_transcoding')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_menu_transcoding')

    def test_check_menu_jobs(self):  # Jobs 메뉴 확인 및 이동
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Jobs 메뉴 출력 확인
            self.assertEqual("Jobs", driver.find_element_by_link_text("Jobs").text)
            # Jobs 메뉴 클릭
            driver.find_element_by_link_text("Jobs").click()
            time.sleep(3)
            # Jobs 메뉴로 이동 확인 (Breadcrumb : Transcoding > Jobs)
            self.assertEqual("Transcoding", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Jobs'])[2]/following::li[1]").text)
            # Jobs 메뉴로 이동 확인 (Breadcrumb : Transcoding > Jobs)
            self.assertEqual("Jobs", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Transcoding'])[2]/following::li[1]").text)
        except:
            print('TEST FAIL : check_menu_jobs')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_menu_jobs')

    def test_check_menu_createJob(self):  # Create Job 메뉴 확인 및 이동
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Create Job 메뉴 출력 확인
            self.assertEqual("Create Job", driver.find_element_by_link_text("Create Job").text)
            # Create Job 메뉴 클릭
            driver.find_element_by_link_text("Create Job").click()
            time.sleep(3)
            # Create Job 메뉴로 이동 확인 (Breadcrumb : Transcoding > Create Job)
            self.assertEqual("Transcoding", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Create Job'])[2]/following::li[1]").text)
            # Create Job 메뉴로 이동 확인 (Breadcrumb : Transcoding > Create Job)
            self.assertEqual("Create Job", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Transcoding'])[2]/following::li[1]").text)
        except:
            print('TEST FAIL : check_menu_createJob')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_menu_createJob')

    def test_check_menu_contents(self):  # Contents 메뉴 확인 및 이동
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Contents 메뉴 출력 확인
            self.assertEqual("Contents", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create Job'])[1]/following::span[1]").text)
            # Contents 메뉴 클릭
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create Job'])[1]/following::span[1]").click()
            time.sleep(3)
            # Contents 메뉴로 이동 확인 (Breadcrumb : Contents > Assets)
            self.assertEqual("Contents", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Assets'])[2]/following::li[1]").text)
            # Contents 메뉴로 이동 확인 (Breadcrumb : Contents > Assets)
            self.assertEqual("Assets", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Contents'])[2]/following::li[1]").text)
        except:
            print('TEST FAIL : check_menu_contents')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_menu_contents')

    def test_check_menu_assets(self):  # Assets 메뉴 확인 및 이동
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Assets 메뉴 출력 확인
            self.assertEqual("Assets", driver.find_element_by_link_text("Assets").text)
            # Assets 메뉴 클릭
            driver.find_element_by_link_text("Assets").click()
            time.sleep(3)
            # Assets 메뉴로 이동 확인 (Breadcrumb : Contents > Assets)
            self.assertEqual("Contents", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Assets'])[2]/following::li[1]").text)
            # Assets 메뉴로 이동 확인 (Breadcrumb : Contents > Assets)
            self.assertEqual("Assets", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Contents'])[2]/following::li[1]").text)
        except:
            print('TEST FAIL : check_menu_assets')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_menu_assets')

    def test_check_menu_videos(self):  # Videos 메뉴 확인 및 이동
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴 출력 확인
            self.assertEqual("Videos", driver.find_element_by_link_text("Videos").text)
            # Videos 메뉴 클릭
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # Videos 메뉴로 이동 확인 (Breadcrumb : Contents > Videos)
            self.assertEqual("Contents", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Videos'])[2]/following::li[1]").text)
            # Videos 메뉴로 이동 확인 (Breadcrumb : Contents > Videos)
            self.assertEqual("Videos", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Contents'])[2]/following::li[1]").text)
        except:
            print('TEST FAIL : check_menu_videos')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_menu_videos')

    def test_check_menu_people(self):  # People 메뉴 확인 및 이동
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # People 메뉴 출력 확인
            self.assertEqual("People", driver.find_element_by_link_text("People").text)
            # People 메뉴 클릭
            driver.find_element_by_link_text("People").click()
            time.sleep(3)
            # People 메뉴로 이동 확인 (Breadcrumb : Contents > People)
            self.assertEqual("Contents", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='People'])[2]/following::li[1]").text)
            # People 메뉴로 이동 확인 (Breadcrumb : Contents > People)
            self.assertEqual("People", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Contents'])[2]/following::li[1]").text)
        except:
            print('TEST FAIL : check_menu_people')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_menu_people')

    def test_check_menu_live(self):  # Live 메뉴 확인 및 이동
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Live 메뉴 출력 확인
            self.assertEqual("Live", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='People'])[1]/following::span[1]").text)
            # Live 메뉴 클릭
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='People'])[1]/following::span[1]").click()
            time.sleep(3)
            # Live 메뉴로 이동 확인 (Breadcrumb : Live > Streams)
            self.assertEqual("Live", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Streams'])[2]/following::li[1]").text)
            # Live 메뉴로 이동 확인 (Breadcrumb : Live > Streams)
            self.assertEqual("Streams", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Live'])[2]/following::li[1]").text)
        except:
            print('TEST FAIL : check_menu_live')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_menu_live')

    def test_check_menu_streams(self):  # Streams 메뉴 확인 및 이동
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Streams 메뉴 출력 확인
            self.assertEqual("Streams", driver.find_element_by_link_text("Streams").text)
            # Streams 메뉴 클릭
            driver.find_element_by_link_text("Streams").click()
            time.sleep(3)
            # Streams 메뉴로 이동 확인 (Breadcrumb : Live > Streams)
            self.assertEqual("Streams", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Live'])[2]/following::li[1]").text)
            # Streams 메뉴로 이동 확인 (Breadcrumb : Live > Streams)
            self.assertEqual("Streams", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Live'])[2]/following::li[1]").text)
        except:
            print('TEST FAIL : check_menu_streams')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_menu_streams')

    def test_check_menu_listings(self):  # Listings 메뉴 확인 및 이동
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Listings 메뉴 출력 확인
            self.assertEqual("Listings", driver.find_element_by_link_text("Listings").text)
            # Listings 메뉴 클릭
            driver.find_element_by_link_text("Listings").click()
            time.sleep(3)
            # Listings 메뉴로 이동 확인 (Breadcrumb : Live > Listings)
            self.assertEqual("Live", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Listings'])[2]/following::li[1]").text)
            # Listings 메뉴로 이동 확인 (Breadcrumb : Live > Listings)
            self.assertEqual("Listings", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Live'])[2]/following::li[1]").text)
        except:
            print('TEST FAIL : check_menu_listings')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_menu_listings')

    def test_check_menu_channels(self):  # Channels 메뉴 확인 및 이동
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Channels 메뉴 출력 확인
            self.assertEqual("Channels", driver.find_element_by_link_text("Channels").text)
            # Channels 메뉴 클릭
            driver.find_element_by_link_text("Channels").click()
            time.sleep(3)
            # Channels 메뉴로 이동 확인 (Breadcrumb : Live > Channels)
            self.assertEqual("Live", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[2]/following::li[1]").text)
            # Channels 메뉴로 이동 확인 (Breadcrumb : Live > Channels)
            self.assertEqual("Channels", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Live'])[2]/following::li[1]").text)
        except:
            print('TEST FAIL : check_menu_channels')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_menu_channels')

    def test_check_btn_lnb(self):  # LNB 접기/펼치기 버튼 확인 및 이동
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # LNB [접기]버튼 확인
            self.assertEqual("", driver.find_element_by_xpath("(//button[@type='button'])[6]").get_attribute("value"))
            # LNB [펼치기]버튼 클릭
            driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
            # LNB [펼치기]버튼 확인 ★ 접기랑 똑같은데 흠...
            self.assertEqual("", driver.find_element_by_xpath("(//button[@type='button'])[6]").get_attribute("value"))
            # LNB [펼치기]버튼 클릭 ★ 접기랑 똑같은데 흠...
            driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
        except:
            print('TEST FAIL : check_btn_lnb')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_btn_lnb')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Lnb('test_check_menu_dashboard'))
    suite.addTest(Lnb("test_check_menu_transcoding"))
    suite.addTest(Lnb("test_check_menu_jobs"))
    suite.addTest(Lnb("test_check_menu_createJob"))
    suite.addTest(Lnb("test_check_menu_contents"))
    suite.addTest(Lnb("test_check_menu_assets"))
    suite.addTest(Lnb("test_check_menu_videos"))
    suite.addTest(Lnb("test_check_menu_people"))
    suite.addTest(Lnb("test_check_menu_live"))
    suite.addTest(Lnb("test_check_menu_streams"))
    suite.addTest(Lnb("test_check_menu_listings"))
    suite.addTest(Lnb("test_check_menu_channels"))
    suite.addTest(Lnb("test_check_btn_lnb"))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())