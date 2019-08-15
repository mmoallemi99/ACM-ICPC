# https://open.kattis.com/problems/birds

length, distance, current_birds = map(int, input().split())
bird_positions = set()

for _ in range(current_birds):
    bird = int(input())
    bird_positions.add(bird)

bird_positions = sorted(bird_positions)
start = 6
end = length - 6
possible = 0
if bird_positions:
    # start till first list member
    current_position_to_next_bird = bird_positions[0] - start
    possible += int(current_position_to_next_bird / distance)
    start = bird_positions[0]

    # members of the list
    for position in bird_positions:
        current_position_to_next_bird = position - start
        if current_position_to_next_bird:
            possible += int(current_position_to_next_bird / distance) - 1
        start = position

    # last member of the list till the end
    current_position_to_next_bird = end - bird_positions[-1]
    possible += int(current_position_to_next_bird / distance)
else:
    # if no birds are already on the wire
    possible = int((end - start) / distance) + 1

print(possible)
