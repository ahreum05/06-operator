"""
아이덴티티 연산자 : 레퍼런스 변수의 값이 같은 지 검사
1) is
=> True : 주소가 같음, False : 주소가 같지 않음
1) is not
=> True : 주소가 같지 않음, False : 주소가 같음
"""
a = 1
b = 2
c = 1
d = a

# id() : 레퍼런스 변수의 값을 출력함
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print('-' * 20)

print(a is b)
print(a is c)
print(a is d)
print('-' * 20)

print(a is not b)
print(a is not c)
print(a is not d)
print('-' * 20)

# 데이터가 같은 지 검사
# == : 데이터가 같은 지 검사
# != : 데이터가 같지 않은 지 검사
print(a == b)
print(a == c)
print(a == d)
print('-' * 20)

print(a != b)
print(a != c)
print(a != d)
print('-' * 20)

print('ab' == 'ab')
print('ab' != 'ab')




