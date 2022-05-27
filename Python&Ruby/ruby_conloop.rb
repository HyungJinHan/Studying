i = 0
while i < 5 do
  if i != 2
    puts(i)
  end
  i = i + 1
end
# 결과 (2와 같으면 False, 그래서 2와 다른 값만 출력)
# 0
# 1
# 3
# 4
# -----------------------------------
i = 0
while i < 5 do
  if i == 2
    puts(i)
  end
  i = i + 1
end
# 결과 (2와 같은 것만 출력)
# 2
# -----------------------------------
i = 0
while i < 5 do
  if i == 2
    break
  end
  puts(i)
  i = i + 1
end
# 결과 (2와 같아지면 끊기)
# 0
# 1
