# https://open.kattis.com/problems/mia


def game(dices_line):
    one = int(dices_line[0] + dices_line[1])
    two = int(dices_line[1] + dices_line[0])
    if one > two:
        first_player = one
    else:
        first_player = two

    one = int(dices_line[2] + dices_line[3])
    two = int(dices_line[3] + dices_line[2])
    if one > two:
        second_player = one
    else:
        second_player = two

    if (first_player == 21) and (second_player != 21):
        print("Player 1 wins.")
    elif (first_player != 21) and (second_player == 21):
        print("Player 2 wins.")
    elif (first_player == 21) and (second_player == 21):
        print("Tie.")
    elif (first_player % 11 == 0) and (second_player % 11 == 0):
        first = first_player / 11
        second = second_player / 11
        if first > second:
            print("Player 1 wins.")
        elif second > first:
            print("Player 2 wins.")
        else:
            print("Tie.")
    elif first_player % 11 == 0:
        print("Player 1 wins.")
    elif second_player % 11 == 0:
        print("Player 2 wins.")
    elif first_player > second_player:
        print("Player 1 wins.")
    elif first_player < second_player:
        print("Player 2 wins.")
    else:
        print("Tie.")


while True:
    line = input().split()
    if line[0] is not '0':
        game(line)
    else:
        break
