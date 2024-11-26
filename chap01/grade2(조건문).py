1 1330	두 수 비교하기
A, B = map(int, input().split())
if A > B:    
    print(">")
elif A < B:
    print("<")
else :
    print("==")

2	9498	시험 성적
파이썬 조건문 내에서의 부등식
다른 언어와 다르게 파이썬은 조건문안에서 수학의 부등식도 사용가능
x > 0 and x < 20, 0 < x < 20 둘다 사용가능하다.
score  = int(input())
if 100 >= score  >= 90:
    print("A")
elif score  >= 80:
    print("B")
elif score  >= 70:
    print("C")
elif score  >= 60:
    print("D")
else : print("F")


3	2753	윤년
y  = int(input())
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print(1)
else:
    print(0)

4	14681	사분면 고르기
x  = int(input())
y  = int(input())
if x > 0 and y > 0: 
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)

5 2884 알람 시계
H, M = map(int, input().split())
time = H * 60 + M
etime = time - 45
eh = etime // 60
em = etime % 60
if eh < 0:
    eh += 24
print(eh, em)

6 2525 오븐 시계
A, B = map(int, input().split())
C = int(input())
endtime = A * 60 + B + C
endhour = ( endtime // 60) % 24 # 24로 나눠질때만 0으로 바꿔주고 다른값들은 그대로 저장
endmin = endtime % 60
print(endhour, endmin)

7 2480 주사위 세개
a, b, c = map(int, input().split())
if a == b == c:
    print(10000 + a * 1000)
elif a == b or a == c:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    print(max(a, b, c) * 100)