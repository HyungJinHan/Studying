class Cs
  def Cs.class_method()
  # Cs라는 class 소속임을 지정해야 함
    puts("Class Method")
  end
  def instance_method()
    puts("Instance Method")
  end
end

Cs.class_method() # 결과 : Class Method
# class 소속의 메소드

i = Cs.new()
# 인스턴스 생성
i.instance_method() # 결과 : Instance Method
# 인스턴스 소속의 메소드

Cs.instance_method() # 결과 : Error
i.class_method() # 결과 : Error
