#!python
print("content-type: text/html; charset=utf-8\n")

#String
print("Hello World\n") #\n은 줄바꿈표시
print('Hello World\n')
print("Hell'o' World\n")
#여기서 \는 escape (바로 뒤에오는 것을 문자취급해줌)
print("Hell'o' \"W\"orld")

#Newline (\n)
print('H')
print('e')
print('l')
print('l')
print('o')
print('H\ne\nl\nl\no')

#Docstring (한번에 모두 줄바꿈)
print('''
H
e
l
l
o
''')

#String Operation
a ='Hello Python'
print(a)

#String Length
print(len(a))

#String Slice
print(a[0]) #단순히 순서대로 하나만
print(a[0:4]) #0~4까지의 문자 추출
print(a[0] + a[1] + a[3] + a[7] + a[11]) #하나씩 더해서 문자 도출

#Repeat
print((a+'\n')*2) #문장과 줄바꿈을 한꺼번에 2번 반복

#변수 & 여러줄 주석
'''
name = 'Father, Mother'
age = '17'
print('To '+name+'. Lorem ipsum dolor sit amet, consectetur '+age+' adipisicing elit,sed '+name+' do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate '+name+' velit esse '+name+' cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit '+name+' anim id est laborum.')
'''

#Positional Formatting (순서대로 치환하기)
'''
print('To {}. Lorem ipsum dolor sit amet, consectetur {} adipisicing elit,sed {} do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate {} velit esse {} cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit {} anim id est laborum.'.format('Father, Mother', 17, 'Father, Mother', 'Father, Mother', 'Father, Mother', 'Father, Mother'))
'''

#Named Placeholders (지정하여 치환하기)
#예를 들어 age의 값에 무조건 숫자를 넣어야 한다면 {age:d(digit)}으로 입 (d는 digit의 약자)
print('To {name}. Lorem ipsum dolor sit amet, consectetur {age:d} adipisicing elit,sed {name} do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate {name} velit esse {name} cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit {name} anim id est laborum.'.format(name='Father, Mother', age=17))
