# https://open.kattis.com/problems/planina


another = start = 3
num = int(input())
if num == 1:
    print(9)
else:
    for _ in range(num - 1):
        another = another * 2 - 1

    print(another**2)


