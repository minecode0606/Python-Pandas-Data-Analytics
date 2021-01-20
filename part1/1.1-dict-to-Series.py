# -*- coding: UTF-8 -*-

# pandas import
import pandas as pd

# key:value 쌍으로 딕셔너리를 만들고 면수 dict_data 에 저장
dict_data = {"a": 1, "b" : 2 , "c" : 3}

# 판다스 Series() 함수로 dict 를 series 로 변환
sr = pd.Series(dict_data)

# sr 의 자료형 출력
print(type(sr))
print("\n")
# 변수 sr 에 저장되어 있는 시리즈 객체를 출력
print(sr)