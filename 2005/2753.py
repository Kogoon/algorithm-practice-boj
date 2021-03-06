# 2020.01.28
"""
acmicpc.net/problem/2753
문제집 : 처음 프로그래밍을 접할 때 - jaehoo1
문제: 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
    윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때 이다.
    예를 들어, 2012년은 4의 배수라서 윤년이지만, 1900년은 4의 배수이지만, 100의 배수이기 때문에 윤년이 아니다.
    하지만, 2000년은 400의 배수이기 때문에 윤년이다. 
입력: 첫째 줄에 연도가 주어진다. 연도는 1보다 크거나 같고, 4000보다 작거나 같은 자연수이다.
출력: 첫째 줄에 윤년이면 1, 아니면 0을 출력한다.

def find_leap_year(year):
    if year % 100 == 0 and year % 400 == 0:
        return 1
    else:
        if year % 4 == 0:
            return 1
        else: 
            return 0

year = int(input())
print(find_leap_year(year))
"""
import sys
input = sys.stdin.readline

year = int(input())
#윤년이면 1, 아니면 0

if year%4==0:
    if year%400==0:
        print("1")
    elif year%100!=0:
        print("1")
    else:
        print("0")
else:
    print("0")

