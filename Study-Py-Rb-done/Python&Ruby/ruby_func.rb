def ex_1() # ex_1을 함수로 정의
    puts("aaa")
    # def ex_1 밑으로의 내용은 ex_1이라는 함수의 본문
    i = 0
    while i < 2 do
      puts("Hello Function "+i.to_s()+"")
      i = i + 1
    end
end

ex_1()
# 정의된 함수를 호출
# 결과
# aaa
# Hello Function 0
# Hello Function 1
