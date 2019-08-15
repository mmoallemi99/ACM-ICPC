# https://open.kattis.com/problems/goldbach2


def is_prime(n):
    if n == 2:
        return True
    if n & 1 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 2
    return True


number_of_lines = int(input())

for _ in range(number_of_lines):
    answers = []
    num = int(input())
    for i in range(2, int(num / 2) + 1):
        if is_prime(i) and is_prime(num - i):
            ans = "".join([str(i), "+", str(num - i)])
            answers.append(ans)

    print("{num} has {count} representation(s)".format(num=num, count=len(answers)))
    for item in answers:
        print(item)
    print()
