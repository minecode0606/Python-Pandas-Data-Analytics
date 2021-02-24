import pandas as pd

exam_data = {'수학' : [ 100, 80, 70], '영어' : [ 100, 89, 95],
             '음악' : [ 100, 95, 100], '체욱' : [ 100, 90, 80]}

df = pd.DataFrame(exam_data, index=['민서', '소율', '경자'])
print(df)
print('\n')

#