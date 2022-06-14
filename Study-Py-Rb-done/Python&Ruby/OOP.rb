name_1 = String.new("HHJ")
name_2 = String.new("JHS")
fam_1 = Array.new()
# String, Array - class / String.new("XXX") - instance

puts(name_1) # HHJ
puts(name_2) # JHS

puts(name_1.reverse()) # JHH
puts(name_2.reverse()) # SHJ
# 해당 변수에 대한 내용을 뒤집음

puts(name_1.downcase()) # hhj
puts(name_2.downcase()) # jhs
# 해당 변수에 대한 내용을 소문자화

puts(name_1.size()) # 3
puts(name_2.size()) # 3
# 해당 변수에 대한 내용의 글자 수

print(fam_1.push("HHJ")) # ["HHJ"]
print(fam_1.push("JHS")) # ["HHJ", "JHS"]
# 변수로 지정된 배열에 해당 값을 추가

print(fam_1.join(" / ")) # HHJ / JHS
# 변수로 지정된 배열의 인자를 해당 값으로 합쳐줌
