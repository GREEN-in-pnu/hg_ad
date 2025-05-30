# 2주차 학습내용

## Chapter 3. 데이터 정제하기

### 3-1. 불필요한 데이터 삭제하기

---

## 📘 용어 정리

* **데이터 정제(Data Cleaning)**: 손상되거나 불필요한 데이터를 정리하여 분석이나 모델링에 적합한 상태로 만드는 과정
* **데이터 랭글링(Data Wrangling) / 먼징(Munging)**: 데이터를 구조화하고 정형화하여 활용 가능한 형태로 가공하는 일련의 작업
* **사용 도구**: `pandas` 라이브러리를 중심으로 정제 작업 수행

---

## 🔻 열 삭제하기

### 목적

분석에 필요 없는 열을 제거하여 데이터의 크기를 줄이고, 시각적/계산적 복잡성을 낮춤

### 주요 사용 함수 및 개념

* **슬라이싱**: 원하는 열 범위만 선택 가능 (단, 중간 열 제외 어려움)
* **불리언 배열**: 특정 열을 조건으로 걸러내기 좋음 (`columns != '열이름'`)
* **`drop()` 메서드**: 특정 열 이름을 명시적으로 제거 가능 (`axis=1`은 열 삭제)
* **`dropna()` 메서드**: 결측치(NaN)가 있는 열 자동 삭제 가능

### 예시 상황

* 자동 생성된 `Unnamed: 13` 열은 의미 없는 공백 열로 삭제 필요
* 분석에 필요 없는 열인 `부가기호`, `주제분류번호` 제거
* 모든 값이 비어 있는 열은 `dropna(how='all')`로 일괄 삭제

---

## 🔻 행 삭제하기

### 목적

불필요한 행(예: 테스트용 데이터, 조건에 부합하지 않는 데이터)을 제거하여 분석 정확도 향상

### 주요 사용 방법

* **`drop()` 메서드 (axis=0)**: 특정 인덱스 지정하여 삭제
* **슬라이싱**: 특정 범위의 행을 제외하거나 선택 가능
* **불리언 배열**: 조건에 맞는 행만 필터링 가능 (예: 대출건수 > 1000)

### 예시 상황

* 상위 2개 행 제거
* 특정 출판사의 도서만 필터링
* 대출건수가 일정 기준 이상인 도서만 추출

---

## 🔁 중복된 행 찾기

### 목적

같은 도서가 중복 기록되어 있는 경우, 정확한 통계를 위해 중복 제거 필요

### 주요 사용 함수

* **`duplicated()` 메서드**: 전체 또는 일부 열을 기준으로 중복 여부 확인
* **`subset` 매개변수**: 중복 확인에 사용할 열 지정 가능
* **`keep=False`**: 모든 중복 행을 True로 표시 (기본은 첫 번째만 False)

### 예시 상황

* 도서명, 저자, ISBN, 권을 기준으로 중복된 행 파악
* 중복된 모든 도서 정보를 따로 확인해보기 위한 필터링

---

## 📊 그룹별로 모으기

### 목적

중복 도서를 하나로 모으고, 그들의 대출 건수를 합산하여 실질적인 통계로 변환

### 주요 사용 함수

* **`groupby()`**: 지정한 열 기준으로 그룹을 나누어 연산 적용
* **`sum()`**: 그룹별 합계를 계산
* **`dropna=False`**: 결측값도 하나의 그룹으로 처리

### 예시 상황

* 같은 책이 여러 행으로 나뉜 경우, 대출 건수를 합쳐서 한 행으로 만들기 위함
* 도서명, 저자, ISBN, 권 기준으로 그룹핑 수행

---

## 🧬 원본 데이터 업데이트 하기

### 목적

`groupby`로 계산한 대출 건수 정보를 원래의 고유 도서 데이터프레임에 반영

### 과정 요약

1. **중복 행 제거**: 고유 도서 정보만 남기기 위한 불리언 필터링
2. **인덱스 재설정**: `groupby`의 인덱스 기준과 동일하게 맞추기
3. **`update()`**: 계산된 대출건수를 고유 도서 정보에 덮어쓰기
4. **`reset_index()`**: 다시 열 형태로 변환하여 기존 구조 복원
5. **열 순서 복원**: 원래 데이터프레임과 동일한 순서로 재정렬

### 주요 함수

* `duplicated()` + `~`: 중복 아닌 행 필터링
* `set_index()` / `reset_index()`
* `update()`
* 열 순서 재정렬: `df[원래.columns]`

---

## 💾 불필요한 데이터 제거 결과 저장

* 정제된 데이터프레임(`ns_book4`)을 CSV 파일로 저장
* 이후 분석이나 시각화 단계에서 바로 사용할 수 있도록 가공 완료

---

## ⚙️ 일괄처리함수: `data_cleaning()`

### 목적

동일한 정제 작업을 새로운 데이터셋에 반복 적용할 수 있도록 함수화

### 특징

* 파일명을 매개변수로 받아 자동으로 정제된 데이터프레임 반환
* 중복 제거, 그룹별 합산, 열 순서 재정렬까지 포함된 일괄 처리

### 사용 예시

* `data_cleaning('ns_202104.csv')` → 정제 완료된 `DataFrame` 반환
* 이후 `.equals()`로 기존 결과와 비교해 검증 가능
