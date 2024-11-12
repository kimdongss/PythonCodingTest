# 입출력과 사칙연산

#2557 Hello World!
print("Hello World!")

#1000 A + B
A, B = map(int, input().split())
print(A + B)

#1001 A - B
A, B = map(int, input().split())
print(A - B)

#10998 A * B
A, B = map(int, input().split())
print(A * B)

#1008 A / B
A, B = map(int, input().split())
print(A / B)

#10869 사칙연산 +, -, *, /, //, %
A, B = map(int, input().split())

print(A + B)
print(A - B) 
print(A * B)
print(A // B)
print(A % B) 

#10926 ??!
id = input()
print(id + "??!")

# 18108 서기 불기 계산
y = int(input())
print(y - 543)

#10430 나머지
A, B, C = map(int, input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

#2588  세자리 곱셈
A = int(input())
B = int(input())
print(A * (B % 10))
print(A * ((B // 10) % 10))
print(A * (((B // 10) // 10) % 10))
print(A * B)

#11382 A+B+C
A, B, C = map(int, input().split())
print(A+B+C)

#10171
print("\\    /\\")
print(" )  ( \')")
print("(  /  )")
print(" \\(__)|")


#10172
print("|\\_/|")
print("|q p|   /}")
print('( 0 )\"\"\"\\')
print('|"^"`    |')
print("||_/=\\\\__|")