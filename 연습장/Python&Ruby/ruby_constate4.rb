ID_1 = "hhj"
puts("아이디를 입력해주세요.")
ID_input = gets.chomp()

PW_1 = "1210"
puts("비밀번호를 입력해주세요.")
PW_input = gets.chomp()

if ID_1 == ID_input
  if PW_1 == PW_input
    puts("Welcome Master!")
    # ID와 PW가 맞은 경우
  else
    puts("잘못된 비밀번호입니다.")
    # ID는 맞고 PW가 틀린 경우
  end
  # PW_1에 대한 if문의 end
else
  puts("잘못된 아이디입니다.")
  # ID가 틀린 경우
end
# 전체적인 ID_1에 대한 if문의 end
