import pandas as pd

exam_data = {'이름': ["민서", "소율", "태욱"],
             '수학': [100, 80, 70],
             '영어': [100, 89, 95],
             '음악': [100, 95, 100],
             '체육': [100, 90, 80]
             }
df = pd.DataFrame(exam_data)

# '이름' 열을 새로운 인덱스로 지정하고 df 겍체에 변경 사항 반영
df.set_index('이름', inplace=True)
print(df)

# 데이터 프레임 df의 특정 원소 1개 선택('민서'의 '음악'점수)
a = df.loc['소율', '음악']
print(a)

b = df.iloc[1, 2]
print(b)

# 데이터 프레임 df의 특정 원소 2개 선택('태욱'의 '음악', '체육'점수)
c = df.loc['태욱', ['음악', '체육']]
print(c)

d = df.iloc[2, [2, 3]]
print(d)

e = df.loc['태욱', '음악':'체육']
print(e)

f = df.iloc[0, 2:]
print(f)

# df 2개 이상의 행과 열에 속하는 원소를 선택('민서', '소율'의 '음악', '영어'점수)
g = df.loc[["민서", "소율"], ["음악", "체육"]]
print(g)

h = df.iloc[[0, 1], [2, 3]]
print(h)

i = df.loc["민서":"소율", "음악":"체육"]
print(i)

j = df.iloc[0:2, 2:]
print(j)