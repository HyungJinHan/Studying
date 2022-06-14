# === 모듈을 파일로 따로 나누지 않을 때 ===

puts("아이디를 입력해주세요.")
input_id = gets.chomp()

module Module_login
  module_function()
  # module내의 여러 함수를 module의 함수로써 작동하도록 하는 코드
  def login(id)
    fam = ["hsh", "jhs", "hhj1", "hhj2"]
    for item in fam do
      if item == id
      # 함수를 정의할 때의 () 안의 id값과 같은지를 확인
        return true
        # return값을 true로 지정을 하면 밑의 if문에서 true의 값에 해당하는 값이 출력
      end
    end
    return false
    # return값을 false로 지정을 하면 밑의 if문에서 false의 값에 해당하는 값이 출력
  end
end

if Module_login.login(input_id)
  puts("Hello! "+input_id)
  # hhj1 입력 결과 : Hello! hhj1
else
  puts("GET OUT!")
end
