#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

fam = ["HSH", "JHS", "HHJ1", "HHJ2"]
print(type(fam)) # <class 'list'>
fam.append("tory") # ['HSH', 'JHS', 'HHJ1', 'HHJ2', 'tory']
del(fam[4]) # ['HSH', 'JHS', 'HHJ1', 'HHJ2']
# index에 해당하는 값 삭제
# 해당하는 값을 맨 뒤에 추가
print(len(fam)) # 4 (배열의 총 개수)

fam_2 = "HSH", "JHS", "HHJ1", "HHJ2"
print(type(fam_2)) # <class 'tuple'>
fam_2.append("tory") # Error
del(fam_2[2]) # Error
# tuple은 내부의 값 수정 불가
