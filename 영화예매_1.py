import requests
from bs4 import BeautifulSoup

#개발자 도구 보면 그 홈페이지에 아예 다른 홈페이지를 이미지스럽게 덮어씌워둔 형태가 있거든.
#그게 iframe id에 있는건데 여기서 src에 있는거 가져와서 cgv 도메인 뒤에 넣으면 그 상영시간표만 웹에 띄울 수 있다 이거여



url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0059&date=20200405'
html = requests.get(url)

#body > div > div.sect-showtimes > ul > li:nth-child(1) > div > div.info-movie > a > strong

soup = BeautifulSoup(html.text,'html.parser')

#text = soup.select_one('body > div > div.sect-showtimes > ul > li:nth-child(1) > div > div.info-movie > a > strong')

title_list=soup.select('div.info-movie')

#strip()으로 앞뒤의 공백을 없앨 수 있다
for i in title_list:
    print(i.select_one('a > strong').text.strip())