def start(data_s):
	import os,sys
	from urllib.request import urlopen
	from bs4 import BeautifulSoup

	if data_s == '1':
		b = '09'
	elif data_s == '2':
		b = '08'
	elif data_s == '3':
		b = '06'
	elif data_s == '4':
		b = '11'
	elif data_s == '5':
		b = '05'
	elif data_s == '6':
		b = '07'
	elif data_s == '7':
		b = '10'
	elif data_s == '8':
		b = '17'
	elif data_s == '9':
		b = '02'
	elif data_s == '10':
		b = '01'
	elif data_s == '11':
		b = '16'
	elif data_s == '12':
		b = '15'
	elif data_s == '13':
		b = '13'
	elif data_s == '14':
		b = '12'
	elif data_s == '15':
		b = '04'
	elif data_s == '16':
		b = '03'
	elif data_s == '17':
		b = '14'

	a = data_s
## 코로나 확진자 ----------------------------------------------------------------
	html = urlopen("http://ncov.mohw.go.kr/")
	soup = BeautifulSoup(html.read(), 'html.parser')
	html.close()

	coro_name = soup.find("button",{"type":"button","data-city":"map_city"+a}).select(".name")
	coro_num =  soup.find("button",{"type":"button","data-city":"map_city"+a}).select(".num")
	coro_before =  soup.find("button",{"type":"button","data-city":"map_city"+a}).select(".before")

	temp1 = []
	for a in coro_name:
	        temp1 += a.get_text()
	coro_name = ''.join(temp1)

	temp2 = []
	for a in coro_num:
	        temp2 += a.get_text()
	coro_num = ''.join(temp2)

	temp3 = []
	for a in coro_before:
	        temp3 += a.get_text()
	coro_before = ''.join(temp3)

##미세먼지--------------------------------------------------------------------------------------

	html = urlopen("https://search.naver.com/search.naver?where=nexearch&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&ie=utf8&sm=tab_she&qdt=0")
	dust_html = BeautifulSoup(html.read(), 'html.parser')
	html.close()

	dust_num = dust_html.find("div", {"class":"map_area"}).find("a", {"class":"ct"+b+" lv2 _local"}).em.string
	dust = int(dust_num)

## 초미세먼지-------------------------------------------------------------------------------------

	html = urlopen("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%A0%84%EA%B5%AD%EC%B4%88%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80")
	ufdust = BeautifulSoup(html.read(), 'html.parser')
	html.close()

	ufdust_num = ufdust.find("div", {"class":"map_area"}).find("a", {"class":"ct"+b+" lv2 _local"}).em.string
	ufdust = int(ufdust_num)

## 출력문-----------------------------------------------------------------------------------------
	print("현재 서울의 미세먼지 농도는",dust, "이고 초미세먼지 농도는 ",ufdust,"입니다")
	if dust>0:
		dust_state = "좋음"
	elif dust>30:
		dust_state = "보통"
	elif dust>80:
		dust_state = "나쁨"
	elif dust>150:
		dust_state = "매우 나쁨"


	if ufdust>0:
		ufdust_state = "좋음"
	elif ufdust>15:
		ufdust_state = "보통"
	elif ufdust>35:
		ufdust_state = "나쁨"
	elif ufdust>75:
		ufdust_state = "매우 나쁨"


	ak = "오늘 코로나 상황을 알려 드리겠습니다.  " + coro_name + "지역의  코로나  확진자  수 는 " + coro_num + "명 이고 어제 보다" + coro_before + "명 증가 됐습니다"
	bk = " ()() "+coro_name + "지역 미세먼지 농도 수치는 " + str(dust) + "이므로 " +dust_state + " 상태 이고 초미세먼지 농도 수치는  "+ str(ufdust) +" 이므로 "+ufdust_state+" 상태 입니다." 
	fi = " 오늘 하루도 행복한 하루 되세요"
	text = "http://translate.google.com/translate_tts?ie=UTF-8&total=1&idx=0&textlen=32&client=tw-ob&q="+ak+bk+fi+"&tl=ko-kr"
	os.system('wget -q -U Mozilla -O mp3_file.mp3 "%s"' %text)
	os.system('mplayer mp3_file.mp3')

	return 0;

import socket

me = socket.socket()
me.bind(('192.168.43.152',7895))

me.listen(5)

while True:
        conn, addr = me.accept()
        data = conn. recv(1024).decode()
        if not data :
                break
        n = data.index('\r\n\r\n')+4
        data = data[n:len(data)]
        print(data)
        func = data
        if func > '0':
                data = start(data)
                func = 0
        sdata = 'HTTP/1.1 200 OK \r\n\r\n '+str(data)
        conn.send(sdata.encode())
        conn.close()
        if data == '99' or data == 99:
                break

