def a(num)
    puts(num)
    return "a"
end
a(10) # 결과 : 10

def A(num)
    return "A"*num
end
print(A(10)) # 결과 : AAAAAAAAAA (10*A)

print("\n")

def multiple(str, num)
    return str*num
end
print(multiple("AB", 3)) # 결과 : ABABAB
