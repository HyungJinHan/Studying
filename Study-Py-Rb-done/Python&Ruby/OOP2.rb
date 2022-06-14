class C
  def initialize(n1)
  # 생성자
    @value = n1
  end
  def show()
    puts(@value)
  end
end

c1 = C.new(10)
c1.show() # 결과 : 10
# 인스턴스에 소속된 메소드를 외부에서 사용하는 형식으로만 사용 가능
