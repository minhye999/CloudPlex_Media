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

    def test_checkImgServiceLogo(self): # Service Logo 출력 및 링크 이동 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.moveMainPage(self) # Project Main page로 이동하는 공통 모듈 호출
            # Service Logo 확인

            # Jobs Page로 이동
            driver.find_element_by_link_text("Jobs").click()
            time.sleep(3)
            # Service Logo 클릭
            driver.find_element_by_xpath("//img[@alt='logo']").click()
            time.sleep(3)
            # Main Page로 이동 확인 (Create Jobs Title 확인)
            self.assertEqual("Create Job", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::h3[1]").text)
        except:
            print('TEST FAIL : checkImgServiceLogo')
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkImgServiceLogo')

    def test_checkBtnCreateJob(self): # [Create Job]버튼 출력 및 링크 이동 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.moveMainPage(self) # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job]버튼 확인
            self.assertEqual("+ Create job", driver.find_element_by_link_text("+ Create job").text)
            # Jobs Page로 이동
            driver.find_element_by_link_text("Jobs").click()
            time.sleep(3)
            # [Create Job]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Megazone'])[1]/preceding::strong[1]").click()
            time.sleep(3)
            # Create Job 페이지로 이동 확인 (Create Job Title 확인)
            self.assertEqual("Create Job", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::h3[1]").text)
        except:
            print('TEST FAIL : checkBtnCreateJob')
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkBtnCreateJob')

    def test_checkProject(self): # Project 정보 출력 및 링크 이동 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.moveMainPage(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Project 아이콘 확인
            self.assertEqual("Megazone", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Create job'])[1]/following::strong[1]").text)
            # Stage Name 확인 (Megazone)
            self.assertEqual("Continuum", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Megazone'])[1]/following::span[1]").text)
            # Project Name 확인 (Continuum)
            # self.assertEqual("MegazoneContinuum", driver.find_element_by_xpath(
            #   "(.//*[normalize-space(text()) and normalize-space(.)='Create job'])[1]/following::button[1]").text)
            # Project Select Menu 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Create job'])[1]/following::button[1]").click()
            time.sleep(3)
            # Project Select Menu에서 Project 아이콘 확인
            self.assertEqual("Megazone", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Continuum'])[1]/following::strong[1]").text)
            # Project Select Menu에서 Project Name 확인 (Continuum)
            self.assertEqual("Continuum", driver.find_element_by_link_text("Continuum").text)
            # Project Select Menu에서 Project Name 확인 (Demo)
            self.assertEqual("Demo", driver.find_element_by_link_text("Demo").text)
            # Project Select Menu에서 다른 Project 클릭 (Demo)
            driver.find_element_by_link_text("Demo").click()
            time.sleep(3)
            # Demo Project Page로 이동 확인
            self.assertEqual("Demo", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Megazone'])[1]/following::span[1]").text)
        except:
            print('TEST FAIL : checkProject')
            logging.basicConfig(stream=sys.stderr, level=logging.error)
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkProject')

    def test_checkUser(self): # User 정보 출력 및 링크 이동 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.moveMainPage(self) # Project Main page로 이동하는 공통 모듈 호출
            # 사용자 아이콘 확인
            self.assertEqual("sprite sprite-user", driver.find_element_by_class_name('sprite sprite-user').text)
            # 사용자 이름 확인
            self.assertEqual("Megazone (Owner)", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='mcmtestowner@gmail.com'])[1]/preceding::em[1]").text)
            # 사용자 계정 확인
            self.assertEqual("mcmtestowner@gmail.com", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Megazone (Owner)'])[1]/following::small[1]").text)
        except:
            print('TEST FAIL : checkUser')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                'F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkUser')

    def test_clickBtnSignOut(self): # Sign Out 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.moveMainPage(self) # Project Main page로 이동하는 공통 모듈 호출
            # [Sign Out]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/nav/div[2]/div/ul/li[3]/div/button/i").click()
            time.sleep(3)
            # After (Welcome Text 확인)
            self.assertEqual("Welcome!", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='You need to sign in a Megazone Accounts account to get started.'])[1]/preceding::h4[1]").text)
        except:
            print('TEST FAIL : clickBtnSignOut')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                'F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : clickBtnSignOut')

    def test_clickBtnAdmin(self): # Admin 버튼 출력 및 이동 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.moveMainPage(self)  # Project Main page로 이동하는 공통 모듈 호출
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
            print('TEST FAIL : clickBtnAdmin')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                'F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : clickBtnAdmin')

    def test_clickBtnDownloadApps(self):  # Downlaod Apps 버튼 출력 및 이동 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.moveMainPage(self)  # Project Main page로 이동하는 공통 모듈 호출
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
            print('TEST FAIL : clickBtnDownloadApps')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
        else:
            print('TEST PASS : clickBtnDownloadApps')

    def test_checkDownloadAppsPopUp(self): # Downlaod Apps 팝업 구성요소 및 기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.moveMainPage(self) # Project Main page로 이동하는 공통 모듈 호출
            GNB.clickBtnDownloadApps(self) # Download Apps 팝업을 호출하는 함수 호출
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
            print('TEST FAIL : check_checkDownloadAppsPopUp')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
        else:
            print('TEST PASS : check_checkDownloadAppsPopUp')

    def test_checkMyJobs(self): # My Jobs 버튼 출력 및 이동 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.moveMainPage(self) # Project Main page로 이동하는 공통 모듈 호출
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
            print('TEST FAIL : checkMyJobs')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
        else:
            print('TEST PASS : checkMyJobs')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Gnb('test_checkImgServiceLogo'))
    suite.addTest(Gnb('test_checkBtnCreateJob'))
    suite.addTest(Gnb('test_checkProject'))
    suite.addTest(Gnb('test_checkUser'))
    suite.addTest(Gnb('test_clickBtnSignOut'))
    suite.addTest(Gnb('test_clickBtnAdmin'))
    suite.addTest(Gnb('test_clickBtnDownloadApps'))
    suite.addTest(Gnb('test_checkDownloadAppsPopUp'))
    suite.addTest(Gnb('test_checkMyJobs'))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Reports")
    runner.run(suite())