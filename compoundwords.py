# https://open.kattis.com/problems/compoundwords

import sys

words = []
for line in sys.stdin:
    words += line.split()

answers = set()

for i in range(len(words)):
    for j in range(i + 1, len(words)):
        first_word = words[i] + words[j]
        second_word = words[j] + words[i]

        answers.add(first_word)
        answers.add(second_word)

answers = sorted(answers)

for word in answers:
    print(word)
