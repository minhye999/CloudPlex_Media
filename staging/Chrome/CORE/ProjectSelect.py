# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class ProjectSelect(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_checkUser(self): # User 정보 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.signInMegazone(self) # Megazone SignIn하는 공통 모듈 호출
            # 사용자 이름 확인
            self.assertEqual("Megazone (Owner)", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='mcmtestowner@gmail.com'])[1]/preceding::em[1]").text)
            # 사용자 계정 확인
            self.assertEqual("mcmtestowner@gmail.com", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Megazone (Owner)'])[1]/following::small[1]").text)
            # 사용자 이름이 출력된 인사 텍스트 확인
            self.assertEqual("Hi, Megazone (Owner)", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='mcmtestowner@gmail.com'])[1]/following::h1[1]").text)
        except:
            print('TEST FAIL : checkUser')
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkUser')

    def test_checkProject(self): # Project 정보 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.signInMegazone(self) # Megazone SignIn하는 공통 모듈 호출
            # Administration 아이콘 확인
            self.assertEqual("Continuum", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Administration'])[1]/following::div[4]").text)
            # Project Icon 확인
            self.assertEqual("", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Continuum'])[1]/following::button[1]").get_attribute(
                "value"))
            # Project Name 확인 (Continuum)
            self.assertEqual("mz-cm-v1", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Continuum'])[1]/following::p[1]").text)
            # Project ID 확인 (Continuum)
            self.assertEqual("mz-cm-v1", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Continuum'])[1]/following::p[1]").text)
            # Project 이동 아이콘 확인 (Continuum)
            #self.assertEqual("Continuummz-cm-v1", driver.find_element_by_link_text("Continuummz-cm-v1").text)
        except Exception as e:
            print('TEST FAIL : checkProject')
            logging.basicConfig(stream=sys.stderr, level=logging.error)
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkProject')

    def test_setAsDefault(self): # Default Project 설정 기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.signInMegazone(self) # Megazone SignIn하는 공통 모듈 호출
            # [...]아이콘 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/ul/li/div/button/i").click()
            # [Set as default] 설정
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Etc'])[1]/following::button[1]").click()
            # Project에 Default 아이콘 출력 확인
            self.assertEqual("Default", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Continuum'])[1]/following::span[1]").text)
            # Default가 설정된 Project로 이동
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Administration'])[1]/following::div[4]").click()
            time.sleep(3)
            # [Sign Out]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/nav/div[2]/div/ul/li[3]/div/button/i").click()
            time.sleep(3)
            # [Sign in]버튼 클릭
            driver.find_element_by_link_text("Sign in with Megazone Accounts").click()
            time.sleep(3)
            # Project Select 과정없이, Default로 설정한 Project의 Stage에 진입하였음을 확인 (Megazone)
            self.assertEqual("Megazone", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Create job'])[1]/following::strong[1]").text)
            # Project Select 과정없이, Default로 설정한 Project에 진입하였음을 확인 (Continuum)
            self.assertEqual("Continuum", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Megazone'])[1]/following::span[1]").text)
        except:
            print('TEST FAIL : setAsDefault')
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : setAsDefault')

    def test_unsetAsDefault(self): # Default Project 설정 해제 기능 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.signInMegazone(self) # Megazone SignIn하는 공통 모듈 호출
            # [...]아이콘 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/ul/li/div/button/i").click()
            # [Set as default] 설정
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Etc'])[1]/following::button[1]").click()
            # [...]아이콘 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/ul/li/div/button/i").click()
            # [Unset default] 설정
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Etc'])[1]/following::button[1]").click()
            # Default가 설정안된 Project로 이동
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Administration'])[1]/following::div[4]").click()
            time.sleep(3)
            # [Sign Out]버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/nav/div[2]/div/ul/li[3]/div/button/i").click()
            time.sleep(3)
            # [Sign in]버튼 클릭
            driver.find_element_by_link_text("Sign in with Megazone Accounts").click()
            time.sleep(3)
            # Project Select 화면으로 이동함 확인

            # Project Name 확인 (Continuum)
            self.assertEqual("mz-cm-v1", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Continuum'])[1]/following::p[1]").text)
            # Project ID 확인 (Continuum)
            self.assertEqual("mz-cm-v1", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Continuum'])[1]/following::p[1]").text)
        except:
            print('TEST FAIL : unsetAsDefault')
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : unsetAsDefault')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(ProjectSelect('test_checkUser'))
    suite.addTest(ProjectSelect('test_checkProject'))
    suite.addTest(ProjectSelect('test_setAsDefault'))
    suite.addTest(ProjectSelect('test_unsetAsDefault'))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="F:/PyCharm/Project/CloudPlex_Media/staging/Test_Results/Reports")
    runner.run(suite())