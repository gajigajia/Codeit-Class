from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")


driver.get("https://finance.naver.com/")
driver.find_element_by_class_name("h_opn").click()


#브라우저 종료 코드
driver.close()
