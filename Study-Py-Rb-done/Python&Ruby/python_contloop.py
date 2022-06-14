#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

fam = ["HSH", "JHS", "HHJ1", "HHJ2", "ex"]
i = 0
while i < len(fam):
# len(fam)을 통해 내용의 개수만큼 반복수 변경
    print(fam[i])
    # i값을 index로 지정해서 해당 값 출력
    i = i + 1
# 결과
# HSH
# JHS
# HHJ1
# HHJ2
# ex (추가한 값)
