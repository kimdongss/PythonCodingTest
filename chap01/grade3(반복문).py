
# Python에서  f-string 사용하는 법 
# 문자열 앞에 f 또는 F 접두사를 붙이고 변수나 표현식은 {} 중괄호로 감싸준다. 
# 그냥 했다가 개같이 틀렸네 ........
# N = int(input())
# for i in range(1, 10):
#     print(f"{N} * {i} = {N*i}")

# T = int(input())
# for _ in range(T):
#     A, B = map(int, input().split())
#     print(A + B)


# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     sum += i
    
# print(sum)

# X = int(input())
# N = int(input())
# total = 0
# for _ in range(N):
#     a, b = map(int, input().split())
#     total += a * b
# if X == total:
#     print("Yes")
# else : print("No")

# N = int(input())
# num = N // 4
# print("long " * num + "int" )

# import sys
# T = int(sys.stdin.readline())
# for _ in range(T):
#     a, b = map(int, sys.stdin.readline().split())
#     print(a + b)

# import sys
# T = int(sys.stdin.readline())
# for i in range(1, T+1):
#     a, b = map(int, sys.stdin.readline().split())
#     print(f"Case #{i}: {a + b}")

# import sys
# T = int(sys.stdin.readline())
# for i in range(1, T+1):
#     a, b = map(int, sys.stdin.readline().split())
#     print(f"Case #{i}: {a} + {b} = {a + b}")

# import sys
# a = int(sys.stdin.readline())
# for i in range(1, a+1):
#     print("*" * i)

# import sys
# a = int(sys.stdin.readline())
# for i in range(1, a+1):
#     print(' ' * (a-i) + "*" * i)

# while True:
#     A, B = map(int, input().split())
#     if A == 0 and B == 0:
#         break
#     print(A + B)

while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except EOFError:
        break