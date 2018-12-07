# codeforces.com/contest/158/problem/B

n = input()
ch = input().split()
ch = [int(x) for x in ch]
sums = 0
sums += ch.count(4)
sums += int(ch.count(2)/2)
two = False
if (ch.count(2)/2).is_integer() == False:
    two = True
if ch.count(3) < ch.count(1):
    sums += ch.count(3)
    ones = ch.count(1) - ch.count(3)
    if (ones/4).is_integer():
        sums += ones/4
    else:
        if ones >= 2 and two == True:
            two = False
            sums += 1
            ones -= 2
            if ones > 0:
                if (ones / 4).is_integer():
                    sums += ones / 4
                else:
                    sums = sums + int(ones / 4) + 1
        elif ones >= 2:
            sums = sums + int(ones / 4) + 1
        elif ones < 2 and two == True:
            two = False
            sums += 1
        elif ones < 2:
            sums += 1
elif ch.count(3) >= ch.count(1):
    sums += ch.count(3)
if two == True:
    sums += 1
print(int(sums))
