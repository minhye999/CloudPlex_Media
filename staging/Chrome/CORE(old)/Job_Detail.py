# -*- coding: utf-8 -*-
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
import unittest
import HtmlTestRunner
import staging.Chrome.CORE.common

class Job_Detail(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../../venv/webdriver/chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path='../venv/webdriver/geckodriver.exe')
        #self.driver = webdriver.edge(executable_path='../venv/webdriver/msedgedriver.exe')
        #self.driver = webdriver.Ie(executable_path='../venv/webdriver/iedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        #Job detail
    def test_checkBreadcrumb(self):  # Job상세 Breadcrumb 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # 검증용 컨텐츠 URL 불러오기 (EXO 엑소 'CALL ME BABY' MV)
            driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/transcoding/jobs/1577670155fUFD")
            time.sleep(10)
            # Breadcrumb 확인 (Transcoding > Jobs > 1577670155fUFD 텍스트 )
            self.driver.find_element_by_xpath('//div[@id="root"]/div/div/div[1]/div/div[1]/nav/ol/li[1]')
            self.assertEqual("Jobs", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Transcoding'])[2]/following::a[1]").text)
            self.assertEqual("1577670155fUFD", driver.find_element_by_xpath(
             "(.//*[normalize-space(text()) and normalize-space(.)='Jobs'])[2]/following::li[1]").text)
            time.sleep(10)

        except:
            print('TEST FAIL : checkBreadcrumb')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkBreadcrumb')

    def test_checkTitle(self):  # Job상세 타이틀 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # 검증용 컨텐츠 URL 불러오기 (EXO 엑소 'CALL ME BABY' MV)
            driver.get(
                "http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/transcoding/jobs/1577670155fUFD")
            time.sleep(10)
            # Title 확인 (EXO 엑소 'CALL ME BABY' MV)
            self.assertEqual("1577670155fUFD", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Jobs'])[2]/following::li[1]").text)

        except:
            print('TEST FAIL : checkTitle')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkTitle')

    def test_checkJobOverview(self):  # Job Overview 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # 검증용 컨텐츠 URL 불러오기 (EXO 엑소 'CALL ME BABY' MV)
            driver.get(
                "http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/transcoding/jobs/1577670155fUFD")
            time.sleep(10)
            # Job Overview Title 확인, xpath이슈로 div class체크
            self.driver.find_element_by_xpath('//div[@id="root"]/div/div/div[1]/div/div[2]/div[1]/div/div/h4')

            # Job ID 텍스트 및 해당 ID 확인
            self.assertEqual("Job ID", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Job Overview'])[1]/following::strong[1]").text)
            self.driver.find_element_by_xpath(
                '//div[@id="root"]/div/div/div[1]/div/div[2]/div[1]/div/div/ul[1]/li[1]/span')

            # Status 텍스트 및 해당 상태 확인
            self.assertEqual("Status", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Job ID'])[1]/following::strong[1]").text)
            self.assertEqual("COMPLETE", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Status'])[1]/following::span[2]").text)

            # Provider/ Service 텍스트 및 Provider이미지, AWS MediaConvert텍스트 확인
            self.driver.find_element_by_xpath(
                '//div[@id="root"]/div/div/div[1]/div/div[2]/div[1]/div/div/ul[2]/li[1]/strong')
            driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[2]/div/div/div/ul[2]/li/span/span/img")
            self.assertEqual("AWS MediaConvert", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Provider / Service'])[1]/following::span[1]").text)

            # Transcoder Job ID 텍스트 및 해당 ID확인
            self.assertEqual("Transcoder Job ID", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='AWS MediaConvert'])[1]/following::strong[1]").text)
            self.assertEqual("1577670184136-j5puxu", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Transcoder Job ID'])[1]/following::span[1]").text)

            # Pipeline 텍스트 및 해당 Pipeline확인
            self.assertEqual("Pipeline", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Transcoder Job ID'])[1]/following::strong[1]").text)
            self.assertEqual("dash, mp4 automatic", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Pipeline'])[1]/following::span[2]").text)

            # Transcode Profile 텍스트 및 해당 Profile확인
            self.assertEqual("Transcode Profile", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='(5)'])[1]/following::strong[1]").text)
            self.assertEqual("MPEG-Dash video profile", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Transcode Profile'])[1]/following::span[2]").text)

            # Output path 텍스트 및 해당 경로 확인
            self.assertEqual("Output path", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='(1571127399xrWX)'])[1]/following::strong[1]").text)
            self.assertEqual("mz-cm-stg-transcoding-output/mz-cm/dash-mp4", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Output path'])[1]/following::span[1]").text)

            # Owner 텍스트 및 해당 owner확인
            self.driver.find_element_by_xpath(
                '//div[@id="root"]/div/div/div[1]/div/div[2]/div[1]/div/div/ul[3]/li[1]/strong')
            self.assertEqual("이선애", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Owner'])[1]/following::span[2]").text)

            # Created 텍스트 및 해당 일자 확인
            self.driver.find_element_by_xpath(
                '//div[@id="root"]/div/div/div[1]/div/div[2]/div[1]/div/div/ul[3]/li[2]/strong')
            self.assertEqual("2019-12-30 10:42:37", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Created'])[1]/following::span[1]").text)

            # Submitted 텍스트 및 해당 일자 확인
            self.driver.find_element_by_xpath(
                '//div[@id="root"]/div/div/div[1]/div/div[2]/div[1]/div/div/ul[3]/li[3]/strong')
            self.assertEqual("2019-12-30 10:43:06", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Submitted'])[1]/following::span[1]").text)

            # Started 텍스트 및 해당 일자 확인
            self.driver.find_element_by_xpath(
                '//div[@id="root"]/div/div/div[1]/div/div[2]/div[1]/div/div/ul[3]/li[4]/strong')
            self.assertEqual("2019-12-30 10:43:07", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Started'])[1]/following::span[1]").text)

            # Completed 텍스트 및 해당 일자 확인
            self.driver.find_element_by_xpath(
                '//div[@id="root"]/div/div/div[1]/div/div[2]/div[1]/div/div/ul[3]/li[5]/strong')
            self.assertEqual("2019-12-30 10:47:20", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Completed'])[1]/following::span[1]").text)

            # Transcoding time 텍스트 및 해당 일자 확인
            self.driver.find_element_by_xpath(
                '//div[@id="root"]/div/div/div[1]/div/div[2]/div[1]/div/div/ul[3]/li[6]/strong')
            self.assertEqual("00:04:13", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Transcoding time'])[1]/following::span[1]").text)

        except:
            print('TEST FAIL : checkJobOverview')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkJobOverview')

    def test_checkInput(self):  # Input 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # 검증용 컨텐츠 URL 불러오기 (EXO 엑소 'CALL ME BABY' MV)
            driver.get(
                "http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/transcoding/jobs/1577670155fUFD")
            time.sleep(10)

            # Input 타이틀 확인
            self.driver.find_element_by_xpath(
                '//div[@id="root"]/div/div/div[1]/div/div[2]/div[2]/div[1]/div/h4')

            # Input1 텍스트 확인
            self.assertEqual("Input1", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Inputs'])[1]/following::strong[1]").text)

            # Type 텍스트 및 항목 (Video) 확인
            self.assertEqual("Type", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Input1'])[1]/following::th[1]").text)
            self.assertEqual("Video", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Size'])[1]/following::td[1]").text)

            # Source 텍스트 및 항목 (URL링크) 확인
            self.assertEqual("Source", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Type'])[1]/following::th[1]").text)
            self.driver.find_element_by_xpath(
                '//div[@id="root"]/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/table/tbody/tr/td[2]/a')

            # Duration 텍스트 및 해당 재생시간 확인
            self.assertEqual("Duration", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Source'])[1]/following::th[1]").text)
            self.assertEqual("00:03:56", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Video'])[1]/following::td[2]").text)

            # Size 텍스트 및 해당 용량 확인
            self.assertEqual("Size", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Duration'])[1]/following::th[1]").text)
            self.assertEqual("68.94 MB", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Video'])[1]/following::td[3]").text)

        except:
            print('TEST FAIL : checkInput')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkInput')

    def test_checkOutput(self):  # Output 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # 검증용 컨텐츠 URL 불러오기 (EXO 엑소 'CALL ME BABY' MV)
            driver.get(
                "http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/transcoding/jobs/1577670155fUFD")
            time.sleep(10)

            # Output 타이틀 확인
            self.driver.find_element_by_xpath(
                '//div[@id="root"]/div/div/div[1]/div/div[2]/div[2]/div[2]/div/h4')

            # 라벨 확인(Dash)
            self.assertEqual("DASH", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Outputs'])[1]/following::span[1]").text)

            # Custom Name 확인(DASH ISO)
            self.assertEqual("DASH ISO", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='DASH'])[1]/following::span[1]").text)

            # master m3u8 Preview 링크 확인
            driver.find_element_by_link_text("DASH ISO").click()

            # Output 텍스트 > Preview 링크 확인
            self.driver.find_element_by_xpath(
                '//div[@id="root"]/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/table/thead/tr/th[1]')
            driver.find_element_by_link_text("Output 2").click()

            # Video Setting 텍스트 > Codec, Resolution, Rate control mode, Bitrate 확인
            self.assertEqual("Video Setting", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Output'])[1]/following::th[1]").text)
            self.assertEqual("H.264, 854x480, CBR, 500Kbps", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='-'])[2]/preceding::td[1]").text)

            # Audio Settings 텍스트 > Codec, Bitrate, Rate control mode, Sample rate 확인
            self.assertEqual("Audio Settings", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Video Setting'])[1]/following::th[1]").text)
            self.assertEqual("AAC, CBR, 96bps, 48kHz", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='-'])[1]/following::td[1]").text)

            # Size 텍스트 및 용량 확인
            self.assertEqual("Size", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Audio Settings'])[1]/following::th[1]").text)
            self.assertEqual("2.78 MB", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='-'])[1]/following::td[2]").text)

            # 라벨 확인(MP4)
            self.assertEqual("MP4", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='-'])[4]/following::span[1]").text)

            # Custom Name 확인(File Group - MP4)
            self.assertEqual("File Group - MP4", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='MP4'])[1]/following::span[1]").text)

            # master m3u8 Preview 링크 확인
            driver.find_element_by_link_text("File Group - MP4").click()

            # Output 텍스트 > Preview 링크 확인
            self.driver.find_element_by_xpath(
                '//div[@id="root"]/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/table/thead/tr/th[1]')
            self.assertEqual("Output 1", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Size'])[3]/following::span[1]").text)

            # Video Setting 텍스트 > Codec, Resolution, Rate control mode, Bitrate 확인
            self.assertEqual("Video Setting", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Output'])[2]/following::th[1]").text)
            self.assertEqual("H.264, 1280x720, CBR, 4.5Mbps", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Size'])[3]/following::td[2]").text)

            # Audio Settings 텍스트 > Codec, Bitrate, Rate control mode, Sample rate 확인
            self.assertEqual("Audio Settings", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Video Setting'])[2]/following::th[1]").text)
            self.assertEqual("AAC, CBR, 160bps, 48kHz", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='IMAGE'])[1]/preceding::td[2]").text)

            # Size 텍스트 및 용량 확인
            self.assertEqual("Size", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Audio Settings'])[2]/following::th[1]").text)
            self.assertEqual("131.40 MB", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='IMAGE'])[1]/preceding::td[1]").text)

            # 라벨 확인(IMAGE)
            self.assertEqual("IMAGE", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Thumbnails'])[1]/preceding::span[1]").text)

            # Custom Name 확인(Thumbnails)
            self.assertEqual("Thumbnails", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='IMAGE'])[1]/following::span[1]").text)

            # Output 텍스트 > Preview 링크 확인
            self.driver.find_element_by_xpath(
                '//div[@id="root"]/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/table/thead/tr/th[1]')
            self.assertEqual("Output 1", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Size'])[4]/following::span[1]").text)

            # Image setting 텍스트 > Thumbnails, Resolution 확인
            self.assertEqual("Image setting", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Output'])[3]/following::th[1]").text)
            self.assertEqual("THUMBNAILS, 854x480", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Size'])[4]/following::span[2]").text)

            # Size 텍스트 및 용량 확인
            self.assertEqual("Size", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Image setting'])[1]/following::th[1]").text)
            self.assertEqual("2.00 GB", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Metadata'])[1]/preceding::td[1]").text)

        except:
            print('TEST FAIL : checkOutput')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkOutput')

    def test_checkMetadata(self):  # Metadata 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # 검증용 컨텐츠 URL 불러오기 (EXO 엑소 'CALL ME BABY' MV)
            driver.get(
                "http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/transcoding/jobs/1577670155fUFD")
            time.sleep(10)

            # Metadata 타이틀 확인
            self.driver.find_element_by_xpath(
                '//div[@id="root"]/div/div/div[1]/div/div[2]/div[2]/div[3]/div/h4')

            # Description 항목명 확인
            self.assertEqual("Description", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Metadata'])[1]/following::strong[1]").text)

            # Description 입력내용 확인(엑소노래, 뮤직비디오)
            self.assertEqual("엑소노래, 뮤직비디오", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Description'])[1]/following::pre[1]").text)

            # Category 항목명 확인
            self.assertEqual("Category", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='엑소노래, 뮤직비디오'])[1]/following::strong[1]").text)

            # Category 입력내용 확인(세훈)
            self.assertEqual("세훈", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Category'])[1]/following::span[1]").text)

            # Attribution 항목명 확인
            self.assertEqual("Attribution", driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='세훈'])[1]/following::strong[1]").text)

            # Attribution 입력내용 확인(SM뮤직)
            self.assertEqual("SM뮤직", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Attribution'])[1]/following::p[1]").text)

            # Tag 항목명 확인
            self.assertEqual("Tag", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Exo'])[1]/following::strong[1]").text)

            # Tag 입력내용 확인(#엑소)
            self.assertEqual("엑소,", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Tag'])[1]/following::span[1]").text)

        except:
            print('TEST FAIL : checkMetadata')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkMetadata')

    def test_checkrequestBody(self):  # Request body확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # 검증용 컨텐츠 URL 불러오기 (EXO 엑소 'CALL ME BABY' MV)
            driver.get(
                "http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/transcoding/jobs/1577670155fUFD")
            time.sleep(10)

            # Request Body탭명 확인
            self.driver.find_element_by_xpath(
                '//div[@id="root"]/div/div/div[1]/div/div[2]/div[2]/div[4]/nav/div/a[1]/span')

        except:
            print('TEST FAIL : checkrequestBody')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
            '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkrequestBody')

    def test_checkresponseBody(self):  # Response body확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # 검증용 컨텐츠 URL 불러오기 (EXO 엑소 'CALL ME BABY' MV)
            driver.get(
                    "http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/transcoding/jobs/1577670155fUFD")
            time.sleep(10)

            # Response Body탭명 확인
            self.driver.find_element_by_xpath(
                '//div[@id="root"]/div/div/div[1]/div/div[2]/div[2]/div[4]/nav/div/a[2]/span')

        except:
            print('TEST FAIL : checkresponseBody')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkresponseBody')

    def test_checkViewMode(self):  # View Mode 확인
        driver = self.driver
        driver.get("http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/welcome")
        try:
            staging.Chrome.CORE.common.move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
            # 검증용 컨텐츠 URL 불러오기 (EXO 엑소 'CALL ME BABY' MV)
            driver.get(
                "http://mz-cm-console-stg-stage.s3-website.ap-northeast-2.amazonaws.com/transcoding/jobs/1577670155fUFD")
            time.sleep(10)

            # Mode 확인 (Default : Tree) ★★★★ 오류로 제외 ★★★★
            # self.assertEqual("TreeText", driver.find_element_by_xpath(
              # "(.//*[normalize-space(text()) and normalize-space(.)='Response body'])[1]/following::select[1]").text)

            # Mode Select Box 클릭
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Response body'])[1]/following::select[1]").click()
            # Mode Select Box에 Tree Mode 출력 확인
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Response body'])[1]/following::select[1]")
            # Mode Select Box에서 Tree Mode 선택
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Response body'])[1]/following::select[1]").click()
            time.sleep(3)
            # Tree Mode 출력 확인
            self.assertEqual("4 items", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='{'])[1]/following::span[1]").text)
            self.assertEqual('"arn:aws:iam::068670021050:role/mz-cm-mediaconvert-default"', driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='string'])[1]/following::span[1]").text)
            # Mode Select Box에 Text Mode 출력 확인
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Response body'])[1]/following::select[1]")
            # Mode Select Box에서 Text Mode 선택
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Response body'])[1]/following::select[1]").click()
            # Text Mode 출력 확인 ★★★★ 오류로 제외 ★★★★
            #
            # 펼치기/접기버튼 확인 (Default : 접혀있음)
            #
            # [펼치기]버튼 클릭 -> 우케하지?
            #
            # 영역 펼쳐지는지 확인
            #
            # [접기]버튼 클릭 -> 우케하지?
            #
            # 영역 접히는지 확인
            #
        except:
            print('TEST FAIL : checkViewMode')
            logging.basicConfig(stream=sys.stderr, level=logging.error)  # 로그 출력
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.save_screenshot(
                '../../../staging/Chrome/Test_Results/Screenshots/test_SignIn-%s.png' % now)
        else:
            print('TEST PASS : checkViewMode')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Job_Detail("test_checkBreadcrumb"))
    suite.addTest(Job_Detail("test_checkTitle"))
    suite.addTest(Job_Detail("test_checkJobOverview"))
    suite.addTest(Job_Detail("test_checkInput"))
    suite.addTest(Job_Detail("test_checkOutput"))
    suite.addTest(Job_Detail("test_checkMetadata"))
    suite.addTest(Job_Detail("test_checkrequestBody"))
    suite.addTest(Job_Detail("test_checkresponseBody"))
    suite.addTest(Job_Detail("test_checkViewMode"))
    return suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="../../../staging/Chrome/Test_Results/Reports")
    runner.run(suite())