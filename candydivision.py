def prime_factors(n):
    temp = 2
    prime_factors_list = []
    while n > 1:
        if n % temp == 0:
            prime_factors_list.append(temp)
            n = n / temp
            temp -= 1
        temp += 1
    return prime_factors_list


number = int(input())
primes = prime_factors(number)

# answer = {0, number - 1}
answer = {1, number}
for num in primes:
    answer.add(num)

i, j = 0, 0
for i in range(0, len(primes)):
    for j in range(i+1, len(primes)):
        result = primes[i] * primes[j]
        answer.add(result)
for i in range(0, len(primes)):
    result = int(number / primes[i])
    answer.add(result)

final = sorted(answer)
for item in final:
    print(item, end=" ")


