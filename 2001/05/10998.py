# 2020.01.05
"""
acminpc.net/problem/10998
문제집 : 백준에서 가장 많이 풀린 문제 TOP 100 (입문자 추천) - njw1204
문제: 두 정수 A와 B를 입력받은 다음, AxB를 출력하는 프로그램을 작성하시오
입력: 첫째 줄에 A와 B가 주어진다. (0<A, B<10)
출력: 첫째 줄에 AxB를 출력한다.
"""
A, B = map(int, input().split())
print(A * B)