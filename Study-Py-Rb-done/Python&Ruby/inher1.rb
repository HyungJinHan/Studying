class Class1
  def method1()
    return "m1"
  end
end

class Class2 < Class1
# 상속받을 class를 < xxx으로 지정
  def method2()
    return "m2"
  end
end

class Class3 < Class2
# 상속받을 class를 < xxx으로 지정
  def method3()
    return "m3"
  end
end

c1 = Class1.new()
puts(c1.method1()) # 결과 : m1

c2 = Class2.new()
puts(c1.method1()) # 결과 : m1 (Class1에게 상속받음)
puts(c2.method2()) # 결과 : m2

c3 = Class3.new()
puts(c1.method1()) # 결과 : m1 (Class1에게 상속받음)
puts(c2.method2()) # 결과 : m2 (Class2에게 상속받음)
puts(c3.method3()) # 결과 : m3

# 상속을 통해서 인스턴스 내에 없는 메소드 출력 가능
# Class1의 메소드의 값이 변경되면 Class2, Class3의 내용도 바뀜
