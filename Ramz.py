# quera.ir/problemset/contest/17902/%D8%B3%D8%A4%D8%A7%D9%84-%D8%B1%D9%85%D8%B2

k = int(input())
a = list(input())
c = 0
li = []

for _ in range(k):
    li.append(list((input())))
i = 0
for ch in a:
    x = int(li[i].index(ch))
    i += 1
    if x <= 4:
        c += x
    else:
        c += 9 - x

print(c)
