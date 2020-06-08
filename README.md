

# Service 소개
 - 간단하다. 현재 코로나 홈페이지와 네이버 미세먼지 정보를 불러와 내가 선택한 지역의 상황을  TTS를 통해
  출력해주는 것.
 



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



