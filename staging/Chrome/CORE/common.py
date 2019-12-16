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