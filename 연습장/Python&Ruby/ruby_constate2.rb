PW_1 = "1210"
PW_2 = "0420"
puts("아이디를 입력해주세요.")
PW_input = gets.chomp()
# gets.chomp()를 통해 사용자의 입력값을 가져옴

if PW_1 == PW_input
# PW_1 == PW_input : Hello Master
# python과 마찬가지로 PW_1과 in_str의 datatype이
# datatype이 숫자와 문자열로 다르기 때문에
# 숫자를 문자열로 바꿔야 True값 출력
  puts("Hello Master")
elsif PW_2 == PW_input
# PW_2 == PW_input : Hello User (elsif 주의)
  puts("Hello User")
else
# PW_1, PW_2 != PW_input : GET OUT!
  puts("GET OUT!")
end
