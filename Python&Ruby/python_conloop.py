#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

i = 0
while i < 5:
    if i != 2:
        print(i)
    i = i + 1
# 결과 (2와 같으면 False, 그래서 2와 다른 값만 출력)
# 0
# 1
# 3
# 4
# -----------------------------------
i = 0
while i < 5:
    if i == 2:
        print(i)
    i = i + 1
# 결과 (2와 같은 것만 출력)
# 2
# -----------------------------------
i = 0
while i < 5:
    if i == 2:
        break
    print(i)
    i = i + 1
# 결과 (2와 같아지면 끊기)
# 0
# 1
