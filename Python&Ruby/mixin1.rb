module M1
  def m1_m()
    return "Method 1"
  end
end

module M2
  def m2_m()
    return "Method 2"
  end
end

class C
  include M1, M2
end

class C1
  prepend M1, M2
end

c = C.new()
print(c.m1_m(),", ",c.m2_m())

print("\n")

c1 = C1.new()
print(c1.m1_m(),", ",c1.m2_m())

# include와 prepend는 기능 자체로는 유사
# class에 대한 다중 상속이 아닌, module로부터 기능을 가져와 쓴다는 개념
