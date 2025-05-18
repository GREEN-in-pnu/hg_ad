# eda_summary_code.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 샘플 데이터 생성
data = {
    'age': [25, 32, 47, 51, 62, 22, 33, 45, 52, 46],
    'income': [2500, 3200, 4700, 5100, 6200, 2200, 3300, 4500, 5200, 4600]
}
df = pd.DataFrame(data)

# 1. 기술통계 요약
print("\n[기술통계] df.describe()")
print(df.describe())

# 평균
print("\n[평균] Series.mean(), np.mean()")
print(df['age'].mean())           # Pandas
print(np.mean(df['age']))         # NumPy

# 중앙값
print("\n[중앙값] Series.median(), np.median()")
print(df['age'].median())         # Pandas
print(np.median(df['age']))      # NumPy

# 최솟값, 최댓값
print("\n[최솟값, 최댓값]")
print(df['age'].min(), df['age'].max())

# 분위수
print("\n[분위수] 0.25, 0.5, 0.75")
print(df['age'].quantile(0.25))
print(np.quantile(df['age'], 0.5))  # 중앙값과 동일

# 분산, 표준편차
print("\n[분산, 표준편차]")
print(df['age'].var(), df['age'].std())        # Pandas
print(np.var(df['age']), np.std(df['age']))    # NumPy

# 최빈값
print("\n[최빈값] Series.mode()")
print(df['age'].mode())

# 2. 시각화 ----------------------------------

# 2-1. 산점도 scatter()
plt.figure(figsize=(5, 4))
plt.scatter(df['age'], df['income'], 
            color='green',      # 점 색상
            marker='o',         # 점 모양
            s=50,               # 점 크기
            alpha=0.7)          # 투명도
plt.title('Age vs Income Scatter Plot')
plt.xlabel('Age')
plt.ylabel('Income')
plt.grid(True)
plt.show()

# 2-2. 히스토그램 hist()
plt.figure(figsize=(5, 4))
plt.hist(df['age'], 
         bins=5,             # 구간 수
         color='skyblue',    # 색상
         edgecolor='black')  # 테두리 색
plt.title('Age Histogram')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# 2-3. 박스플롯 boxplot()
plt.figure(figsize=(5, 4))
plt.boxplot(df['income'], 
            patch_artist=True,   # 박스 채우기
            boxprops=dict(facecolor='lightgreen'))
plt.title('Income Boxplot')
plt.ylabel('Income')
plt.show()

# 2-4. 막대그래프 bar()
categories = ['A', 'B', 'C']
values = [10, 15, 7]
plt.figure(figsize=(5, 4))
plt.bar(categories, values, 
        color='coral',        # 막대 색상
        edgecolor='black')   # 테두리
plt.title('Category Bar Plot')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()

# 2-5. 꺾은선그래프 plot()
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 6, 4]
plt.figure(figsize=(5, 4))
plt.plot(x, y, 
         marker='o',          # 각 점 표시
         linestyle='-',       # 선 스타일
         color='purple')      # 선 색상
plt.title('Line Plot Example')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

# 2-6. pandas plot()
df.plot(kind='hist', y='age', bins=5, color='orange', edgecolor='black', title='Pandas Histogram')
plt.show()

df.plot.box(y='income', title='Pandas Boxplot')
plt.show()
