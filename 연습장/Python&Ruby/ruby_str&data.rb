puts("Hello World") # Hello World
puts("Hello "+"World") # Hello World
puts("Hello "*3) # Hello Hello Hello
# 문자열에는 빼기, 나누기는 없음

puts("Hello World"[0]) # H - 1(0)번째 문자
puts("Hello World"[1]) # e - 2(1)번째 문자
puts("Hello World"[2]) # l - 3(2)번째 문자
puts("Hello World"[3]) # l - 4(3)번째 문자

puts("hello world".capitalize()) # Hello world
# 제일 앞글자 대문자화

puts("hello world".upcase()) # HELLO WORLD
# 전체를 대문자화

puts("Hello World".length()) # 11
# 해당 문자열의 문자 개수

puts("hi World".sub("hi", "Hello")) # HELLO WORLD
# hi를 Hello로 치환

puts("Hello\nWorld") # HELLO
                     # WORLD
# \n (new line) : 줄바꿈

puts('Hello\nWorld') # Hello\nWorld
# Ruby는 ""와 ''의 기능이 다름

puts("Hello\tWorld") # Hello	World
# \t (tab) : 들여쓰기

puts("\a") # 경고음 재생
# \a (alert)

# Datatype
puts("100"+"100") # 100100 (문자로써의 100)
puts(100+100) # 200 (숫자로써의 100)
