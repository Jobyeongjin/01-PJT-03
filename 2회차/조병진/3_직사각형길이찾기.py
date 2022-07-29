import sys

sys.stdin = open("_직사각형길이찾기.txt")

t = int(input())

for tc in range(1, t + 1):
    num = list(map(int, input().split()))

    if num[0] == num[1]:
        print(f'#{tc} {num[2]}')
    elif num[0] != num[1] and num[0] != num[2]:
        print(f'#{tc} {num[0]}')
    else:
        print(f'#{tc} {num[1]}')
