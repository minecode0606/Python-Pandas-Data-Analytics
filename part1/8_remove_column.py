import pandas as pd

# DataFrame() 함수로 데이터프레임 변환, 변수 df에 저장
exam_data = {'수학' : [ 100, 80, 70], '영어' : [ 100, 89, 95],
             '음악' : [ 100, 95, 100], '체욱' : [ 100, 90, 80]}

df = pd.DataFrame(exam_data, index=['민서', '소율', '태욱'])
print(df)
print()

# 데이터 프레임 df를 복제하여 변수 df4에 저장, df4의 1개열 삭제
df4 = df[:]
df4.drop('수학', axis=1, inplace=True)
print(df4)
print()

# 데이터 프레임 df를 복제하여 변수 df5에 저장, df5의 2개열 삭제
df5 = df[:]
df5.drop(['영어', '음악'], axis=1, inplace=True)
print(df5)