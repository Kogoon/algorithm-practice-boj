# 2020.01.05
"""
acmicpc.net/problem/9498
문제집 : 백준에서 가장 많이 풀린 문제 TOP 100 (입문자 추천) - njw1204
문제: 시험 점수를 입력받아 90 ~ 100 점은 A, 80 ~ 89 점은 B, 70 ~ 79점은 C,
    60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
입력: 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
출력: 시험 성적을 출력한다. 
"""
score = int(input())
if (100 >= score >= 90):
    print("A")
elif (90 > score >= 80):
    print("B")
elif (80 > score >= 70):
    print("C")
elif (70 > score >= 60):
    print("D")
else:
    print("F")
