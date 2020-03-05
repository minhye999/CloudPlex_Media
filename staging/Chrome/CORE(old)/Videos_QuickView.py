# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class Videos_QuickView(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_check_iconVideo(self):  # Asset 아이콘 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # 유효한 검색어 입력 (ID) > [Search]버튼 클릭
            driver.find_element_by_id("quick-search").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys("1576551212ICoH")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").click()
            time.sleep(3)
            # ID 클릭하여 Quick View 호출
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::p[2]").click()
            time.sleep(3)
            # 아이콘 확인 (Videos)
            self.driver.find_element_by_xpath("//div/h4/i[@class='sprite sprite-bul-video-title']")
        except:
            print('TEST FAIL : test_check_iconVideo')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_iconVideo-%s.png' % now)
        else:
            print('TEST PASS : test_check_iconVideo')

    def test_check_title(self):  # Title 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # 유효한 검색어 입력 (ID) > [Search]버튼 클릭
            driver.find_element_by_id("quick-search").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys("1576551212ICoH")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").click()
            time.sleep(3)
            # ID 클릭하여 Quick View 호출
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::p[2]").click()
            time.sleep(3)
            # 타이틀 확인 (Video)
            self.assertEqual("Video", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Megazone Corp.'])[1]/following::h4[1]").text)
        except:
            print('TEST FAIL : test_check_title')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_title-%s.png' % now)
        else:
            print('TEST PASS : test_check_title')

    def test_check_iconPreview(self):  # priview 아이콘 확인 및 팝업 호출
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # 유효한 검색어 입력 (ID) > [Search]버튼 클릭
            driver.find_element_by_id("quick-search").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys("1576551212ICoH")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").click()
            time.sleep(3)
            # ID 클릭하여 Quick View 호출
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::p[2]").click()
            time.sleep(3)
            # 아이콘 확인 (Preview)
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div/div/div/button/i")
            # Preview 아이콘 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div/div/div/button/i").click()
            # Preview 새창에서 Title 확인 (Title : EXO 엑소 'CALL ME BABY' MV)
            driver.switch_to.window(driver.window_handles[-1])  # 최근 열린 탭으로 전환 (새로 열린 탭으로 활성 탭 변경)
            time.sleep(3)
            self.assertEqual(u"EXO 엑소 'CALL ME BABY' MV", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='MP4'])[1]/following::span[1]").text)
        except:
            print('TEST FAIL : test_check_iconPreview')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_iconPreview-%s.png' % now)
        else:
            print('TEST PASS : test_check_iconPreview')

    def test_check_btn_close(self):  # Title 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # 유효한 검색어 입력 (ID) > [Search]버튼 클릭
            driver.find_element_by_id("quick-search").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys("1576551212ICoH")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").click()
            time.sleep(3)
            # ID 클릭하여 Quick View 호출
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::p[2]").click()
            time.sleep(3)
            # [X]버튼 확인
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div/div/div/button[2]/span/i")
            # [X]버튼 클릭하여 Quick View 닫기
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div/div/div/button[2]/span/i").click()
            # [X]버튼이 없으면 닫힌 것으로 간주
            #
        except:
            print('TEST FAIL : test_check_btn_close')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_btn_close-%s.png' % now)
        else:
            print('TEST PASS : test_check_btn_close')

    def test_check_player(self):  # Player 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # 유효한 검색어 입력 (ID) > [Search]버튼 클릭
            driver.find_element_by_id("quick-search").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys("1576551212ICoH")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").click()
            time.sleep(3)
            # ID 클릭하여 Quick View 호출
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::p[2]").click()
            time.sleep(3)
            # Player 출력 확인
            driver.find_element_by_id("vjs_video_1145_html5_api")
            # [재생]버튼 출력 확인
            self.assertEqual("play", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='progress'])[1]/following::button[1]").text)
            # [재생]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Video Player is loading.'])[1]/following::button[1]").click()
            # 재생중 [일시정지]버튼 출력 확인
            self.assertEqual("paused", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='progress'])[1]/following::button[1]").text)
            # [일시정지]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='progress'])[1]/following::button[1]").click()
            # 일시정지되어 [재생]버튼 출력 확인
            self.assertEqual("play", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='progress'])[1]/following::button[1]").text)
            # 음소거 아이콘 출력 확인
            self.assertEqual("mute", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='replay'])[1]/following::button[1]").text)
            # Default 영상 빠르기 확인 (x1.0)
            self.assertEqual("x1.0", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='|'])[1]/following::button[1]").text)
            # 영상 빠르기 변경 (x1.0 -> 2.0)
            # MZCLOUDMED-6418 Assets_퀵뷰_빠르기 기능안됨
            # [전체화면] 아이콘 출력 확인
            self.assertEqual("fullscreen", driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='세팅'])[1]/following::button[1]").text)
            # [전체화면] 아이콘 클릭
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='세팅'])[1]/following::button[1]").click()
            # [기본화면] 아이콘 클릭
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='세팅'])[1]/following::button[1]").click()
        except:
            print('TEST FAIL : test_check_player')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_player-%s.png' % now)
        else:
            print('TEST PASS : test_check_player')

    def test_check_overview(self):  # Player 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # 유효한 검색어 입력 (ID) > [Search]버튼 클릭
            driver.find_element_by_id("quick-search").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys("1576551212ICoH")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").click()
            time.sleep(3)
            # ID 클릭하여 Quick View 호출
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::p[2]").click()
            time.sleep(3)
            # 탭 확인 (Overview)
            self.assertEqual("Overview", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='close'])[2]/following::span[1]").text)
            # 탭 클릭 (Overview)
            driver.find_element_by_link_text("Overview").click()
            # Data 확인 (Name : EXO 엑소 'CALL ME BABY' MV)
            self.assertEqual("Name", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Metadata'])[1]/following::strong[1]").text)
            self.assertEqual(u"EXO 엑소 'CALL ME BABY' MV", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Name'])[1]/following::span[1]").text)
            # Data 확인 (ID : 1576551212ICoH)
            self.assertEqual("ID", driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)=concat('EXO 엑소 ', \"'\", 'CALL ME BABY', \"'\", ' MV')])[2]/following::strong[1]").text)
            self.assertEqual("1576551212ICoH", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='ID'])[1]/following::span[1]").text)
            # Data 확인 (Status : ACTIVE)
            self.assertEqual("Status", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='ID'])[1]/following::strong[1]").text)
            self.assertEqual("ACTIVE", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Status'])[1]/following::div[1]").text)
            # Data 확인 (Duration : 00:03:56)
            self.assertEqual("Duration", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='MP4'])[2]/following::strong[1]").text)
            self.assertEqual("00:03:56", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Duration'])[1]/following::span[1]").text)
            # Data 확인 (Job ID : 1576550912NUDt)
            self.assertEqual("Job ID", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Size'])[2]/following::strong[1]").text)
            self.assertEqual("1576550912NUDt", driver.find_element_by_link_text("1576550912NUDt").text)
            # Data 확인 (Owner : 이선애(rosa@mz.co.kr)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Job ID'])[1]/following::strong[1]").click()
            self.assertEqual("Owner", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Job ID'])[1]/following::strong[1]").text)
            self.assertEqual(u"이선애(rosa@mz.co.kr)", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Owner'])[1]/following::span[1]").text)
            # Data 확인 (Created : 2019-12-17 11:53:32)
            self.assertEqual("Created", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='(rosa@mz.co.kr)'])[1]/following::strong[1]").text)
            self.assertEqual("2019-12-17 11:53:32", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created'])[1]/following::span[1]").text)
            # Data 확인 (Detail 텍스트)
            self.assertEqual("Detail", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='None'])[2]/following::strong[1]").text)
            # Data 확인 (Detail 이동 아이콘)
            self.driver.find_element_by_xpath("//div/span/i[@class='sprite']")
            # [Detail] 아이콘 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div/div[3]/a/div/span/i").click()
            # Detail 페이지로 이동 확인 (Title 체크)
            self.assertEqual(u"EXO 엑소 'CALL ME BABY' MV", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::span[1]").text)
        except:
            print('TEST FAIL : test_check_overview')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_overview-%s.png' % now)
        else:
            print('TEST PASS : test_check_overview')

    def test_check_metadata(self):  # Player 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # 유효한 검색어 입력 (ID) > [Search]버튼 클릭
            driver.find_element_by_id("quick-search").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys("1576551212ICoH")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").click()
            time.sleep(3)
            # ID 클릭하여 Quick View 호출
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::p[2]").click()
            time.sleep(3)
            # 탭 확인 (Metadata)
            self.assertEqual("Metadata", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Overview'])[1]/following::span[1]").text)
            # 탭 클릭 (Metadata)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Overview'])[1]/following::span[1]").click()
            # Data 확인 (categories : 세훈, 찬열)
            self.assertEqual("Categories", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Metadata'])[1]/following::strong[1]").text)
            self.assertEqual(u"세훈, 찬열", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Categories'])[1]/following::span[1]").text)
            # Data 확인 (Attributions : SM뮤직 : boy group)
            self.assertEqual("Attributions", driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='세훈, 찬열'])[1]/following::strong[1]").text)
            self.assertEqual(u"SM뮤직", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Attributions'])[1]/following::p[1]").text)
            self.assertEqual("boy group", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Attributions'])[1]/following::span[1]").text)
            # Data 확인 (Tags : 자동화테스트)
            self.assertEqual("Tags", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='boy group'])[1]/following::strong[1]").text)
            self.assertEqual(u"자동화테스트", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='SM'])[1]/following::span[1]").text)
            # Data 확인 (People : None)
            self.assertEqual("People", driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='자동화테스트'])[1]/following::strong[1]").text)
            self.assertEqual("None", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='People'])[2]/following::span[1]").text)
            # People 이슈 해결되면 인물 사진/이름 출력으로 대체 필요
            # 사진
            # 이름
            # Custom Metadata 확인 (앨범 : The 2nd Album 'EXODUS')
            self.assertEqual(u"앨범", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='None'])[2]/following::strong[1]").text)
            self.assertEqual("The 2nd Album 'EXODUS'", driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='앨범'])[1]/following::span[1]").text)
        except:
            print('TEST FAIL : test_check_metadata')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_metadata-%s.png' % now)
        else:
            print('TEST PASS : test_check_metadata')

    def test_check_relatedAssets(self):  # Player 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # 유효한 검색어 입력 (ID) > [Search]버튼 클릭
            driver.find_element_by_id("quick-search").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys("1576551212ICoH")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").click()
            time.sleep(3)
            # ID 클릭하여 Quick View 호출
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::p[2]").click()
            time.sleep(3)
            # 탭 확인 (Related Assets)
            self.assertEqual("Related Assets", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Metadata'])[1]/following::span[1]").text)
            # 탭 클릭 (Related Assets)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Metadata'])[1]/following::span[1]").click()
            # MP4 Asset Data 확인 (썸네일)
            self.driver.find_element_by_xpath("//div/span/img[@class='list-thumbnail type-video']")
            # MP4 Asset Data 확인 (MP4)
            self.assertEqual("MP4", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Dubbing'])[1]/following::span[3]").text)
            # MP4 Asset Data 확인 (Asset Name)
            self.assertEqual(u"EXO 엑소 'CALL ME BABY' MV", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='MP4'])[1]/following::strong[1]").text)
            # MP4 Asset Data 확인 (Asset ID)
            self.assertEqual("1576550945AK5a", driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)=concat('EXO 엑소 ', \"'\", 'CALL ME BABY', \"'\", ' MV')])[2]/following::span[1]").text)
            # THUMBNAILS Asset Data 확인 (썸네일)
            self.driver.find_element_by_xpath("//div/img[@class='list-thumbnail type-image']")
            # THUMBNAILS Asset Data 확인 (MP4)
            self.assertEqual("THUMBNAILS", driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)=concat('EXO 엑소 ', \"'\", 'CALL ME BABY', \"'\", ' MV')])[2]/following::span[2]").text)
            # THUMBNAILS Asset Data 확인 (Asset Name)
            self.assertEqual(u"EXO 엑소 'CALL ME BABY' MV", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='THUMBNAILS'])[1]/following::strong[1]").text)
            # THUMBNAILS Asset Data 확인 (Asset ID)
            self.assertEqual("1576550945sR4B", driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)=concat('EXO 엑소 ', \"'\", 'CALL ME BABY', \"'\", ' MV')])[3]/following::span[1]").text)
            # DASH Asset Data 확인 (썸네일)
            self.driver.find_element_by_xpath("//div/span/img[@class='list-thumbnail type-video']")
            # DASH Asset Data 확인 (MP4)
            self.assertEqual("DASH", driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)=concat('EXO 엑소 ', \"'\", 'CALL ME BABY', \"'\", ' MV')])[3]/following::span[3]").text)
            # DASH Asset Data 확인 (Asset Name)
            self.assertEqual(u"EXO 엑소 'CALL ME BABY' MV", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='DASH'])[1]/following::strong[1]").text)
            # DASH Asset Data 확인 (Asset ID)
            self.assertEqual("1576550945WQ8J", driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)=concat('EXO 엑소 ', \"'\", 'CALL ME BABY', \"'\", ' MV')])[4]/following::span[1]").text)
        except:
            print('TEST FAIL : test_check_relatedAssets')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_relatedAssets-%s.png' % now)
        else:
            print('TEST PASS : test_check_relatedAssets')

    def test_check_dubbing(self):  # Player 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # Videos 메뉴로 이동
            driver.find_element_by_link_text("Videos").click()
            time.sleep(3)
            # 유효한 검색어 입력 (ID) > [Search]버튼 클릭
            driver.find_element_by_id("quick-search").click()
            driver.find_element_by_id("quick-search").clear()
            driver.find_element_by_id("quick-search").send_keys("157804115376Zl")
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Quick Search'])[1]/following::span[1]").click()
            time.sleep(3)
            # ID 클릭하여 Quick View 호출
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Refresh'])[1]/following::p[2]").click()
            time.sleep(5)
            # 탭 확인 (Dubbing)
            self.assertEqual("Dubbing", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Related Assets'])[1]/following::span[1]").text)
            # 탭 클릭 (Dubbing)
            driver.find_element_by_link_text("Dubbing").click()
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Related Assets'])[1]/following::span[1]").click()
            # 개수 확인 (Total2)
            self.assertEqual("Total2", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Dubbing'])[1]/following::span[2]").text)
            # 컬럼 확인 (Label)
            self.assertEqual("Label", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Dubbing'])[1]/following::div[4]").text)
            # 컬럼 확인 (Language)
            self.assertEqual("Language", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Label'])[1]/following::div[1]").text)
            # Data 확인 (Label - Chinese)
            self.assertEqual("Chinese", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Language'])[1]/following::span[1]").text)
            # Data 확인 (Language - ZHO)
            self.assertEqual("ZHO", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Chinese'])[2]/following::td[1]").text)
            # Data 확인 (Label - Korean)
            self.assertEqual("Korean", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='ZHO'])[1]/following::span[1]").text)
            # Data 확인 (Language - KOR)
            self.assertEqual("KOR", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Korean'])[2]/following::td[1]").text)
        except:
            print('TEST FAIL : test_check_dubbing')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_dubbing-%s.png' % now)
        else:
            print('TEST PASS : test_check_dubbing')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    '''
    suite.addTest(Videos_QuickView('test_check_iconVideo'))
    suite.addTest(Videos_QuickView("test_check_title"))
    suite.addTest(Videos_QuickView("test_check_iconPreview"))
    suite.addTest(Videos_QuickView("test_check_btn_close"))
    suite.addTest(Videos_QuickView("test_check_player"))
    suite.addTest(Videos_QuickView("test_check_overview"))
    suite.addTest(Videos_QuickView("test_check_metadata")) # people 이슈 해결시 사진/이름 체크하도록 하기
    suite.addTest(Videos_QuickView("test_check_relatedAssets"))
    '''
    suite.addTest(Videos_QuickView("test_check_dubbing")) # 더빙 Data가 있는 것으로 Test Data 변경 필요
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())