import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0059&date=20200405'
html = requests.get(url)

soup = BeautifulSoup(html.text,'html.parser')

gold= soup.select_one('span.gold')


#골드가 있따면...을 이렇게도 걍 써도 되는구나
if(gold):
    #span gold의 부모div를 찾아서~거기서 다시 내려와야함
    gold=gold.find_parent('div',class_='col-times')

    title=gold.select('div.info-movie>a>strong')
    print(title)



    #print('GOLD CLASS 상영이 있습니다')
else:
    print('GOLD CLASS 상영이 없습니다')



