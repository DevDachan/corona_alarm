

# Service 소개
 - 간단합니다. 라즈베리파이에서 현재 실시간 코로나 정보와 네이버 미세먼지 정보를 불러와 내가 선택한 지역의 상황을 TTS를 통해
  출력해주고 이것을 안드로이드로 제어가 가능하게 만들었습니다. 또한 사용자가 해당 어플에서 알람을 설정했을때 핸드폰 알람이 울림과 동시에 당일 코로나 상황을 알려줍니다.

 - 제가 사용하는 라즈베리파이는 raspberrypi.local에 접속이 안되기 때문에 모든 파일은 웹 주소가 Local IP주소로 되어 있습니다
 따라서 다른 사용자가 사용하기 위한 raspberrypi.local로 만들어진 apk를 첨부하고 appinventor 소스도 첨부합니다.

# 사용법
 - 1. 아래 기능들을 설치해줍니다.
 - 2. 라즈베리파이에서 Final_21700351.py를 다운받아 실행시켜 줍니다.
 - 3. 안드로이드에서 어플을 설치해 실행시켜주면 됩니다.
 
 ※ 해당 py 코드 내에서 음성이 출력되기 위해서는 라즈베리파이에 소리를 출력해줄 장치를 미리 연결시켜야 합니다
 
# 사용한 기능 설치

**mplayer**

> sudo apt-get install mplayer

**python**

> sudo apt-get install python3
 - 기본적으로도 설치 되어있지만 python3를 사용하기 위해 다운받았습니다

**blutueth**

 - 블루투스를 터미널에서 하는 방법이 있지만 좀더 편리하게 안드로이드 VNC를 사용하여 연결했습니다

방법은 아래 링크를 확인하세요
- https://m.blog.naver.com/PostView.nhn?blogId=cosmosjs&logNo=221008665859&proxyReferer=https:%2F%2Fwww.google.com%2F

**beautifulsoup** 

> sudo apt-get install python-bs4



# 각 지역 코드
 - HTML 정보를 불러오며 해당 사이트가 저장한 class 번호를 그대로 따와 사용했습니다.

**코로나**
서울 1 
부산 2 
대구 3 
인천 4 
광주 5 
대전 6 
울산 7 
세종 8 
경기 9 
강원 10 
충북 11  
충남 12 
전북 13 
전남 14 
경북 15 
경남 16 
제주 17 
검역 18 

> http://ncov.mohw.go.kr/

**미세먼지**
서울 09
부산 08
대구 06
인천 11
광주 05
대전 07
울산 10
세종 17
경기 02
강원 01
충북 16
충남 15
전북 13
전남 12
경북 04
경남 03
제주 14

> https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%A0%84%EA%B5%AD%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80
> https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%A0%84%EA%B5%AD%EC%B4%88%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80


# 해당 서비스 개선할 점
 - 먼저 어플상에서는 핸드폰에서 어플을 종료후 알람이 울리는 것은 구현하지 못함
 - 라즈베리 파이에서 tts를 출력하며 음성이 매끄럽지 않음

