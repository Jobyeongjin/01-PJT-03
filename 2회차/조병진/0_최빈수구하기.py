import sys

sys.stdin = open("_최빈수구하기.txt")

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    score = list(map(int, input().split()))

    arr = [0] * 101
    for i in score:
        arr[i] += 1

    result = []
    max_ = max(arr)
    for i in range(len(arr)):
        if arr[i] == max_:
            result.append(i)

    print(f'#{tc} {max(result)}')
