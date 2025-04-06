# 데이터 수집

## 1) API (Application Programming Interface)

**정의** : 소프트웨어 애플리케이션 간에 데이터와 기능을 교환할 수 있도록 하는 일련의 규칙과 프로토콜

- **HTTP** : 웹 브라우저 → 웹 서버에 웹 페이지 요청
- **HTML** (HyperText Markup Language) : 웹 서버 → 웹 브라우저에 웹 페이지 전송

### 종류
- **CSV**, **JSON**, **XML**

#### JSON
- Python의 dictionary와 비슷한 구조: `{key: value}`
- 데이터를 주고받을 때는 텍스트 형태로 전달함
- 사용 방법:
  ```python
  import json

  # 데이터 전송 (웹 브라우저)
  json.dumps(data, ensure_ascii=False)

  # 데이터 수신 (웹 서버)
  json.loads(json_string)

  # pandas를 이용해 JSON 읽기
  import pandas as pd
  pd.read_json('파일경로')  # key는 열(column)로, value는 행(row)으로 변환
  ```

#### XML
- 시작 태그 <태그> : 루트(부모)
- 자식 태그 <태그> : 자식
- Element 구조: <태그>내용</태그>
- 종료 태그 </태그>
  ```python
  # 자식 엘리먼트의 값을 출력하는 방법
  from xml.etree.ElementTree import Element
  element.findtext('자식태그')
  ```
