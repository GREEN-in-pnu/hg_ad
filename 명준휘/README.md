A. 데이터 수집
1) API (Application Programming Interface)
 정의 : 소프트웨어 애플리케이션 간에 데이터와 기능을 교환할 수 있도록 하는 일련의 규칙과 프로토콜
- HTTP : 웹 브라우저 -웹 페이지 요청-> 웹 서버
- HTML(markable language?) : 웹 서버 -웹 페이지 전송-> 웹 브라우저
 종류) CSV, JSON, XML
      JSON : python의 dictionary와 비슷 {key:value}
             데이터 받을 땐 텍스트로 받아야하므로 사용함
             import json
             json.dumps( ,ensure_ascii=False) #데이터 전송하는 애(웹 브라우저)
             json.loads() #데이터 받는 애(웹 서버)
  
             import pandas as pd
             pd.read_json() key는 열으로, value는 행으로
      XML : 시작태그 < > => 루
