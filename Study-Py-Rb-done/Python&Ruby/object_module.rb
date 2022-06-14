require_relative "lib"
# module을 불러오기 위한 코드

obj = Lib::A.new()
# Lib::A : lib이라는 module 내의 A라는 class를 사용하기 위함

puts(obj.a()) # 결과 : a

# lib.rb 내용
# module Lib
# # module로써 사용하기 위한 코드
#   class A
#     def a()
#       return "a"
#     end
#   end
# end
