# https://open.kattis.com/problems/greedilyincreasing

n = int(input())
line = [int(x) for x in input().split()]
answer = []

i = 1
for i in range(n):
    if i is 0:
        answer.append(str(line[0]))
    if line[i] > int(answer[-1]):
        answer.append(str(line[i]))

print(len(answer))
print(" ".join(answer))
