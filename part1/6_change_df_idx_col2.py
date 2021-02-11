import pandas as pd

# 행 인덱스/열 이름 지정하여 데이터프레임 만들기
from pandas import DataFrame

df = pd.DataFrame([[15, '남', '현암중'], [12, '여', '현암초']],
                  index=['민서', '소율'],
                  columns=['나이', '성별', '학교'])

# dataframe 출력
print(df)
print()

# 열 이름중 나이를 연령으로, 성별을 남녀로 학교를 소속으로 바꾸기
df.rename(columns={'나이': '연령', '성별': '남녀', '학교': '소속'}, inplace=True)

# df의 행 인덱스 안에서, '민서'를 '학생1'로, '소율'을 '학생2'로 바꾸기
df.rename(index={'민서':'학생1', '소율': '학생2'}, inplace=True)

print(df)
