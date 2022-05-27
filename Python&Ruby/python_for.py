#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

fam = ["HSH", "JHS", "HHJ1", "HHJ2"]
for item in fam: # = for item in ["HSH", "JHS", "HHJ1", "HHJ2"]:
# fam이라는 배열에 담긴 item(문법)을 의미
    print(item)
# 결과
# HSH
# JHS
# HHJ1
# HHJ2

for item in range(5):
# 0~4까지의 숫자 배열을 출력
    print(item)
# 결과
# 0
# 1
# 2
# 3
# 4

for item in range(5, 11):
# 5~10까지의 숫자 배열을 출력
    print(item)
# 결과
# 5
# 6
# 7
# 8
# 9
# 10
