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

# 데이터 프레임 df에 국어 점수 열(column) 추가, 데이터 값은 80지정
df['국어'] = 80
print(df)