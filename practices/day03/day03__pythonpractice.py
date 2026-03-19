# 파이썬 기초 문법 연습
# 파이썬 기본에 대한 연습의 필요성을 느껴 정리해보았다.


# 1. 변수와 자료형
name = "dayoung"  # 문자열 변수
sentence = """Hello,
 World!
 줄바꿈 가능"""  # 문자열 변수

age = 30        # 정수 변수
height = 1.65   # 실수 변수
is_student = True  # 불리언 변수

print(sentence)


# 2. 리스트와 딕셔너리
fruits = ["apple", "banana", "cherry"]  # 리스트 (배열과 유사)
person = {  # 딕셔너리 (key, value 쌍)
    "name": "Bob",
    "age": 25,
    "city": "New York"
}

print(fruits) # 리스트 전체 출력
print(fruits[0]) # 리스트의 첫 번째 요소 출력
print(person) # 딕셔너리 전체 출력
print(person["city"]) # 딕셔너리에서 "city" 키의 값 출력

# 3. 조건문과 반복문
if age > 18:
    print("성인입니다.") # 위의 age변수를 사용하여 조건문 사용

for fruit in fruits:
    print(fruit)    # fruits 리스트의 각 요소를 반복하여 출력


# 4. 함수 정의
def greet(name):
    return f"Hello, {name}!"
print(greet("Charlie"))
# greet이라는 함수를 정의하여 이름을 출력
# 이때 return f"Hello, {name}!"는 문자열 포매팅을 사용


# 5. 클래스 정의
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."
    
person1 = Person("David", 40)
print(person1.introduce())
# 클래스의 첫 글자는 대문자로 시작
# __init__ 메서드는 클래스의 생성자로, 객체가 생성될 때 자동으로 호출되어 초기화 작업을 수행
# self는 클래스의 인스턴스 자신을 가리키는 매개변수로, 클래스 내에서 인스턴스 변수에 접근할 때 사용
# 초기화 후 클래스 안에 함수를 정의하여 사용
# person1이라는 객체를 생성하여 클래스를 선언



# 6. 예외 처리
try:
    result = 10 / 2
    print(result)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
# try-except 블록을 사용하여 예외 처리를 수행



# # 7. 파일 입출력
# with open("example.txt", "w") as file:
#     file.write("Hello, World!")
# # with 구문을 사용하여 파일을 열고, "w" 모드로 쓰기 작업을 수행

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# with 구문을 사용하여 파일을 열고, "r" 모드로 읽기 작업을 수행하여 파일의 내용을 출력


# 8. 라이브러리 사용
import math
print(math.sqrt(16))  # 제곱근 계산
import random
print(random.randint(1, 10))  # 1부터 10 사이의 랜덤 숫자

# 9. 리스트 컴프리헨션
squares = [x**2 for x in range(10)]
print(squares)
# 리스트 안에 for문을 사용하여 0부터 9까지의 숫자의 제곱을 계산하여 리스트로 생성


# 10. 람다 함수
add = lambda x, y: x + y
print(add(5, 3))
# 람다 함수는 익명 함수로, 간단한 함수를 한 줄로 정의할 때 사용

