from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")


driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
driver.find_element_by_id("id").send_keys("saturnjoa")
driver.find_element_by_id("pw").send_keys("mala1004*")
driver.find_element_by_id("log.login").click()
