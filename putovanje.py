# https://open.kattis.com/problems/putovanje

fruit_count, belly_max = map(int, input().split())
fruits = [int(x) for x in input().split()]

max_now = 0
max_possible = 0
start = 0

while True:
    count = 0
    max_now = 0
    for i in range(start, fruit_count):
        if max_now + fruits[i] <= belly_max:
            max_now += fruits[i]
            count += 1
    if count > max_possible:
        max_possible = count
    start += 1
    if start == fruit_count:
        break

print(max_possible)
