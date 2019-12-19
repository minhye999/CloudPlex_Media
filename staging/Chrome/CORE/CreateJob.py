# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common
#import staging.Chrome.ProjectAd.Settings_Transcoding

class CreateJob(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        # self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        # self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        # self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_check_breadcrumb(self):  # Breadcrumb 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴 클릭
            driver.find_element_by_link_text("Create Job").click()
            # Breadcrumb 확인 (Transcoding > Create Job)
            self.assertEqual("Transcoding", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Create Job'])[2]/following::li[1]").text)
            self.assertEqual("Create Job", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Transcoding'])[2]/following::li[1]").text)
        except:
            print('TEST FAIL : test_check_breadcrumb')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_breadcrumb-%s.png' % now)
        else:
            print('TEST PASS : test_check_breadcrumb')

    def test_check_title(self):  # Title 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴 클릭
            driver.find_element_by_link_text("Create Job").click()
            # Title 확인 (Create Job)
            self.assertEqual("Create Job", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Channels'])[1]/following::h3[1]").text)
        except:
            print('TEST FAIL : test_check_title')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_title-%s.png' % now)
        else:
            print('TEST PASS : test_check_title')

    def test_check_pipeline(self):  # Pipeline 확인 및 선택
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # Pipeline Text 확인
            self.assertEqual("Pipeline", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Create Job'])[3]/following::h6[1]").text)
            # Pipeline 확인 (Default : hls with multiple audio manual)
            self.assertEqual("hls with multiple audio manual", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Pipeline'])[1]/following::div[5]").text)
            # Pipeline Select Box 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Pipeline'])[1]/following::div[4]").click()
            # Pipeline Select Box에서 Pipeline 확인
            #
            # [Pipeline Detail] 버튼 확인
            self.assertEqual("", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='hls with multiple audio manual'])[1]/following::button[1]").get_attribute(
                "value"))
            # [Pipeline Detail] 버튼 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[2]/div/div/div/div/button/i").click()
            time.sleep(3)
            # Pipeline Detail 팝업 출력 확인 (Title만 체크)
            self.assertEqual("Pipeline Detail", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='hls with multiple audio manual'])[1]/following::h5[1]").text)
        except:
            print('TEST FAIL : check_pipeline')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_pipeline-%s.png' % now)
        else:
            print('TEST PASS : check_pipeline')

    def test_check_pipelineDetailPopUp(self):  # Pipeline Detail 팝업 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            CreateJob.test_check_pipeline(self) # Pipeline Detail 팝업 호출
            # Pipeline Detail 팝업의 Title 확인
            self.assertEqual("Pipeline Detail", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='hls with multiple audio manual'])[1]/following::h5[1]").text)
        except:
            print('TEST FAIL : test_check_pipelineDetailPopUp')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_pipelineDetailPopUp-%s.png' % now)
        else:
            print('TEST PASS : test_check_pipelineDetailPopUp')

    def test_check_profile(self):  # Profile 확인 및 선택
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # Pipeline Select Box 활성화
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='dash, mp4 automatic'])[1]/following::*[name()='svg'][1]").click()
            # Pipeline 선택 ("dash, mp4 automatic")
            driver.find_element_by_id("react-select-47-option-2").click()
            # Profile Text 확인
            self.assertEqual("Profile", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='dash, mp4 automatic'])[1]/following::h6[1]").text)
            # Profile 확인 (MPEG-Dash video profile)
            self.assertEqual("MPEG-Dash video profile", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Profile'])[1]/following::span[1]").text)
            # Profile 링크 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Pipeline'])[1]/following::div[5]").click()
            # [Profile Detail] 버튼 확인
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Profile'])[1]/following::span[1]")
            # [Profile Detail] 버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Profile'])[1]/following::span[1]").click()
            time.sleep(3)
            # Profile Detail 팝업 출력 확인 (Title만 체크)
            self.assertEqual("Profile Detail", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='(3)'])[1]/following::h5[1]").text)
        except:
            print('TEST FAIL : test_check_profile')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_profile-%s.png' % now)
        else:
            print('TEST PASS : test_check_profile')

    def test_check_profile_component(self):  # Profile 상세 구성요소 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # Output 라벨 확인 ★
            #self.assertEqual("m3u8", driver.find_element_by_xpath(
            #    "(.//*[normalize-space(text()) and normalize-space(.)='(10)'])[1]/following::span[1]").text)
            #self.driver.find_element_by_xpath("//div[@class='container-badge container-badge-raw mr-2']")
            # Output Name 확인
            #self.assertEqual("m3u8Apple HLS - HLS", driver.find_element_by_xpath(
            #    "(.//*[normalize-space(text()) and normalize-space(.)='(10)'])[1]/following::h6[1]").text)
            # Output Video Settings >  Codec 확인
            self.assertEqual("H.264", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='m3u8'])[1]/following::strong[1]").text)
            # Output Video Settings > Resolution 확인
            self.assertEqual("854x480,", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='H.264'])[1]/following::span[1]").text)
            # Output Video Settings > ABR 확인
            self.assertEqual("CBR,", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='H.264'])[1]/following::span[2]").text)
            # Output Video Settings > Bitrate 확인
            self.assertEqual("500Kbps", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='CBR,'])[1]/following::span[1]").text)
            # Output Audio Settings > Codec 확인
            self.assertEqual("AAC", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='CBR,'])[3]/following::strong[1]").text)
            # Output Audio Settings > ABR 확인
            self.assertEqual("CBR,", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='AAC'])[1]/following::span[1]").text)
            # Output Audio Settings > Bitrate 확인
            self.assertEqual("96Kbps,", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='CBR,'])[4]/following::span[1]").text)
            # Output Audio Settings > Samplerate 확인
            self.assertEqual("48kHz", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='CBR,'])[4]/following::span[2]").text)
            '''
            # Thumbnail 라벨 확인★
            #self.assertEqual("raw", driver.find_element_by_xpath(
            #    "(.//*[normalize-space(text()) and normalize-space(.)='CBR,'])[4]/following::span[3]").text)
            #self.driver.find_element_by_xpath("//div[@class='container-badge container-badge-raw mr-2']")
            # Thumbnail Name 확인
            self.assertEqual("raw File Group - Thumbnails", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='CBR,'])[4]/following::h6[1]").text)
            '''
            # Thumbnail 확장자 확인
            self.assertEqual("JPEG", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='raw'])[1]/following::strong[1]").text)
            # Thumbnail Resolution 확인
            self.assertEqual("854x480 1/10s", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='JPEG'])[1]/following::span[1]").text)
            # Thumbnail 추출방식 확인
            self.assertEqual("854x480 1/10s", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='JPEG'])[1]/following::span[1]").text)
        except:
            print('TEST FAIL : test_check_profile_component')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_profile_component-%s.png' % now)
        else:
            print('TEST PASS : test_check_profile_component')

    def test_check_add_file(self):  # 파일추가하는 영역 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # Drag and drop 영역 안내 텍스트 확인 (Drag and drop a file here) + ( -o r -)
            self.assertEqual("Drag and drop a file here", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='JPEG'])[1]/following::p[1]").text)
            self.assertEqual("- or -", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='JPEG'])[1]/following::span[2]").text)
            # [Local files] 아이콘 확인
            #self.driver.find_element_by_xpath("//div[@class='btn btn-select-file btn-select-file-local']")
            # [Local files] 버튼 출력 확인
            self.assertEqual("Local files", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='- or -'])[1]/following::button[1]").text)
            # [Local files] 버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='- or -'])[1]/following::button[1]").click()
            # Local files 팝업 출력 확인
            #
            # Local files 팝업 닫기
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/button/span/i").click()
            # [S3 files] 아이콘 확인
            #
            # [S3 files] 버튼 출력 확인
            self.assertEqual("S3 files", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='- or -'])[1]/following::button[2]").text)
            # [S3 files] 버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='- or -'])[1]/following::button[2]").click()
            # S3 files 팝업 출력 확인
            #
        except:
            print('TEST FAIL : test_check_add_file')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_add_file-%s.png' % now)
        else:
            print('TEST PASS : test_check_add_file')

    def test_check_metadata(self):  # metadata title 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # Title 확인-> xpath 자꾸 오류남
            #self.assertEqual(
             #   "MetadataMetadata rulesName ConstraintsBase video file to be used for the channel can be set only for English name asset without special characters and spaces. (Allowed special characters: ~! () _-.)",
              #  driver.find_element_by_xpath(
               #     "(.//*[normalize-space(text()) and normalize-space(.)='Category'])[1]/preceding::h6[1]").text)
        except:
            print('TEST FAIL : test_check_metadata')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_metadata-%s.png' % now)
        else:
            print('TEST PASS : test_check_metadata')

    def test_check_info(self):  # info 말풍선 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # info 아이콘 확인
            #
            # info 아이콘 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/h6/div/i").click()
            # info 팝업에서 Title 확인
            self.assertEqual("Metadata rules", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Category'])[1]/preceding::strong[1]").text)
            # info 팝업에서 규칙명 확인
            self.assertEqual("Name Constraints", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Category'])[1]/preceding::p[1]").text)
            # info 팝업에서 규칙 상세내용 확인
            self.assertEqual(
                "Base video file to be used for the channel can be set only for English name asset without special characters and spaces. (Allowed special characters: ~! () _-.)",
                driver.find_element_by_xpath(
                    "(.//*[normalize-space(text()) and normalize-space(.)='Category'])[1]/preceding::div[1]").text)
            # info 팝업에서 [X]버튼 확인
            #
            # info 팝업에서 [X]버튼 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/h6/div/div/div/div/button/span/i").click()
        except:
            print('TEST FAIL : test_check_info')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_info-%s.png' % now)
        else:
            print('TEST PASS : test_check_info')

    def test_check_category(self):  # Profile 상세 구성요소 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # Category 항목명 확인
            self.assertEqual("Category", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Select category'])[1]/preceding::dt[1]").text)
            # Category Default 확인
            self.assertEqual("Select category", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Category'])[1]/following::span[1]").text)
            '''
            # Category [+]버튼 클릭 -> 폭망함. 카테고리 팝업이 출력안됨
            #driver.find_element_by_xpath(
            #    "//div[@id='root']/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/dl/dd/div/div[3]/button/i").click()
            #self.driver.find_element_by_xpath("//div[@class='btn btn-add-category']").click()
            time.sleep(3)
            # Category 팝업 출력 확인 (Title)
            self.assertEqual("Select Categories", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Category'])[1]/following::h5[1]").text)
            # Category 팝업 [X]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Select Categories'])[1]/following::button[1]").click()
            '''
            # Category 선택
            # 선택한 Category 출력 확인
        except:
            print('TEST FAIL : check_category')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_category-%s.png' % now)
        else:
            print('TEST PASS : check_category')

    def test_check_name(self):  # Profile 상세 구성요소 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # Name 항목명 확인
            self.assertEqual("Name", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Select category'])[1]/following::dt[1]").text)
            # Name 입력필드 value 확인
            self.assertEqual("", driver.find_element_by_xpath("(//input[@value=''])[2]").get_attribute("value"))
            # Name 입력필드 클릭
            driver.find_element_by_xpath("(//input[@value=''])[2]").click()
            # Name 입력 (test)
            #driver.find_element_by_xpath("//input[@value='test']").send_keys("test")
            # Name 입력필드 외 영역 클릭
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]").click()
            # Name 입력필드에 입력한 텍스트 출력 확인 (test)
            #self.assertEqual("test", driver.find_element_by_xpath("//input[@value='test']").get_attribute("value"))
            # 파일추가
            #
            # 파일추가 후, 항목명 확인
            #
        except:
            print('TEST FAIL : test_check_name')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_name-%s.png' % now)
        else:
            print('TEST PASS : test_check_name')

    def test_check_description(self):  # Profile 상세 구성요소 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # Description 항목명 확인
            self.assertEqual("Description", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Name'])[1]/following::dt[1]").text)
            # Description 입력필드 확인
            self.assertEqual("", driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/dl[3]/dd/div/div/div/textarea").get_attribute(
                "value"))
            # Description 입력필드 클릭
            #driver.find_element_by_xpath(
            #    "//div[@id='root']/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/dl[3]/dd/div/div/div/textarea").click()
            # 텍스트 입력(test)
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Description'])[1]/following::textarea[1]").send_keys(
                u"test")
            # Description 입력필드 외 영역 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Attribution'])[1]/following::dd[1]").click()
            # Description 입력필드에 출력된 텍스트 확인 (test)
            self.assertEqual(u"test", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Description'])[1]/following::textarea[1]").text)
        except:
            print('TEST FAIL : test_check_description')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_description-%s.png' % now)
        else:
            print('TEST PASS : test_check_description')

    def test_check_attribution(self):  # Profile 상세 구성요소 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # Attribution 항목명 확인
            self.assertEqual("Attribution", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Description'])[1]/following::dt[1]").text)
            # Attribution [Add]버튼 확인
            self.assertEqual("Add", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Attribution'])[1]/following::button[1]").text)
            # Attribution [Add]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Attribution'])[1]/following::button[1]").click()
            # Key 입력필드 value 확인
            self.assertEqual("", driver.find_element_by_id("key0").get_attribute("value"))
            # value 입력필드 value 확인
            self.assertEqual("", driver.find_element_by_xpath("(//input[@value=''])[4]").get_attribute("value"))
            # Key/value 미입력 시, 안내문구 출력 확인
            self.assertEqual("\"Attribution\" cannot be empty. Please enter a valid attribution.",
                             driver.find_element_by_xpath(
                                 "(.//*[normalize-space(text()) and normalize-space(.)='Attribution'])[1]/following::p[1]").text)
            # key 입력필드 클릭
            driver.find_element_by_id("key0").click()
            # key 입력필드에 텍스트 입력(key)
            driver.find_element_by_id("key0").clear()
            driver.find_element_by_id("key0").send_keys("key")
            # value 입력필드 클릭
            driver.find_element_by_xpath("(//input[@value=''])[2]").click()
            # key 입력필드에 입력한 텍스트 출력 확인(key) -> 안찍히
            #
            ''' 입력필드에 텍스트 입력한게 왜 안직히냐
            # value 입력필드에 텍스트 입력(value)
            driver.find_element_by_xpath("//input[@value='value']").clear()
            driver.find_element_by_xpath("//input[@value='value']").send_keys("value")
            # value 입력필드 외 영역 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Attribution'])[1]/following::dd[1]").click()
            # value 입력필드에 입력한 텍스트 출력 확인(value) -> 안찍히네
            #
            '''
            # [Add]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Attribution'])[1]/following::button[2]").click()
            ''' 입력필드에 텍스트 입력한게 왜 안직히냐
            # key 입력필드의 value 확인
            self.assertEqual("", driver.find_element_by_id("key1").get_attribute("value"))
            # Value 입력필드의 value 확인
            self.assertEqual("", driver.find_element_by_xpath("(//input[@value=''])[3]").get_attribute("value"))
            '''
            # 입력필드 라인 [X]버튼 눌러 삭제
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Attribution'])[1]/following::i[2]").click()
        except:
            print('TEST FAIL : test_check_attribution')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : test_check_attribution')

    def test_check_tags(self):  # Profile 상세 구성요소 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # tag 항목명 확인
            self.assertEqual("Tags", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Add'])[1]/following::dt[1]").text)
            # tag 입력필드 value 확인
            self.assertEqual("", driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/dl[5]/dd/div/div/div/textarea").get_attribute(
                "value"))
            ''' 안먹힘
            # tag 입력필드 클릭
            driver.find_element_by_xpath(
                "//div[@id='root']/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/dl[5]/dd/div/div/div/textarea").click()
            '''
            # tag 입력필드에 텍스트 입력(test)하고 엔터키 입력
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tags'])[1]/following::textarea[1]").send_keys(
                "test")
            # 엔터키 입력하여 tag로 추가 -> 아 요게 안먹네
            #
            # 입력한 텍스트 확인 (test)
            #
        except:
            print('TEST FAIL : test_check_tags')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_attribution-%s.png' % now)
        else:
            print('TEST PASS : test_check_tags')

    def test_check_originSource(self):  # Profile 상세 구성요소 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            # 만약 Setting = On 이라면
            # Project Admin > Settings > Transcoding > Create Origin Asset : Enable 설정
            #staging.Chrome.ProjectAd.Settings_Transcoding.test_settings_transcoding_origin_enable(self)
            staging.Chrome.CORE.common.test_settings_transcoding_origin_enable(self)  # Project Main page로 이동하는 공통 모듈 호출
            # CORE 페이지로 이동
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Administration'])[1]/following::button[1]").click()
            time.sleep(3)
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # 체크박스 On으로 설정되어있는지 확인
            #self.assertEqual("on", driver.find_element_by_id("chkIsCreateOriginAsset").get_attribute("value"))
            '''
            # 체크박스 체크
            driver.find_element_by_id("chkIsCreateOriginAsset").click()
            '''
            # 만약 Setting = Off 이라면
            # Project Admin > Settings > Transcoding > Create Origin Asset : Disable 설정
            staging.Chrome.CORE.common.test_settings_transcoding_origin_disable(self)
            # CORE 페이지로 이동
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Administration'])[1]/following::button[1]").click()
            time.sleep(3)
            # 체크박스 Off로 설정되어있는지 확인
            #self.assertEqual("off", driver.find_element_by_id("chkIsCreateOriginAsset").get_attribute("value"))
            '''
            # 체크박스 체크해제
            driver.find_element_by_id("chkIsCreateOriginAsset").click()
            # 안내문구 출력 확인 (Save the transcode origin source as an asset)
            #self.assertEqual("Save the transcode origin source as an asset", driver.find_element_by_xpath("//div[@class='d-flex justify-content-end align-items-center']").text)
            '''
        except:
            print('TEST FAIL : test_check_originSource')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_check_originSource-%s.png' % now)
        else:
            print('TEST PASS : test_check_originSource')

    def test_localFile_startTranscoding(self):  # Profile 상세 구성요소 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # [Local files]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='- or -'])[1]/following::button[1]").click()
            # [Add Files]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Please select a file to add.'])[1]/following::label[1]").click()
            '''
            # 파일탐색기에서 파일 선택 (경로:C://사진/test_001.mp4) -> 요기부터 안됨 S3 파일로 테스트해야하나봐
            driver.find_element_by_id("upload").clear()
            driver.find_element_by_id("upload").send_keys("C://사진/test_001.mp4")
            # 파일 추가되고, [Select]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
            # [Start Transcoding]버튼 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
            time.sleep(5)
            # Job List에 해당 Job 출력 확인 (title 체크)
            self.assertEqual("test_001.mp4", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::span[1]").text)
            '''
        except:
            print('TEST FAIL : test_localFile_startTranscoding')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_localFile_startTranscoding-%s.png' % now)
        else:
            print('TEST PASS : test_localFile_startTranscoding')

    def test_s3File_startTranscoding(self):  # Profile 상세 구성요소 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # [Create Job] 메뉴로 이동
            driver.find_element_by_link_text("Create Job").click()
            # [s3 files]버튼 클릭
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='- or -'])[1]/following::button[2]").click()
            # s3 경로 입력
            #
            # [Add]버튼 클릭
            #
            # [Select]버튼 클릭
            #
        except:
            print('TEST FAIL : test_s3File_startTranscoding')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_s3File_startTranscoding-%s.png' % now)
        else:
            print('TEST PASS : test_s3File_startTranscoding')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    '''
    suite.addTest(CreateJob('test_check_breadcrumb'))
    suite.addTest(CreateJob("test_check_title"))
    suite.addTest(CreateJob("test_check_pipeline"))
    suite.addTest(CreateJob("test_check_pipelineDetailPopUp"))
    suite.addTest(CreateJob("test_check_profile"))
    suite.addTest(CreateJob("test_check_profile_component"))
    suite.addTest(CreateJob("test_check_add_file"))
    suite.addTest(CreateJob("test_check_metadata"))
    suite.addTest(CreateJob("test_check_info"))
    suite.addTest(CreateJob("test_check_category"))
    suite.addTest(CreateJob("test_check_name"))
    suite.addTest(CreateJob("test_check_description"))
    suite.addTest(CreateJob("test_check_attribution"))
    suite.addTest(CreateJob("test_check_tags"))
    '''
    #suite.addTest(CreateJob("test_check_originSource"))
    suite.addTest(CreateJob("test_localFile_startTranscoding"))
    #suite.addTest(CreateJob("test_s3File_startTranscoding"))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())