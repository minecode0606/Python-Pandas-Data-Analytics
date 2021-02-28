import pandas as pd

exam_data = {'수학' : [ 100, 80, 70], '영어' : [ 100, 89, 95],
             '음악' : [ 100, 95, 100], '체욱' : [ 100, 90, 80]}

df = pd.DataFrame(exam_data, index=['민서', '소율', '태욱'])
print(df)
print()

# 행 인덱스를 1개 실행
lable1 =  df.loc['민서']
position1 = df.iloc[0]

print(lable1)
print()
print(position1)

# 행 인덱스를 사용하여 2개 이상의 행 선택
lable2 = df.loc[['민서', '소율']]
position2 = df.iloc[0, 1]

print(lable2)
print()
print(position2)

# 행 인덱스의 범위를 지정하여 행 선택
lable3 = df.loc['민서' : '소율']
position3 = df.iloc[0:1]
print(lable3)
print()
print(position3)
