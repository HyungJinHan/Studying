# 모듈을 파일로 따로 나누지 않을 때
module Example1 # 첫 글자는 무조건 대문자로
  module_function()
  # module내의 여러 함수를 module의 내부 함수로써 작동하도록 하는 코드
  def a()
    return "A"
  end
  def b()
    return "B"
  end
end

module Example2
  module_function()
  def a()
    return "AA"
  end
  def b()
    return "BB"
  end
end

puts(Example1.a()) # 결과 : A

puts(Example1.b()) # 결과 : B

puts(Example2.a()) # 결과 : AA

puts(Example2.b()) # 결과 : BB
