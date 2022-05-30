def a3()
    return "aaa"
end
puts(a3()) # 결과 : aaa

def a2()
    a = "aa"
    return a
end
puts(a2()) # 결과 : aa

def a1()
    puts("before")
    return "a"
    puts("after")
end
a1() # 결과 : before
puts(a1())
 # 결과
 # before
 # a
 # (return은 함수를 종료하므로 after 출력 X)
