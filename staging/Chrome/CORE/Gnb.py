# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class Gnb(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_check_ui(self): # Service Logo 출력 및 링크 이동 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self) # Project Main page로 이동하는 공통 모듈 호출
            # Service Logo 확인
            driver.find_element_by_xpath("//img[@alt='logo']")
            # Jobs Page로 이동
            driver.find_element_by_link_text("Jobs").click()
            time.sleep(3)
            # Brand Logo 클릭
            driver.find_element_by_xpath("//img[@alt='logo']").click()
            time.sleep(3)
            # Main Page로 이동 확인 (Create Jobs Title 확인)
            self.assertEqual("Create Job", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::h3[1]").text)

            ### [Create Job]버튼 출력 및 링크 이동 확인
            # [Create Job]버튼 확인
            self.assertEqual("Create job",
                             driver.find_element_by_xpath("//div[@id='root']/div/nav/div[2]/div/ul/li/a/strong").text)
            # [Create Job]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/nav/div[2]/div/ul/li/a/strong").click()
            time.sleep(3)
            # Create Job 페이지로 이동 확인 (Create Job Title 확인)
            self.assertEqual("Create Job", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::h3[1]").text)
        except:
            print('TEST FAIL : test_check_ui')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('../../../staging/Chrome/Test_Results/Screenshots/test_check_ui-%s.png' % now)
        else:
            print('TEST PASS : test_check_ui')

    def test_check_project(self): # Project 정보 출력 및 링크 이동 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Stage 아이콘 확인 (시간될때 찾아보자)
            #self.assertEqual("thumbnail", driver.find_element_by_xpath("//div/i[@class='thumbnail']").text)
            #self.assertEqual("/images/stage.png",
            #                 driver.find_element_by_xpath("//div/i[@img src='/images/stage.png']").text)
            # Stage Name 확인 (Megazone)
            self.assertEqual("Megazone", driver.find_element_by_xpath(
                "//div[@id='root']/div/nav/div[2]/div/ul/li[2]/div/div/button/div/div/strong").text)
            # Project Name 확인 (Project C)
            self.assertEqual("Project C", driver.find_element_by_xpath(
                "//div[@id='root']/div/nav/div[2]/div/ul/li[2]/div/div/button/div/div/span").text)
            # Project Select Menu 클릭
            driver.find_element_by_xpath("//button[@type='button']").click()
            time.sleep(3)
            # Project Select Menu에서 Stage 아이콘 확인
            #self.assertEqual("Megazone", driver.find_element_by_xpath(
            #    "(.//*[normalize-space(text()) and normalize-space(.)='Continuum'])[1]/following::strong[1]").text)
            # Project Select Menu에서 Stage Name 확인 (Megazone)
            self.assertEqual("Megazone", driver.find_element_by_xpath(
                "//div[@id='root']/div/nav/div[2]/div/ul/li[2]/div/div/div/div/div/strong").text)
            # Project Select Menu에서 Project Name 확인 (Project C)
            self.assertEqual("Project C", driver.find_element_by_link_text("Project C").text)
            # Project Select Menu에서 Project Name 확인 (Project D)
            self.assertEqual("Project D", driver.find_element_by_link_text("Project D").text)
            # Project Select Menu에서 다른 Project 클릭 (Project D)
            driver.find_element_by_link_text("Project D").click()
            time.sleep(3)
            # Project D Project Page로 이동 확인
            self.assertEqual("Project D", driver.find_element_by_xpath(
                "//div[@id='root']/div/nav/div[2]/div/ul/li[2]/div/div/button/div/div/span").text)
            # Project Select Menu 클릭
            driver.find_element_by_xpath("//button[@type='button']").click()
            time.sleep(3)
            # Project Select 이동 아이콘 클릭하여 Project Select 화면으로 이동
            driver.find_element_by_xpath("//div[@id='root']/div/nav/div[2]/div/ul/li[2]/div/div/div/div/a/i").click()
            # Project 선택하여 다시 메인 메이지로 복귀 (Project C)
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/ul/li/a/div/p").click()
        except:
            print('TEST FAIL : check_project')
            logging.basicConfig(stream=sys.stderr, level=logging.error)
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_project')

    def test_check_user(self): # User 정보 출력 및 링크 이동 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self) # Project Main page로 이동하는 공통 모듈 호출
            # 사용자 아이콘 확인 -> 갑자기 버튼이 upload로 바뀜 why?
            #self.assertEqual("sprite sprite-user", driver.find_element_by_class_name('sprite sprite-user').text)
            driver.find_element_by_xpath("//div[@id='root']/div/nav/div[2]/div/ul/li[3]/div/a/i")
            # 사용자 이름 확인
            self.assertEqual("메가존", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='media.qa.001@gmail.com'])[1]/preceding::em[1]").text)
            # 사용자 계정 확인
            self.assertEqual("media.qa.001@gmail.com", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='메가존'])[1]/following::small[1]").text)
        except:
            print('TEST FAIL : check_user')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_user')

    def test_click_btn_signOut(self): # Sign Out 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self) # Project Main page로 이동하는 공통 모듈 호출
            # [Sign Out]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/nav/div[2]/div/ul/li[3]/div/button/i").click()
            time.sleep(3)
            # After (Welcome Text 확인)
            self.assertEqual("Welcome!", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='You need to sign in a Megazone Accounts account to get started.'])[1]/preceding::h4[1]").text)
        except:
            print('TEST FAIL : click_btn_signOut')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : click_btn_signOut')

    def test_click_btn_admin(self): # Admin 버튼 출력 및 이동 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Admin]버튼 확인 -> 이슈로 div class 체크
            self.driver.find_element_by_xpath("//div[@class='admin-menu-toggle ']")
            # [Admin]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/nav/div[2]/div/ul/li[4]/div/div/button/i").click()
            # Admin 메뉴에서 [Administrator] 메뉴 확인
            self.assertEqual("Administrator", driver.find_element_by_link_text("Administrator").text)
            # Admin 메뉴에서 [Project manager] 메뉴 확인
            self.assertEqual("Project manager", driver.find_element_by_link_text("Project manager").text)
            # Admin 메뉴에서 [Administrator] 메뉴 선택
            driver.find_element_by_link_text("Administrator").click()
            time.sleep(7)
            # [Administrator] 메뉴로 이동 (Administration Title 출력 확인) -> 이슈로 해당 Title이 있는 div class 체크
            # self.assertEqual("Administration", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Download Apps'])[1]/following::p[1]").text)
            self.driver.find_element_by_xpath("//div[@class='menu-type menu-type-admin']")
            # [Admin]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/nav/div[2]/div/ul/li[4]/div/div/button/i").click()
            # driver.find_element_by_class_name("admin-menu-toggle ").click()
            # Admin 메뉴에서 [Project manager] 메뉴 선택
            driver.find_element_by_link_text("Project manager").click()
            time.sleep(3)
            # [Project manager] 메뉴로 이동 (Project manager Title 출력 확인) -> 이슈로 해당 Title이 있는 div class 체크
            # self.assertEqual("Project manager", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Download Apps'])[1]/following::p[1]").text)
            self.driver.find_element_by_xpath("//div[@class='menu-type menu-type-project']")
            # self.assertEqual("Project manager", driver.find_element_by_xpath("//div[@class='menu-type menu-type-project']").text)
        except:
            print('TEST FAIL : click_btn_admin')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : click_btn_admin')

    def test_click_btn_downloadApps(self):  # Downlaod Apps 버튼 출력 및 이동 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Download Apps]버튼 확인 -> xpath 아예 안직힘 -> div class로 체크 (근데 왜 명칭이 Admin menu 인지 ^^;)
            self.driver.find_element_by_xpath("//div[@class='admin-menu-toggle ']")
            # [Download Apps]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/nav/div[2]/div/ul/li[5]/div/div/button/i").click()
            # [Download Apps] 메뉴 확인
            self.assertEqual("Download Apps", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Project manager'])[1]/following::button[2]").text)
            # [Download Apps] 메뉴에서 [Download Apps] 메뉴 선택
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Project manager'])[1]/following::button[2]").click()
            time.sleep(3)
            # DownloadApps 팝업에서 Title 확인
            self.assertEqual("Download Apps", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Download Apps'])[1]/following::h5[1]").text)
        except:
            print('TEST FAIL : click_btn_downloadApps')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_clickBtnDownloadApps-%s.png' % now)
        else:
            print('TEST PASS : click_btn_downloadApps')

    def test_check_btn_downloadAppsPopUp(self): # Downlaod Apps 팝업 구성요소 및 기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self) # Project Main page로 이동하는 공통 모듈 호출
            Gnb.test_click_btn_downloadApps(self) # Download Apps 팝업을 호출하는 함수 호출
            time.sleep(3)
            # DownloadApps 팝업에서 Title 확인
            self.assertEqual("Download Apps", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Download Apps'])[1]/following::h5[1]").text)
            # DownloadApps 팝업에서 Hyper Browser 로고 확인
            self.driver.find_element_by_xpath("//div[@class='apps.hyper-browser']")
            # DownloadApps 팝업에서 Hyper Browser App Name 확인
            self.assertEqual("Hyper Browser", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Download Apps'])[2]/following::h6[1]").text)
            # DownloadApps 팝업에서 Hyper Browser App Version 확인
            self.assertEqual("1.3.4.5091", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Hyper Browser'])[1]/following::p[1]").text)
            # DownloadApps 팝업에서 Hyper Browser App 소개 확인
            self.assertEqual(
                "Hyper Browser is an enterprise cloud storage client.Accelerate a variety of workloads with a multi-CDN integration environment and powerful features such as multi-part upload/download, purge and pre-patch.",
                driver.find_element_by_xpath(
                    "(.//*[normalize-space(text()) and normalize-space(.)='Hyper Browser'])[1]/following::p[2]").text)
            # DownloadApps 팝업에서 Hyper Browser App [Download]버튼 확인
            self.assertEqual("Download", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Hyper Browser'])[1]/following::strong[1]").text)
            # DownloadApps 팝업에서 Hyper Browser App [Download]버튼 클릭 ★버튼 클릭 후 다운이 받아지는지 확인해보고 싶다
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Hyper Browser'])[1]/following::strong[1]").click()
            # DownloadApps 팝업에서 Hyper Subtitle Editor App 로고 확인
            self.driver.find_element_by_xpath("//div[@class='apps hyper-subtitle-editor']")
            # DownloadApps 팝업에서 Hyper Subtitle Editor App Name 확인
            self.assertEqual("Hyper Subtitle Editor", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Download'])[1]/following::h6[1]").text)
            # DownloadApps 팝업에서 Hyper Subtitle Editor App Version 확인
            self.assertEqual("0.7.0.28", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Hyper Subtitle Editor'])[1]/following::p[1]").text)
            # DownloadApps 팝업에서 Hyper Subtitle Editor App 소개 확인
            self.assertEqual(
                "Hyper Subtitle Editor works with the MCM platform to provide flexible workflows from subtitling registration to publishing.Quickly create subtitles with user experience-based UI to gain a wider audience.",
                driver.find_element_by_xpath(
                    "(.//*[normalize-space(text()) and normalize-space(.)='Hyper Subtitle Editor'])[1]/following::p[2]").text)
            # DownloadApps 팝업에서 Hyper Subtitle Editor App [Download]버튼 확인
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Hyper Browser'])[1]/following::strong[1]").click()
            # DownloadApps 팝업에서 Hyper Subtitle Editor App [Download]버튼 클릭 ★버튼 클릭 후 다운이 받아지는지 확인해보고 싶다
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Hyper Browser'])[1]/following::strong[1]").click()
            # DownloadApps 팝업에서 [X]버튼 확인
            self.driver.find_element_by_xpath("//i[@class='sprite sprite-cancel-lg']")
            # DownloadApps 팝업에서 [X]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/button/span/i").click()
            # DownloadApps 팝업 닫혔는지 확인
            #
        except:
            print('TEST FAIL : check_btn_downloadAppsPopUp')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/check_checkDownloadAppsPopUp-%s.png' % now)
        else:
            print('TEST PASS : check_btn_downloadAppsPopUp')

    def test_check_myJobs(self): # My Jobs 버튼 출력 및 이동 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self) # Project Main page로 이동하는 공통 모듈 호출
            # [My Jobs]버튼 확인
            self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Download Apps'])[1]/following::a[1]")
            # [My Jobs]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Download Apps'])[1]/following::a[1]").click()
            # My Jobs 패널에서 Title 확인
            self.assertEqual("My Jobs", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Detail'])[1]/following::h4[1]").text)
            # My Jobs 패널에서 [X]버튼 확인
            self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Detail'])[1]/following::span[2]")
            # My Jobs 패널에서 Job 부재 시, 문구 확인
            self.assertEqual("No Jobs searched.", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='My Jobs'])[1]/following::span[1]").text)
            # My Jobs 패널에서 [X]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Detail'])[1]/following::span[2]").click()
            # My Jobs 패널닫혔는지 확인 ([My Jobs]버튼 출력)
            self.driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Download Apps'])[1]/following::a[1]")
        except:
            print('TEST FAIL : check_myJobs')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/checkMyJobs-%s.png' % now)
        else:
            print('TEST PASS : check_myJobs')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Gnb('test_check_ui'))
    suite.addTest(Gnb('test_check_project'))
    suite.addTest(Gnb('test_check_user'))
    suite.addTest(Gnb('test_click_btn_signOut'))
    suite.addTest(Gnb('test_click_btn_admin'))
    suite.addTest(Gnb('test_click_btn_downloadApps'))
    suite.addTest(Gnb('test_check_btn_downloadAppsPopUp'))
    suite.addTest(Gnb('test_check_myJobs'))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())