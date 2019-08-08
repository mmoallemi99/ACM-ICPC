# https://open.kattis.com/problems/nodup

words = sorted(input().split())
repeat = False
count = len(words)

i, j = 0, 0

for i in range(count):
    for j in range(i+1, count):
        if words[i] == words[j]:
            repeat = True
        j += 1

    i += 1

if repeat:
    print('no')
else:
    print('yes')
