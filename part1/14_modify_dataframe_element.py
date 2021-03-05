import pandas as pd

exam_data = {'이름': ["민서", "소율", "태욱"],
             '수학': [100, 80, 70],
             '영어': [100, 89, 95],
             '음악': [100, 95, 100],
             '체육': [100, 90, 80]
             }
df = pd.DataFrame(exam_data)

df.set_index("이름", inplace=True)
print(df)
print()

# 데이터프레임 df의 특정 원소를 변경하는 방법: 민서의 체육 점수
df.iloc[0] [3] = 80
print(df)
print()

df.loc['민서']['체육'] = 90
print(df)
print()

df.loc['민서', '체육'] = 100
print(df)