#!python
print("content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

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

#Boolean (참과 거짓으로 이루어진 값)
print(True)
print(False)

#Expression (표현식)
print(1+1) #2 도출
print("Hello "+"World") #Hello World 도출

#Comparison Operator (비교 연산자)
print(1==1) #True
print(1<1) #False
print(1<3) #True

#포함된 텍스트 찾기
print("world" in "Hello World") #False
print("Hello" in "Hello World") #True

#포함된 파일 찾기 (Cmd상에서는 왜 안되는지 모름)
import os.path
print(os.path.exists("String.py"))

#Conditional (조건문)
# if xxx : # → 반드시 True/False인 Boolean 값이 와야함
    # yyy

'''
user_PW = input("password?")
if user_PW == "hhj": #hhj라는 비밀번호를 설정, -user_input과 hhj가 같다면?-을 의미
    print("Welcome Master") #비밀번호가 맞을 시 뜨는 문구 (들여쓰기의 경우, 같은 블럭의 경우 같은 선상에 있어야 함)
else:
    print("Get Out!") #비밀번호가 틀렸을 시 나오는 문구
'''

'''
if user_ID == "hhj":
    if user_PW == "1210":
        print("Welcome Master")
    else:
        print("Get Out!")
else :
    print("Get Out!")
'''

print("-------------------")

#Logical Operator (논리 연산자)
user_ID = input("ID?")
user_PW = input("PW?")
if user_ID == "hhj" and user_PW == "1210": #두 조건을 모두 만족시키도록 and를 사용
    print("Welcome Master")
elif user_ID == "hsh" and user_PW == "0802": #조건을 추가하려면 else + if인 elif사용
        print("Welcome Father")
elif user_ID == "jhs" and user_PW == "7304": #조건을 추가하려면 else + if인 elif사용
        print("Welcome Mother")
else:
    print("Get Out!")

print("-------------------")

#List (일종의 수납장)
List = [1, "four", 9, 16, 25, 30] # → []안의 것들을 원소(element)라고 부름
print(List[1])
print(List[0])
print(List[4])

print(len(List)) #List 내의 element의 수

List[1] = 4 #elment 값 변경
print(List)

del List[1] #index(순서)를 이용한 elment 삭제
print(List)

List.insert(2, 75) #index(순서)를 이용한 elment 추가
print(List)

List.append("hhj") #끝에 element 추가
print(List)

print("hhj".capitalize()) #앞글자 대문자로 변환

print("-------------------")

#Dictionary (dic)
family = {"father" : "hsh", "mother" : "jhs", "son1" : "hhj", "son2" : "hhj2"}
print(family["father"])

print("-------------------")

#Loop (반복문)
for hhj in ["a", "b", "c"]: #element인 a,b,c를 hhj 값으로 입력
    print(hhj)

print("-------------------")

#range의 수 만큼 반복
for jhs in range(5):
    print(jhs)
