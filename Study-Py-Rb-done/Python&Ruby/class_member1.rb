require "date"
# date라는 class 불러오기

d1 = Date.new(2022, 06, 01)
d2 = Date.new(1996, 12, 10)
d3 = Date.new(1973, 04, 20)
# Date는 ruby에 내장되어있는 class
puts(d1.strftime("%y %b %d %a")) # 결과 : 22 Jun 01 Wed
puts(d2.strftime("%y %b %d %a")) # 결과 : 96 Dec 10 Tue
puts(d3.strftime("%y %b %d %a"))
# %y : 년 / %b : 월 / %d : 일 / %a : 요일

puts(d1.year()) # 결과 : 2022
puts(d1.day()) # 결과 : 1
puts(d2.year()) # 결과 : 1996
puts(d2.month()) # 결과 : 12
# year, day, month는 인스턴스 소속의 메소드
# d1, d2는 자신의 날짜를 가지고 있는 객체

print("현재 날짜 : ", Date.today())
# 현재 날짜 : 2022-06-01
# 오늘 날짜 출력
# today는 인스턴스 소속이 아닌 class 소속의 메소드

puts(Date.year()) # 결과 : Error
puts(d1.today()) # 결과 : Error

# 인스턴스에 따라 다르게 동작해야 하는 메소드는 인스턴스 소속
# 인스턴스와 상관없이 동작하는 메소드는 클래스 소속
