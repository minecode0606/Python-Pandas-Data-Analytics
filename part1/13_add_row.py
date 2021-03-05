import pandas as pd

exam_data = {'이름': ["민서", "소율", "태욱"],
             '수학': [100, 80, 70],
             '영어': [100, 89, 95],
             '음악': [100, 95, 100],
             '체육': [100, 90, 80]
             }
df = pd.DataFrame(exam_data)
print(df)
print()

# 새로운 행 추가 - 같은 원소 값 입력
df.loc[3] = 0
print(df)
print()

# 새로운 행 추가 - 원소 값 여러개의 배열 입력
df.loc[4] = ['경자', 90, 80, 70, 60]
print(df)
print()

# 새로운 행 추가 - 기존 행 복사
df.loc['행5'] = df.loc[3]
print(df)
