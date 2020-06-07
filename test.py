import os,sys

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://ncov.mohw.go.kr/")
soup = BeautifulSoup(html.read(), 'html.parser')
html.close()

##input a
a = '1'

coro_name = soup.find("button",{"type":"button","data-city":"map_city"+a}).select(".name")
coro_num =  soup.find("button",{"type":"button","data-city":"map_city"+a}).select(".num")
coro_before =  soup.find("button",{"type":"button","data-city":"map_city"+a}).select(".before")




temp = []
for a in coro_name:
        temp += a.get_text()
coro_name = ''.join(temp)

temp = []
for a in coro_num:
        temp += a.get_text()
coro_num = ''.join(temp)

temp = []
for a in coro_before:
        temp += a.get_text()
coro_before = ''.join(temp)


print("현재",coro_name,"의 코로나 확진자 수는",coro_num,"명이고 어제보다",coro_before,"변화됐습니다.")

ak = "현재 " + coro_name + "지역의  코로나  확진자  수 는" + coro_num + "명 이고 어제 보다" + coro_before + "명 증가 됐습니다"

text = "http://translate.google.com/translate_tts?ie=UTF-8&total=1&idx=0&textlen=32&client=tw-ob&q="+ak+"&tl=ko-kr"

print(text)
os.system('wget -q -U Mozilla -O mp3_file.mp3 "%s"' %text)
os.system('mplayer mp3_file.mp3')

