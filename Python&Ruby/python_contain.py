#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

family = "HSH", "JHS", "HHJ1", "HHJ2"
print(family) # ('HSH', 'JHS', 'HHJ1', 'HHJ2')

print(type("Hello World!")) # <class 'str'>

family = ["HSH", "JHS", "HHJ1", "HHJ2"]
print(type(family)) # <class 'list'>
print(family) # ['HSH', 'JHS', 'HHJ1', 'HHJ2']
print(family[0]) # HSH / [0] → index(순서)
print(family[3]) # HHJ2

family2 = ["KWS", "JHK", "KJH1", "KJH2"]
family2[3] = "tory" # KJH2를 tory로 변경
print(family2) # ['KWS', 'JHK', 'KJH1', 'tory']

family = "HSH", "JHS", "HHJ1", "HHJ2"
print(type(family)) # <class 'tuple'>
# tuple : 셀 수 있는 수량의 순서있는 열거

# type() : 해당 값의 datatype 출력

# list와 tuple의 차이
# list : 내부의 값을 변경하거나 삭제 가능
# tuple : 내부의 값이 변하지 않음
