# 모듈을 파일로 따로 나눌 때
require_relative("import_ex3")
require_relative("import_ex4")
# require_relative를 통해 module의 경로를 잡아주고 불러옴

puts(Example1.a()) # 결과 : A

puts(Example1.b()) # 결과 : B

puts(Example2.a()) # 결과 : AA

puts(Example2.b()) # 결과 : BB

# === import_ex3.rb 내용 ===
# module Example1
#   module_function()
#   def a()
#     return "A"
#   end

#   def b()
#       return "B"
#   end
# end

# === import_ex4.rb 내용 ===
# module Example2
#   module_function()
#   def a()
#     return "AA"
#   end

#   def b()
#       return "BB"
#   end
# end
