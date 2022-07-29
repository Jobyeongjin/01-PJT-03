import sys

sys.stdin = open("_문자열의거울상.txt")

t = int(input())

for tc in range(1, t + 1):
    alpha = list(input())

    arr = ''
    reverse_ = alpha[::-1]

    for i in reverse_:
        if i == 'b':
            arr += 'd'
        elif i == 'd':
            arr += 'b'
        elif i == 'p':
            arr += 'q'
        else:
            arr += 'p'

    print(f'#{tc} {arr}')
