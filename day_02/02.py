def transform(play):
    if play == 'A':
        return 'rock'
    elif play == 'B':
        return 'paper'
    elif play == 'C':
        return 'scissors'


def select_points_by_element(opponent, final_result):
    '''
    return the points
    x losw
    y draw
    z win

    1 rock
    2 paper
    3 scissors
    '''
    if opponent == 'rock' and final_result == 'Z': #paper
        return 2
    elif opponent == 'rock' and final_result == 'Y': #rock
        return 1
    elif opponent == 'rock' and final_result == 'X': #scissors
        return 3

    elif opponent == 'paper' and final_result == 'Z': #scissors
        return 3
    elif opponent == 'paper' and final_result == 'Y': #paper
        return 2
    elif opponent == 'paper' and final_result == 'X': #rock
        return 1


    elif opponent == 'scissors' and final_result == 'Z': #rock
        return 1
    elif opponent == 'scissors' and final_result == 'Y': #scissors
        return 3
    elif opponent == 'scissors' and final_result == 'X': #paper
        return 2

def select_winner(me):
    if me == 'X':
        return 0
    elif me == 'Y':
        return 3
    elif me == 'Z':
        return 6

filepath = 'input2.txt'
with open(filepath) as fd:
    lines = fd.read().splitlines()
    total_points = 0
    for line in lines:
        opponent_element = transform(line[0])
        points_object = select_points_by_element(opponent_element, line[2])
        points_match = select_winner(line[2])
        total_points+=points_object+points_match
        print(total_points)
        print(opponent_element)
        print(line[2])
        print(f"Points object: {points_object}")
        print(f"Points match: {points_match}")
        print("\n")

print(total_points)