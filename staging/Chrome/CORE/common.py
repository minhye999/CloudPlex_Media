import time

# 로그인
def signIn_megazone(self):
    print("Calling up a signin_Megazone Module") # 해당 모듈 호출되었음을 안내
    driver = self.driver
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div[2]/form/div[1]/a').click()
    driver.find_element_by_xpath('//*[@id="username"]').send_keys('mcmtestowner@gmail.com')
    driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div/div/div[2]/div[4]/button').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('Megazone1!')
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='로그인'])[1]/following::strong[1]").click()
    time.sleep(5)

# 로그인 > Project 선택 > Project 메인 페이지로 이동
def move_main(self):
    print("Calling up a move_main Module") # 해당 모듈 호출되었음을 안내
    driver = self.driver
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div[2]/form/div[1]/a').click()
    driver.find_element_by_xpath('//*[@id="username"]').send_keys('mcmtestowner@gmail.com')
    driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div/div/div[2]/div[4]/button').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('Megazone1!')
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='로그인'])[1]/following::strong[1]").click()
    time.sleep(5)
    # Project로 이동
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Administration'])[1]/following::div[4]").click()
    time.sleep(5)

# Project Admin > Settings > Transcoding > Create origin asset : Enable 설정
def test_settings_transcoding_origin_enable(self):
    print("Calling up a settings_transcoding_origin_enable Module")  # 해당 모듈 호출되었음을 안내
    driver = self.driver
    move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
    # [Admin]버튼 클릭
    driver.find_element_by_xpath("//div[@id='root']/div/nav/div[2]/div/ul/li[4]/div/div/button/i").click()
    # Admin 메뉴에서 [Project manager] 메뉴 선택
    driver.find_element_by_link_text("Project manager").click()
    time.sleep(3)
    # [Transcoding]탭 클릭
    driver.find_element_by_link_text("Transcoding").click()
    # [Create origin asset] : [Enable] 선택
    # driver.find_element_by_xpath("//input[@type='radio']").click()
    driver.find_element_by_xpath("(//input[@type='radio'])[2]").click()
    # [Save]버튼 클릭
    driver.find_element_by_xpath(
        "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
    time.sleep(3)

# Project Admin > Settings > Transcoding > Create origin asset : Disable 설정
def test_settings_transcoding_origin_disable(self):
    print("Calling up a settings_transcoding_origin_disable Module")  # 해당 모듈 호출되었음을 안내
    driver = self.driver
    move_main(self)  # Project Main page로 이동하는 공통 모듈 호출
    # [Admin]버튼 클릭
    driver.find_element_by_xpath("//div[@id='root']/div/nav/div[2]/div/ul/li[4]/div/div/button/i").click()
    # Admin 메뉴에서 [Project manager] 메뉴 선택
    driver.find_element_by_link_text("Project manager").click()
    time.sleep(3)
    # [Transcoding]탭 클릭
    driver.find_element_by_link_text("Transcoding").click()
    # [Create origin asset] : [Disable] 선택
    driver.find_element_by_xpath("(//input[@type='radio'])[2]").click()
    # [Save]버튼 클릭
    driver.find_element_by_xpath(
        "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
    time.sleep(3)