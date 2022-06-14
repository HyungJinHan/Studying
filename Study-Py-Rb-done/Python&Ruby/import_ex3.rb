module Example1 # 첫 글자는 무조건 대문자로
# ruby는 모듈을 파일로 따로 나눌 수도, 나누지 않을 수도 있음
  module_function()
  # module내의 여러 함수를 module의 함수로써 작동하도록 하는 코드
  def a()
    return "A"
  end
  def b()
    return "B"
  end
end
