#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

PW_1 = 1210
PW_2 = 1234 # 0420 Python은 0으로 시작 X
# str(420).zfill(4)
# 420을 앞에 0을 붙여서 4자리 숫자로 만든다는 의#
PW_input = 1234

if PW_1 == PW_input:
# PW_1 == PW_input : Hello Master
  print("Hello Master")
elif PW_2 == PW_input:
# PW_2 == PW_input : Hello User (elsif 주의)
  print("Hello User")
else:
# PW_1, PW_2 != PW_input : GET OUT!
  print("GET OUT!")
