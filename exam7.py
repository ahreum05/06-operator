"""
소속 연산자 : 어떤 데이터가 특정 데이터안에 포함되어 있는 지 검사
1) in
=> True : 존재함, False : 존재하지 않음
2) not in
=> True : 존재하지 않음, False : 존재함
"""
st1 = "abcdefg"
print('ab' in st1)
print('xy' in st1)
print(None in [1, 2, 3])
print('-' * 20)

print('ab' not in st1)
print('xy' not in st1)
print('-' * 20)

