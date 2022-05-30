5.times() {print("times ")} # while 반복문과 같음
# block을 5번 반복
# times는 함수, {}의 내용은 block
# 결과 : times times times times times

print("\n")

5.times() {|i| print(i)}
# |i|에 0부터 대입해서 5가 되기 전까지 print(i)를 통해 i를 출력
# 결과 : 01234

print("\n")

1.upto(5) {print("upto ")}
# 1부터 5까지 block 반복
# 결과 : upto upto upto upto upto

print("\n")

1.upto(5) {|hhj| print(hhj," Hello ")}
# |hhj|에 1부터 5까지 대입해서 print(hhj)를 통해 i를 출력
# 결과 : 1 Hello 2 Hello 3 Hello 4 Hello 5 Hello
# ||내의 값은 변수의 지정이므로 원하는 값으로 변수 지정 가능

print("\n")

["A", "B", "C"].each() {|i| print(i)} # for 문과 같음
# 변수인 i에 각각의 원소인 A, B, C를 대입하여 출력
# 결과 : ABC

print("\n")

["A", "B", "C"].each() {|i| print(i.downcase())}
# 변수인 i에 각각의 원소인 A, B, C를 대입하여 소문자로 출력
# 결과 : abc

print("\n")

arr = [100, 97, 56, 60, 80, 82, 70]
arr.delete_if {|value| print(value, " ")}
# 결과 : 100 97 56 60 80 82 70

print("\n")

scores = [100, 97, 56, 60, 80, 82, 70]
scores.delete_if() {|score| score <= 80}
print(scores)
# 삭제를 위해 지정한 범위의 값을 삭제
# 결과 : [100, 97, 82]
# 한 줄로 짧은 경우에 주로 사용

print("\n")

scores1 = [100, 97, 56, 60, 80, 82, 70]
scores1.delete_if() do
  |score|
  score <= 60
end
print(scores1)
# [100, 97, 80, 82, 70]
# 한 줄 이상의 긴 문법의 경우에 주로 사용
