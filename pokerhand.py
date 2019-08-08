# https://open.kattis.com/problems/pokerhand

hand = input().split()
scores_list = {}
for card in hand:
    rank = card[0]
    
    if rank in scores_list.keys():
        scores_list[rank] += 1
    else:
        scores_list[rank] = 1

print(max(scores_list.values()))
