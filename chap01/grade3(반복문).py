
# Python에서  f-string 사용하는 법 
# 문자열 앞에 f 또는 F 접두사를 붙이고 변수나 표현식은 {} 중괄호로 감싸준다. 
N = int(input())
for i in range(1, 10):
    print(f"{N} * {i} = {N*i}")

#2	10950	A+B - 3
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(A + B)

# 3	8393	합
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)
#가우스의 합, 등차수열
n = int(input())
sum = n * (n + 1) // 2
print(sum)

# 4	25304	영수증
X = int(input())
N = int(input())
total = 0
for _ in range(N):
    a, b = map(int, input().split())
    total += a * b
if X == total:
    print("Yes")
else : print("No")

# 5	25314	코딩은 체육과목 입니다
N = int(input())
num = N // 4
print("long " * num + "int" )

# 6	15552	빠른 A+B
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

# 7	11021	A+B - 7
import sys
T = int(sys.stdin.readline())
for i in range(1, T+1):
    a, b = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {a + b}")

# 8	11022	A+B - 8
import sys
T = int(sys.stdin.readline())
for i in range(1, T+1):
    a, b = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {a} + {b} = {a + b}")

# 9	2438	별 찍기 - 1
import sys
a = int(sys.stdin.readline())
for i in range(1, a+1):
    print("*" * i)

# 10	2439	별 찍기 - 2
import sys
a = int(sys.stdin.readline())
for i in range(1, a+1):
    print(' ' * (a-i) + "*" * i)

# 11	10952	A+B - 5
while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    print(A + B)

# 12	10951	A+B - 4
while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except EOFError:
        break
