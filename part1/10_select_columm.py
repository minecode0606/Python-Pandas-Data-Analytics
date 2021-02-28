import pandas as pd

exam_data = {'이름': ["민서", "소율", "태욱"],
             '수학': [100, 80, 70],
             '영어': [100, 89, 95],
             '음악': [100, 95, 100],
             '체육': [100, 90, 80]
             }
df = pd.DataFrame(exam_data)
print(df)
print(type(df))
print()

# 수학 점수 데이터만 선택, 변수 math1에 저장
math1 = df["수학"]
print(math1)
print(type(math1))
print()

# 영어 점수 데이터만 선택, 변수 english에 저장
english = df.영어
print(english)
print()
print(type(english))

# "음악", "체육" 점수 데이터를 선택, 변수 music_gym에 저장
math2 = df[["수학"]]
print(math2)
print(type(math2))

