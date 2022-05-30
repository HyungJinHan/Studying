def func_1()
  return "This is func_1"
end
puts(func_1())
# 결과
# This is func_1

def func_2 # () 생략 가능
  return "This is func_2"
end
puts(func_2())
# 결과
# This is func_2

def func_3 # () 생략 가능
  return "This is func_3"
end
puts(func_3) # () 생략 가능
# 결과
# This is func_3

def func_4(a)
# a = This is func_4
  return a
end
puts(func_4("This is func_4"))
# 결과
# This is func_4

def func_5 a # () 생략 후 띄어쓰기 가능
# a = This is func_4
  return a
end
puts(func_5("This is func_5"))
# 결과
# This is func_5

def func_6 a # () 생략 후 띄어쓰기 가능
# a = This is func_4
  return a
end
puts(func_6 "This is func_6") # () 생략 후 띄어쓰기 가능
# 결과
# This is func_6

def func_7
  "This is func_7"  # return 또한 생략 가능
end
puts func_7
# 결과
# This is func_7

def func_8
  a = 100
  b = 150
  a + b # 변수 지정 후에도 return을 생략 가능
end
puts func_8
# 결과 : 250

# puts 자체도 내장함수이기 때문에 () 생략 가능

puts func_1 # This is func_1
puts func_2 # This is func_2
puts func_3 # This is func_3
puts func_4 "This is func_4" # This is func_4
puts func_5 "This is func_5" # This is func_5
puts func_6 "This is func_6" # This is func_6
puts func_7 # This is func_7
puts func_8 # 250
