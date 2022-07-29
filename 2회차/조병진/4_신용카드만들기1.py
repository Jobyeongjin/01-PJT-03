import sys

sys.stdin = open("_신용카드만들기1.txt")

t = int(input())

for tc in range(1, t + 1):
    card = list(input().split())

    odd = []
    even = []
    for i in range(len(card)):
        if i % 2 == 0:
            odd += card[i]
        else:
            even += card[i]

    odd_sum = 0
    for i in odd:
        odd_sum += int(i) * 2

    even_sum = 0
    for i in even:
        even_sum += int(i)

    total = odd_sum + even_sum
    for i in range(10):
        if (total + i) % 10 == 0:
            print(f'#{tc} {i}')
