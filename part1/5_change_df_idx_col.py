import pandas as pd

# 행 인덱스/열 이름 지정하여 데이터프레임 만들기
df = pd.DataFrame([[15, '남', '현암중'], [12, '여', '현암초']],
                  index=['민서', '소율'],
                  columns=['나이', '성별', '학교'])
# 행 인덱스 열 이름 확인하기
print(df) # 데이터 프레임
print()
print(df.index) # 행 인덱스
print()
print(df.columns) # 열 이름

# 행, 인덱스, 열 이름 변경하기
df.index=['학생1', '학생2']
df.columns=['연령', '남녀', '소속']

print(df)
print()
print(df.index) # 행 인덱스
print()
print(df.columns) # 열 이름
