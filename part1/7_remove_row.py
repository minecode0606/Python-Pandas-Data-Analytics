import pandas as pd

exam_data = {'수학' : [ 100, 80, 70], '영어' : [ 100, 89, 95],
             '음악' : [ 100, 95, 100], '체욱' : [ 100, 90, 80]}

df = pd.DataFrame(exam_data, index=['민서', '소율', '경자'])
print(df)
print('\n')

# 데이터 프레임 df를 복제하여 변수 df2에 저장, df의 1개 행(row)를 삭제
df2 = df[:]
df2.drop('민서', inplace=True)
print(df2)
print('\n')

# 데이터 프레임 df를 복제하여 변수 df3에 저장, df의 2개 행(row)를 삭제
df3 = df[:]
df3.drop(["민서", "소율"], axis=0, inplace=True)
print(df3)