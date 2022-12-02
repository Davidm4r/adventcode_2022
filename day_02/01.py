def transform(play):
    if play == 'A' or play == 'X':
        return 'rock'
    elif play == 'B' or play == 'Y':
        return 'paper'
    elif play == 'C' or play == 'Z':
        return 'scissors'


def select_winner(opponent, me):
    '''
    return the points
    6 victory
    3 draw
    0 lose
    '''
    if opponent == me:
        return 3
    elif opponent == 'rock' and me == 'scissors':
        return 0
    elif opponent == 'rock' and me == 'paper':
        return 6
    elif opponent == 'paper' and me == 'scissors':
        return 6
    elif opponent == 'paper' and me == 'rock':
        return 0
    elif opponent == 'scissors' and me == 'rock':
        return 6
    elif opponent == 'scissors' and me == 'paper':
        return 0

def select_points_by_element(element):
    if element == 'rock':
        return 1
    elif element == 'paper':
        return 2
    elif element == 'scissors':
        return 3

filepath = 'input.txt'
with open(filepath) as fd:
    lines = fd.read().splitlines()
    total_points = 0
    for line in lines:
        opponent_element = transform(line[0])
        me_element = transform(line[2])
        points_object = select_winner(opponent_element, me_element)
        points_match = select_points_by_element(me_element)
        total_points+=points_object+points_match

print(total_points)