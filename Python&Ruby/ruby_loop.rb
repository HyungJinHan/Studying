i = 0
while i < 10 do
  puts("Hello Ruby "+(i*9).to_s()+"")
  # Hello Ruby은 문자열, i는 숫자이기 때문에
  # 합쳐서 출력이 불가능
  # i를 문자화 시켜서 합쳐서 출력해야 함
  # i.to_s() : 숫자인 i를 문자화 시킴
  # i에 9를 곱하도록 지정 (i*9).to_s()
  # Hello Python에 "+(i*9).to_s()+" 추가
  # +xxx+ : 문자열 + xxx + 문자열 의미
  i = i + 1
end
# 결과
# Hello Ruby 0
# Hello Ruby 9
# Hello Ruby 18
# Hello Ruby 27
# Hello Ruby 36
# Hello Ruby 45
# Hello Ruby 54
# Hello Ruby 63
# Hello Ruby 72
# Hello Ruby 81
