import sys

sys.stdin = open("_소득불균형.txt")

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    money = list(map(int, input().split()))

    mean = sum(money) / n

    cnt = 0
    for i in money:
        if i <= mean:
            cnt += 1

    print(f'#{tc} {cnt}')
