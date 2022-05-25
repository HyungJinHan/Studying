PW_1 = 1210
PW_2 = 0420
PW_input = 0420

if PW_1 == PW_input
# PW_1 == PW_input : Hello Master
  puts("Hello Master")
elsif PW_2 == PW_input
# PW_2 == PW_input : Hello User (elsif 주의)
  puts("Hello User")
else
# PW_1, PW_2 != PW_input : GET OUT!
  puts("GET OUT!")
end
