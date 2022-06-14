# === 모듈을 파일로 따로 나눌 때 ===

require_relative("Module_login")
# require_relative를 통해 module의 경로를 잡아주고 불러옴

puts("아이디를 입력해주세요.")
input_id = gets.chomp()

if Module_login.login(input_id)
  puts("Hello! "+input_id)
  # hhj1 입력 결과 : Hello! hhj1
else
  puts("GET OUT!")
end

# === module_login.rb의 내용 ===

# module Module_login
#   module_function()
#   def login(id)
#     fam = ["hsh", "jhs", "hhj1", "hhj2"]
#     for item in fam do
#       if item == id
#         return true
#       end
#     end
#     return false
#   end
# end
