family = "HSH", "JHS", "HHJ1", "HHJ2"
puts(family)
# HSH
# JHS
# HHJ1
# HHJ2
puts(family.class) # Array
puts(family[0]) # HSH

family = ["HSH", "JHS", "HHJ1", "HHJ2"]
puts(family)
# HSH
# JHS
# HHJ1
# HHJ2
puts(family.class) # Array
# python과 다르게 []의 유무와는 상관없이 array(배열)

family2 = "KWS", "JHK", "KJH1", "KJH2"
family2[3] = "tory" # KJH2를 tory로 변경
puts(family2)
# KWS
# JHK
# KJH1
# tory
