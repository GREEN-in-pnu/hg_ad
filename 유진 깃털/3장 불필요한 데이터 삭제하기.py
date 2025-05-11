#!/usr/bin/env python
# coding: utf-8

# # 열 삭제하기

# In[2]:


get_ipython().system('pip install gdown')

import gdown
gdown.download('https://bit.ly/3RhoNho','ns_202104.csv',quiet=False)


# In[4]:


import pandas as pd
ns_df = pd.read_csv('ns_202104.csv', low_memory=False)
ns_df.head()  #처음 다섯개 행 출력


# ### loc 매서드에 슬라이싱 사용

# In[5]:


ns_book = ns_df.loc[:,'번호':'등록일자'] # 번호열부터 등록일자열까지 전체행 선택
ns_book.head() # ns_df의 데이터프레임에서 열을 삭제한 결과를 ns_book이라는 변수에 저장
#이렇게 하니 쓸모 없었던 열인 Unnamed: 13이 사라짐


# ### loc매서드와 불리언 배열

# In[7]:


# 컬럼 속성 확인
print(ns_df.columns)


# In[8]:


print(ns_df.columns[0])


# In[9]:


ns_df.columns != 'Unnamed: 13' #원소별 비교, 넘파이 배열 반환 


# In[11]:


selected_columns = ns_df.columns != 'Unnamed: 13'
ns_book = ns_df.loc[:, selected_columns] #true인 열의 모든 행을 선택
ns_book.head() 


# In[16]:


#부가기호 열을 제외

selected_columns = ns_df.columns != '부가기호'
ns_book = ns_df.loc[:,selected_columns]
ns_book.head()


# ### drop() 매서드

# drop()매서드로 열을 삭제하려면 첫번째 매개변수에 삭제하려는 열 이름을 전달하고 axis 매개변수를 1로 저장  
# aixs매개변수에는 삭제할 축을 지정할 수 있음.  
# axis 매개변수의 기본값인 0은 행을 삭제하고 1은 열을 삭제함.

# In[17]:


# 'Unnamed: 13'열 삭제
ns_book = ns_df.drop('Unnamed: 13', axis=1) #삭제하려는 열 이름, axis 매개변수에 1을 지정하면 열을 삭제
ns_book.head()


# In[22]:


# 부가기호 열과 unnamed:13열 삭제
# 여러개의 열을 삭제하려면 리스트 형식을 사용
ns_book = ns_df.drop(['부가기호','Unnamed: 13'], axis=1)
ns_book.head()


# #### inplace 매개변수
# inplace 매개변수를 True로 지정하면 현재선택한 데이터 프레임을 바로 수정할 수 있음.

# In[23]:


# 주제분류번호 열 삭제
ns_book.drop('주제분류번호', axis=1, inplace=True) #선택한 데이터프레임에 덮어씀
ns_book.head()


# ### dropna() 매서드  
# NaN이 하나 이상 포함된 행이나 열을 삭제

# In[24]:


ns_book = ns_df.dropna(axis=1)
ns_book.head() #삭제된 열에는 NaN이 적어도 한개 이상 있었을 것


# #### how 매개변수
# 모든 값이 NaN인 열을 삭제 -> dropna() 매서드에 how매개변수를 'all'로 지정

# In[26]:


ns_book = ns_df.dropna(axis=1, how='all')
ns_book.head()


# # 행 삭제하기

# In[27]:


ns_book2 = ns_book.drop([0,1]) # 인덱스 0부터 1까지 2개행을 선택
ns_book2.head()


# ## []연산자와 슬라이싱
# []연산자에  
# 열이름 , 열 이름 리스트 -> 열선택  
# 슬라이싱, 불리언 배열 -> 행선택

# In[28]:


ns_book2 = ns_book[2:]
ns_book2.head()


# In[29]:


ns_book2 = ns_book[0:2] # 2는 포함되지 않음. 0,1만 포함 (loc매서드에서 슬라이싱은 마지막 인덱스 포함)
ns_book2.head()


# ## []연산자와 불리언 배열
# 원하는 행은 T로, 제외할 행은 F로 표시한 불리언 배열로 행을 선택

# In[30]:


selected_rows = ns_df['출판사'] == '한빛미디어'
ns_book2 = ns_book[selected_rows]
ns_book2.head()


# In[31]:


ns_book2 = ns_book[ns_book['대출건수']> 1000] #대출건수 1000권 이하인 행들 삭제, selected_row 변수 만들지 않고 조건을 직접 []연산자에 넣음
ns_book2.head()


# ## 중복된 행 찾기

# #### duplicated() 매서드 사용
# 중복된 행 중 처음 행을 제외한 나머지 행은 T로 이외에는 F로 해서 불리언 배열 반환  
# sum() 함수는 T를 1로 인식해서 중복된 행의 개수를 셀 수 있음

# In[33]:


sum(ns_book.duplicated()) # 중복된 행이 하나도 없음


# #### subset 매개변수
# 일부 열을 기준으로 중복된 행 찾기  
# 매개변수에 기준 열 나열

# In[36]:


sum(ns_book.duplicated(subset=['도서명','저자','ISBN']))


# #### keep 매개변수
# duplicated 메서드에 keep 매개변수를 F로 지정해 중복된 모든 행을 T로 표시  

# In[39]:


dup_rows = ns_book.duplicated(subset=['도서명','저자','ISBN'], keep=False) #중복된 행을 모두 T로 반환한 불리언 배열을 반환
ns_book3 = ns_book[dup_rows]
ns_book3.head()


# ## 그룹별로 모으기
# groupby()매서드 사용  
# by 매개변수에는 행을 합칠 때 기준이 되는 열을 지정  
# by 매개변수에 지정된 열에 NaN이 포함되어 있으면 해당 행을 삭제하기에 불필요한 행의 삭제를 막기위해 dropna 매개변수를 F로 지정  
# -> 연산할때 NaN이 있는 행도 포함  

# In[42]:


count_df = ns_book[['도서명','저자','ISBN','권','대출건수']] #그룹으로 묶을 기준 열


# In[43]:


group_df = count_df.groupby(by=['도서명','저자','ISBN','권'], dropna=False) # dropna=False는 NaN이 있는 행을 삭제하지 않는다는 뜻
loan_count = group_df.sum()


# In[44]:


loan_count = count_df.groupby(by=['도서명','저자','ISBN','권'], dropna = False).sum()
loan_count.head()


# In[ ]:




