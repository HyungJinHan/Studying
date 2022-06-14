def a():
    return "C"

def aa():
    return "CC"

def aaa():
    return "CCC"

import import_ex1 as ex1, import_ex2 as ex2

print(ex1.a()) # 결과 : B
# as ex1를 추가하여 import_ex1를 ex1로 지정 가능

print(ex2.a()) # 결과 : C
