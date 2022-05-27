fam = ["HSH", "JHS", "HHJ1", "HHJ2"]
puts(fam.class) # Array
puts(fam.length) # 4 (배열의 총 개수)
fam.push("tory") # 해당하는 값을 맨 뒤에 추가
puts(fam)
# 결과
# HSH
# JHS
# HHJ1
# HHJ2
# tory (추가)
print(fam) # ["HSH", "JHS", "HHJ1", "HHJ2", "tory"]

fam.delete_at(4)
puts(fam)
# 결과
# HSH
# JHS
# HHJ1
# HHJ2
# (tory) 삭제
print(fam) # ["HSH", "JHS", "HHJ1", "HHJ2"]
