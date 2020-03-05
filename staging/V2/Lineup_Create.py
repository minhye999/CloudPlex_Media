# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class Lineup_Create(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_check_create_fileSource(self):  # Create lineup 패널 출력요소 확인 (File source선택 시)
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
            # Lineup 영역 최하단 - [Add Lineup] 버튼 확인
            self.assertEqual("Add Lineup", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Add'])[1]/following::strong[1]").text)
            time.sleep(3)
            # [Add Lineup] 버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Add'])[1]/following::strong[1]").click()
            time.sleep(5)
            # Source 패널 Title 확인
            self.assertEqual("Sources", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Megazone Corp.'])[1]/following::span[1]").text)
            time.sleep(3)
            # Assets탭 확인
            self.driver.find_element_by_xpath('//div[@id="root"]/div/div/div[2]/div[2]/div[2]/div/ul/li[1]/a')
            time.sleep(3)
            # Asset검색란에 컨텐츠명 입력 ("자동화 테스트 - 01")
            driver.find_element_by_xpath("//input[@value='']").click()
            time.sleep(5)
            driver.find_element_by_xpath("//input[@value='']").clear()
            driver.find_element_by_xpath("//input[@value='']").send_keys("자동화 테스트 - 01")
            time.sleep(10)
            # 검색버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created'])[1]/following::button[2]").click()
            time.sleep(10)
            # 검색된 해당 Asset리스트 클릭
            driver.find_element_by_xpath("(//input[@type='checkbox'])[3]").click()
            # Create lineup패널 Title 확인
            self.assertEqual("Create lineup", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Listings Create Lineup Asset'])[1]/following::h4[1]").text)
            time.sleep(10)
            # [Cancel]버튼, [Save]버튼, [X]버튼
            self.assertEqual("Cancel", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Create lineup'])[1]/following::button[1]").text)
            time.sleep(5)
            self.assertEqual("Save", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::strong[1]").text)
            time.sleep(5)
            driver.find_element_by_xpath("//div[@id='right-sidebar']/span/i")
            time.sleep(5)
            # [Refresh]버튼
            self.assertEqual("Refresh", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Save'])[1]/following::span[1]").text)
            time.sleep(3)
            # Asset 정보(썸네일)
            driver.find_element_by_xpath("//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[2]/div/div[1]")
            # Asset 정보(MP4라벨)
            self.assertEqual("MP4", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[3]/following::span[1]").text)
            # Asset 정보(Asset Name : 자동화 테스트 - 01)
            driver.find_element_by_xpath(
                "//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/strong")
            # Asset 정보(Duration(00:03:28.028))
            self.assertEqual("Duration", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='자동화 테스트 - 01'])[2]/following::strong[1]").text)
            self.assertEqual(": 00:03:28.028", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Duration'])[3]/following::span[1]").text)
            # Asset 정보(Category(-))
            self.assertEqual("Category", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Duration'])[3]/following::strong[1]").text)
            self.assertEqual(": -", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Category'])[1]/following::span[1]").text)
            time.sleep(3)
            # Name(*)
            self.assertEqual("Name", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Category'])[1]/following::span[2]").text)
            self.assertEqual("*", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Name'])[2]/following::span[1]").text)
            # Schedule 타이틀
            self.assertEqual("Schedule", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::h5[1]").text)
            # Schedule - Time
            self.assertEqual("Time", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Shedule repeat'])[1]/following::h6[1]").text)
            # Schedule - Start time(*)
            self.assertEqual("Start time* ~", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Date'])[1]/following::label[1]").text)
            # Schedule - End time(*)
            self.assertEqual("End time*", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='*'])[4]/following::label[1]").text)
            # Schedule - Program Duration (00:03:28.028)
            self.assertEqual("Program Duration", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='*'])[5]/following::span[4]").text)
            self.assertEqual("00:03:28.028", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Program Duration'])[1]/following::strong[1]").text)
            # Schedule - Contents Duration (00:03:28.028)
            self.assertEqual("Contents Duration", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Program Duration'])[1]/following::span[1]").text)
            self.assertEqual("00:03:28.028", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Contents Duration'])[1]/following::strong[1]").text)
            # Schedule - Repeat(checkbox)
            self.assertEqual("Repeat", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Contents Duration'])[1]/following::strong[2]").text)
            driver.find_element_by_name("Recurrence").is_displayed()
            time.sleep(3)
            # Priority
            self.assertEqual("Priority", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='days'])[1]/following::h5[1]").text)
            # Program 타이틀
            self.assertEqual("Program", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='If the value is the same, next event has the highest priority'])[1]/following::h5[1]").text)
            # Program - Name(*)
            self.assertEqual("Name", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Program'])[1]/following::strong[1]").text)
            self.assertEqual("*", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Name'])[3]/following::span[1]").text)
            # Program - Description 텍스트명
            self.assertEqual("Description", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='*'])[6]/following::strong[1]").text)
            time.sleep(3)
            # Program - Description 입력박스 확인 및 입력
            driver.find_element_by_xpath(
                "//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[6]/div/div[2]/div/div/div/textarea").click()
            time.sleep(5)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Description'])[1]/following::textarea[1]").clear()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Description'])[1]/following::textarea[1]").send_keys(
                u"디스크립션")
            time.sleep(10)
            # Program - Attributions 텍스트명
            self.assertEqual("Attributions", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='디스크립션'])[1]/following::strong[1]").text)
            # Program - Attributions [Add] 버튼 확인
            self.assertEqual("Add", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Attributions'])[1]/following::button[1]").text)
            time.sleep(3)
            # Program - Media(*) MP4라벨
            self.assertEqual("Media *", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Add'])[2]/following::h6[1]").text)
            self.assertEqual("MP4", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='*'])[7]/following::span[1]").text)
            time.sleep(3)
            # Program - Posters 텍스트명
            self.assertEqual("Posters", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='close'])[2]/following::h6[1]").text)
            # Program - Posters [Add Posters] 버튼 확인
            self.assertEqual("Add Posters", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Posters'])[1]/following::button[1]").text)
            time.sleep(3)

        except:
            print('TEST FAIL : check_create_fileSource')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_create_fileSource')

    def test_check_create_stream(self):  # Create lineup 패널 출력요소 확인 (Stream선택 시)
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
            # Lineup 영역 최하단 - [Add Lineup] 버튼 확인
            self.assertEqual("Add Lineup", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Add'])[1]/following::strong[1]").text)
            time.sleep(3)
            # [Add Lineup] 버튼 클릭
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Add'])[1]/following::strong[1]").click()
            time.sleep(5)
            # Source 패널 Title 확인
            self.assertEqual("Sources", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Megazone Corp.'])[1]/following::span[1]").text)
            time.sleep(3)
            # Stream탭 클릭
            driver.find_element_by_link_text("Streams1").click()
            time.sleep(3)
            # Stream리스트 클릭 ("autotest")
            driver.find_element_by_xpath("(//input[@type='checkbox'])[3]").click()
            # Create lineup패널 Title 확인
            self.assertEqual("Create lineup", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Listings Create Lineup Stream'])[1]/following::h4[1]").text)
            time.sleep(10)
            # [Cancel]버튼, [Save]버튼, [X]버튼
            self.assertEqual("Cancel", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Create lineup'])[1]/following::button[1]").text)
            time.sleep(5)
            self.assertEqual("Save", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::strong[1]").text)
            time.sleep(5)
            driver.find_element_by_xpath("//div[@id='right-sidebar']/span/i")
            time.sleep(5)
            # [Refresh]버튼
            self.assertEqual("Refresh", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Save'])[1]/following::span[1]").text)
            time.sleep(3)
            # Stream 정보[RTMP(PUSH)라벨]
            self.assertEqual("RTMP(PUSH)", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[3]/following::span[1]").text)
            # Stream 정보(Stream Name : autotest)
            #driver.find_element_by_xpath("//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/strong")
            self.assertEqual("autotest", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='RTMP(PUSH)'])[2]/following::strong[1]").text)
            # Name(*)
            self.assertEqual("Name *", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='autotest'])[2]/following::h5[1]").text)
            # Schedule 타이틀
            self.assertEqual("Schedule", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::h5[1]").text)
            # Schedule - Time
            self.assertEqual("Time", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Shedule repeat'])[1]/following::h6[1]").text)
            # Schedule - Start time(*)
            self.assertEqual("Start time* ~", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Date'])[1]/following::label[1]").text)
            # Schedule - End time(*)
            self.assertEqual("End time*", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='*'])[4]/following::label[1]").text)
            # Schedule - Program Duration (00:30:00.000)
            self.assertEqual("Program Duration", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='*'])[5]/following::span[4]").text)
            self.assertEqual("00:30:00.000", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Program Duration'])[1]/following::strong[1]").text)
            # Schedule - Contents Duration (00:30:00.000)
            self.assertEqual("Contents Duration", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Program Duration'])[1]/following::span[1]").text)
            self.assertEqual("00:30:00.000", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Contents Duration'])[1]/following::strong[1]").text)
            # Schedule - Repeat(checkbox)
            self.assertEqual("Repeat", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Contents Duration'])[1]/following::strong[2]").text)
            driver.find_element_by_name("Recurrence").is_displayed()
            time.sleep(3)
            # Priority
            self.assertEqual("Priority", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='days'])[1]/following::strong[1]").text)
            # Program 타이틀
            self.assertEqual("Program", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='If the value is the same, next event has the highest priority'])[1]/following::h5[1]").text)
            # Program - Name(*)
            self.assertEqual("Name", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Program'])[1]/following::strong[1]").text)
            self.assertEqual("*", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Name'])[2]/following::span[1]").text)
            # Program - Description 텍스트명
            self.assertEqual("Description", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='*'])[6]/following::strong[1]").text)
            time.sleep(3)
            # Program - Description 입력박스 확인 및 입력
            driver.find_element_by_xpath("//div[@id='right-sidebar']/div/div/div/div[2]/div/div/div[5]/div/div[2]/div/div/div/textarea").click()
            time.sleep(5)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Description'])[1]/following::textarea[1]").clear()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Description'])[1]/following::textarea[1]").send_keys(
                u"디스크립션")
            time.sleep(10)
            # Program - Attributions 텍스트명
            self.assertEqual("Attributions", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='디스크립션'])[1]/following::strong[1]").text)
            # Program - Attributions [Add] 버튼 확인
            self.assertEqual("Add", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Attributions'])[1]/following::button[1]").text)
            time.sleep(3)
            # Program - Media(*) [RTMP(PUSH)라벨]
            self.assertEqual("Media *", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Add'])[2]/following::h6[1]").text)
            self.assertEqual("RTMP(PUSH)", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='*'])[7]/following::span[1]").text)
            time.sleep(3)

        except:
            print('TEST FAIL : check_create_stream')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_create_stream')

    def test_check_create_add_btn(self):  # No lineup - add버튼 클릭하여 lineup 생성 (Asset명 : "자동화 테스트 - 01")
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
            # 달력 패널에서 미래날짜 선택 [현재 날짜(2020-1-7) 기준, 미래 날짜(2020-2-7) 설정 ]
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Sa'])[1]/following::*[name()='svg'][2]").click()
            time.sleep(5)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='February 2020'])[1]/following::td[13]").click()
            time.sleep(5)
            # No Lineup 영역 - [Add] 버튼 확인
            self.assertEqual("Add", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Add Lineup'])[1]/preceding::span[1]").text)
            time.sleep(3)
            # [Add] 버튼 클릭
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Add Lineup'])[1]/preceding::span[1]").click()
            time.sleep(5)
            # Source 패널 Title 확인
            self.assertEqual("Sources", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Megazone Corp.'])[1]/following::span[1]").text)
            time.sleep(3)
            # Assets탭 확인
            self.driver.find_element_by_xpath('//div[@id="root"]/div/div/div[2]/div[2]/div[2]/div/ul/li[1]/a')
            time.sleep(3)
            # Asset검색란에 컨텐츠명 입력 ("자동화 테스트 - 01")
            driver.find_element_by_xpath("//input[@value='']").click()
            time.sleep(5)
            driver.find_element_by_xpath("//input[@value='']").clear()
            driver.find_element_by_xpath("//input[@value='']").send_keys("자동화 테스트 - 01")
            time.sleep(10)
            # 검색버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created'])[1]/following::button[2]").click()
            time.sleep(10)
            # 검색된 해당 Asset리스트 클릭
            driver.find_element_by_xpath("(//input[@type='checkbox'])[3]").click()
            # Create lineup패널 Title 확인
            self.assertEqual("Create lineup", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Listings Create Lineup Asset'])[1]/following::h4[1]").text)
            time.sleep(10)
            # Create lineup패널 - Save 버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::strong[1]").click()
            time.sleep(10)
            # 생성된 스케쥴 Name 확인 ("자동화 테스트 - 01")
            self.assertEqual("자동화 테스트 - 01", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='MP4'])[1]/following::div[1]").text)
            time.sleep(10)

        except:
            print('TEST FAIL : check_create_add_btn')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_create_add_btn')

    def test_check_create_addLineup(self):  # Add Lineup버튼 클릭하여 lineup 생성 (Stream명 : "autotest")
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
            # 달력 패널에서 미래날짜 선택 [현재 날짜(2020-1-7) 기준, 미래 날짜(2020-2-7) 설정 ]
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Sa'])[1]/following::*[name()='svg'][2]").click()
            time.sleep(5)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='February 2020'])[1]/following::td[13]").click()
            time.sleep(5)
            # Lineup 영역 최하단 - [Add Lineup] 버튼 확인
            self.assertEqual("Add Lineup", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Add'])[1]/following::strong[1]").text)
            time.sleep(3)
            # [Add Lineup] 버튼 클릭
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Add'])[1]/following::strong[1]").click()
            time.sleep(5)
            # Source 패널 Title 확인
            self.assertEqual("Sources", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Megazone Corp.'])[1]/following::span[1]").text)
            time.sleep(3)
            # Stream탭 클릭
            driver.find_element_by_link_text("Streams1").click()
            time.sleep(3)
            # Stream리스트 클릭 ("autotest")
            driver.find_element_by_xpath("(//input[@type='checkbox'])[3]").click()
            # Create lineup패널 Title 확인
            self.assertEqual("Create lineup", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Listings Create Lineup Stream'])[1]/following::h4[1]").text)
            time.sleep(10)
            # Create lineup패널 - Save 버튼 클릭
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::strong[1]").click()
            time.sleep(10)
            # 생성된 스케쥴 Name 확인 ("autotest")
            self.assertEqual("autotest", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='RTMP PUSH'])[1]/following::div[1]").text)
            time.sleep(10)

        except:
            print('TEST FAIL : check_create_addLineup')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : check_create_addLineup')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Lineup_Create('test_check_create_fileSource'))
    suite.addTest(Lineup_Create('test_check_create_stream'))
    suite.addTest(Lineup_Create('test_check_create_add_btn'))
    suite.addTest(Lineup_Create('test_check_create_addLineup'))

    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())