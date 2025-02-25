#연산자 --> 변수나 값들을 연산(계산)하는 기호
#산술 연산자 +,-,*,/(정수형 나누기),//(실수형 나누기), %(나머지), ** 숫자 연산
#대입 연산자 ---> +=,-=,=,*=/= 대입할 때 씀.
#비교 연산자 !=(같지 않다), ==(같다), >, <, >=, <= 크기 비교할 때 씀
#논리 연산자 --> not, and, or  논리
#부호 연산자 - 음수
#조건 연산자 Result 1 if 조건식 else result2  조건 연산

#대입연산자  --> 변수에 값을 저장할 때 사용
# = 값을 할당
# += 더하고 할당  a+=5  --> a= a+5
# -= 빼고 할당 a-=5  --> a=a-5
# *+ 곱하고 할당 a*=5 --> a= a*5
# /= 니누고 할당

x = 10
#x += 10 #더하고 대입(할당) x = x+10
#x -=5 # 빼고 대입(할당) x = x - 5
#x *=3 # 곱학고 대입(할당) x = x *3
#x /= 2  / 하나 쓰면 실수몫 즉 값이 5.0 나오고 // 두개 쓰면 정수값 즉 값이 5가 나온다.
#x **=2
#print(x)

#비교연산자 --> 두 값을 비교해서 True or False 반환
# == 같음  5==5  True
# != 다름  5!=3  True
# > 크다   7>3 True
# < 작다   7>3 False
# >= 크거나 같다
# <= 작거나 같다

# x = 10
# y = 20
# z = 10
# print(x == z) #같다
# print(x != z) #같지 않다
# print(x > y)
# print(x > z)
# print(x < y)
# print(x >= z)
# print(x <= y)

#논리 연산자 --> 조건을 조합할 때 사용 (and, or, not)
#and 둘 다 참이면 True, True and False  결과 False
#or 하나라도 참이면 True, True or Flase 결과 True
#not 반대 값 반환 not True  결과 False

# a = True
# b = False
# print( a and b)
# print( a or b)
# print(not a and b)
# print(a or (a and b))

#조건연산자
#if - else 문을 한 줄로 표현하는 방법(삼항연산자)
#조건식이 참이면 값1을 반환
#조건식이 거짓이면 값2을 반환
#값1 if 조건식 else 값2  -> 조건식이라서 True False가 나옴. True면 값1, False 면 값2

#조건연산자(삼항연산자)
# a = 10
# b = 20
# max_value = a if a > b else b
# print(max_value)
# min_value = a if a < b else b
# print(min_value)
#
# score = 85
# grade = "A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else "D")) #계속 엮어쓸 수 있다
# print(grade)
#
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# else:
#     print("C")

#복습

# 문자열의 인덱싱 문자열 [인덱스]
# 문자열의 슬라이싱
# 문자열 [start : end : step]

# 다양한 문자열 함수
# index()  찾는거, 없는 애를 찾을려면 오류 strip() -->공백제거
# find() 찾는거, 없는 애를 찾으면 -1을 뱉어냄
# join() 합치는거, count() 해당문자열이 몇개 들어있는지 세는거
# replace() 대체. 원래값이랑 변하는 값

# 컬렉션(리스트, 튜플, 딕셔너리, 세트) --> 여러개의 데이터를 넣고 관리하는 구조
# 리스트 순서가 있고 중복가능 요소 추가/삭제가능 ==> 변경가능
# [] 를 쓴다. fruits = ["apple", "banana", "cherry"]
mixed_list = ["안녕하세요", 12, True]

# 튜플
# 순서가 있지만, 요소 변경 불가능
# birth_info = ("김철수", 1995, "서울")
# () 소가로 사용, 리스트는 대가로[]
# 변경이 불가능해서 추가 삭제 등이 안됨

# 딕셔너리
# # 키 - 값 쌍으로 데이터를 저장하는 자료형
# # 키는 고유해야하며, 키를 사용해서 빠르게 접근 가능
# 중괄호{}를 둘러싸야있고 각 키와 값은 : 으로 구분, 쌍은 쉼표로 구분.
# person = {
#     "이름" : "철수"
#     "나이" : 25
#     "취미" : ["독서","영화감상"]

# 세트
# 중복을 허용하지 않고, 순서가 없는 데이터 모음
# 수학에서 말하는 집합 개념과 유사함. --> 교집합, 차집합, 합집합등을 사용가능
# fruits = {"사과", "바나나", "오렌지"}
# fruits = {} --> 빈딕셔러니
# empty_set = set() --> 빈세트는 이렇게 씀. 그냥 비우면 딕셔너리

