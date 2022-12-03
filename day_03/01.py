filepath = 'input.txt'


minus = {chr(i+96):i for i in range(1,27)}
mayus = {chr(i+64):i+26 for i in range(1,27)}
list_letters_priorities_values = dict(minus)
list_letters_priorities_values.update(mayus)

with open(filepath) as fd:
    total_sum_priority = 0
    lines = fd.read().splitlines()
    total_points = 0
    for line in lines:
        len_line= len(line)
        first_compartiment = line[0:int(len_line/2)]
        second_compartiment = line[int(len_line/2)::]
        
        res = ''.join(sorted(set(first_compartiment) & set(second_compartiment), key = first_compartiment.index))
        priority = list_letters_priorities_values[res]
        total_sum_priority+=priority

print(total_sum_priority)