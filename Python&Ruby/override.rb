class C1
  def m()
    return "Parent"
  end
end

class C2 < C1
  def m()
    return "Child"
  end
end

class C3 < C2
  def m()
    return super() + " HHJ"
    # 부모 class 사용을 위한 메소드
  end
end

o = C2.new()
puts(o.m())

o1 = C3.new()
puts(o1.m())

# Ruby의 super()
# super() : super()가 소속된 메소드 m()와 동일한 이름을 가진 메소드를 찾는 방식

# 결론 : Ruby에서의 super()는 해당 메소드와 동일한 메소드를 찾는다는 것을 의미
