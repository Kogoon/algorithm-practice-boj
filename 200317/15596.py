# 2020.03.17
"""
acmicpc.net/problem/15596
문제: 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.
python : def solve(a: list) -> int
        a : 합을 구해야 하는 정수 n개가 저장되어 있는 리스트
        리턴값 : a에 포함되어 있는 정수 n개의 합(정수)

"""
def solve(a):
    sum = 0
    for i in a:
        sum += i
    return sum