from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")

'''
1. 접속하기
2. 글 누르기
3. 댓글/이름/비밀번호 입력
4. 비밀글 체크하기
'''


driver.get("https://philosopher-chan.tistory.com/")

#selector로도 찾을 수 있어요
driver.find_element_by_css_selector("#main > div > div:nth-child(1) > ul > li > div").click()

#반복하려면 이 아래 애들을 반복하면 되겠죠? 단 중간중간에 refresh()가 들어가야 해요
'''driver.find_element_by_id("comment").send_keys("아오왜 안됀ㄹ댜ㅓㄹ;ㅈㄷ머ㅑㅐㅊ")
driver.find_element_by_name("name").send_keys("아오ㅈㄷㄹㅈㄷㄹ")
driver.find_element_by_name("password").send_keys("1004")
driver.find_element_by_name("secret").click()
driver.find_element_by_class_name("btn_register").click()


driver.refresh()
#너무 바로 달리면 로봇같잖슴?
#아래와 같이 하면 3초 간격을 줍니다
time.sleep(3)

driver.find_element_by_id("comment").send_keys("아오왜 안됀ㄹ댜ㅓㄹ;ㅈㄷ머ㅑㅐㅊ")
driver.find_element_by_name("name").send_keys("아오ㅈㄷㄹㅈㄷㄹ")
driver.find_element_by_name("password").send_keys("1004")
driver.find_element_by_name("secret").click()
driver.find_element_by_class_name("btn_register").click()'''


#반복문 만들기, count가 5되기 전까지만 돌아가용
count = 0
while count < 5 :
    driver.find_element_by_id("comment").send_keys("아오왜 안됀ㄹ댜ㅓㄹ;ㅈㄷ머ㅑㅐㅊ")
    driver.find_element_by_name("name").send_keys("아오ㅈㄷㄹㅈㄷㄹ")
    driver.find_element_by_name("password").send_keys("1004")
    driver.find_element_by_name("secret").click()
    driver.find_element_by_class_name("btn_register").click()
    driver.refresh()
    time.sleep(3)
    count=count+1
