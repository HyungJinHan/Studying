PW_1 = "hhj"
PW_2 = "hsh"
puts("아이디를 입력해주세요.")
PW_input = gets.chomp()

if PW_1 == PW_input or PW_2 == PW_input
# or을 통해 둘 중에 하나가 맞을 시 True
  puts("Welcome!")
else
  puts("GET OUT!")
end
