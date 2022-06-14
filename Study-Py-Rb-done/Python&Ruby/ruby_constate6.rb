puts("아이디를 입력해주세요.")
fam = ["hsh", "jhs", "hhj1", "hhj2"]
input_name = gets.chomp()

for item in fam do
# fam 내부의 item에 대한 반복문
  if item == input_name
  # fam 내부의 item와 input_name의 입력값이 같으면
    puts("Hello!, "+item)
    # hhj1 입력 결과 : Hello!, hhj1
    exit
    # if문이 끝나면 종료시키는 코드
  end
  # if item == input_name에 대한 end
end
# for item in fam do에 대한 end
puts("GET OUT!")
# abc라는 값이 fam의 item과 다를 경우 출력
