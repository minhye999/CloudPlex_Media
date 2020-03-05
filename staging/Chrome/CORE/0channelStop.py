# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner

class ChannelStop(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_channel_stop(self): # Service Logo 출력 및 링크 이동 확인
        driver = self.driver
        driver.get("https://console.media.stg.continuum.co.kr/welcome")
        try:
            # 로그인
            driver.find_element_by_link_text("Sign in with Megazone Accounts").click()
            driver.find_element_by_id("username").click()
            driver.find_element_by_id("username").clear()
            driver.find_element_by_id("username").send_keys("minhye9@mz.co.kr")
            driver.find_element_by_xpath("//button[@type='button']").click()
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys("1q2w3e4r5t")
            driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
            time.sleep(3)
            # Continuum 프로젝트로 진입 (Admin 아이콘으로 진입안되는 오류 짜증남)
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/ul/li[3]/a/div/div").click()
            time.sleep(3)
            # Header : [Administrator] 선택하여 Admin 페이지로 이동
            driver.find_element_by_xpath("//div[@id='root']/div/nav/div[2]/div/ul/li[4]/div/div/button/i").click()
            driver.find_element_by_link_text("Administrator").click()
            time.sleep(3)
            # Channels 페이지로 이동
            driver.find_element_by_link_text("Channels").click()
            time.sleep(3)
            # State 셀렉트박스 클릭
            #driver.find_element_by_xpath("//div[@id='k7c0bznb']/div/div").click()   #요기서 막힘
            #driver.find_element_by_xpath("//div/svg[@class='css-19bqh2r']").click() #요것도 안됨
            driver.find_elements_by_xpath(
                "//div[@class='css-16pqwjk-indicatorContainer select2-selection__indicator select2-selection__dropdown-indicator']")[3].click() # ★ elements와 [3] 의 조합으로 찾음
            # State : [Running] 선택
            driver.find_element_by_id("react-select-6-option-3").click()
            # [Search]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div/form/div/div[2]/div/div/button/span").click()
            time.sleep(5)
            # 만약 검색결과가 없으면, 종료 (Empty Channels. 문구 출력)
            if driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[3]/div/div/div[2]/table/tbody/tr/td").text == "Empty Channels.":
                print("Running인 Channel이 없으므로 종료")
            # 검색결과가 있으면, Channel [stop]버튼을 클릭
            else:
                stop_btn_xpath = "//div[@id='root']/div/div/div/div/div[3]/div/div/div[2]/table/tbody/tr/td[11]/div/button/span" # 반복으로 쓸 아이이므로 변수 만들기
                print(driver.find_elements_by_xpath(stop_btn_xpath)) # 검색된 Channel의 session / element 정보를 Console에 표시 (print문 말고 로그 출력 함수로 바꾸거나 제거 할 것!)
                print(len(driver.find_elements_by_xpath(stop_btn_xpath))) # 검색된 Channel의 개수를 Console에 표시

                # [Stop]버튼이 다 눌러질 때 까지 반복. <= 마지막 [Stop] 버튼이 안 눌러지는 경우 있기 때문에 어쩔수없이 반복을 돌려야함
                while len(driver.find_elements_by_xpath(stop_btn_xpath)) > 0:         # Running인 Channel의 개수가 0보다 크면 계속 반복 돌려라
                    for stop_btn in driver.find_elements_by_xpath(stop_btn_xpath):    # [Stop]버튼 클릭하는 작업을
                        stop_btn.click()
        except:
            print('TEST FAIL : test_channel_stop')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot('../../../staging/Chrome/Test_Results/Screenshots/test_channel_stop-%s.png' % now)
        else:
            print('TEST PASS : test_channel_stop')

    def get_stop_btns(driver, xpath):
        return list

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(ChannelStop('test_channel_stop'))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())