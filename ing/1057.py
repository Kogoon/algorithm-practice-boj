# 2020.03.22
"""
문제: 김지민은 N명이 참가하는 스타 토너먼트에 진출했다. 토너먼트는 다음과 같이 진행된다. 일단 N명의 참가자는 번호가 1번부터 N번까지 배정받는다
    일단 김지민과 임한수는 서로 대결하기 전까지 항상 이긴다고 가정한다. 1 라운드에서 김지민의 번호와 임한수의 번호가 주어질 때, 
    과연 김지민과 임한수가 몇 라운드에서 대결하는지 출력하는 프로그램을 작성하시오.
입력: 셋째 줄에 참가자의 수 N과 1라운드에서 김지민의 번호와 임한수의 번호가 순서대로 주어진다.
    N은 100,000보다 작거나 같은 자연수이고, 김지민의 번호와 임한수의 번호는 N보다 작거나 같은 자연수이고, 서로 다르다.
출력: 첫째 줄에 김지민과 임한수가 대결하는 라운드 번호를 출력한다. 만약 서로 대결하지 않을 때는 -1을 출력한다.
"""
import sys
input = sys.stdin.readline

N, A, B = map(int, input().split())
print(N, A, B)