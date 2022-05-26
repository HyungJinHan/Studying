#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

in_str = input("입력해주세요.\n")
print(in_str.capitalize() + " World")
# ex : hello 입력 → Hello World
