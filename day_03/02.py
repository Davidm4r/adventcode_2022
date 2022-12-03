filepath = 'input2.txt'


minus = {chr(i+96):i for i in range(1,27)}
mayus = {chr(i+64):i+26 for i in range(1,27)}
list_letters_priorities_values = dict(minus)
list_letters_priorities_values.update(mayus)

with open(filepath) as fd:
    total_sum_priority = 0
    lines = fd.read().splitlines()
    total_points = 0
    elf_counter = 0
    racksacks_elf = []
    for line in lines:
        racksacks_elf.append(line)
        elf_counter+=1
        if elf_counter == 3:
            common_letter = {c for c in racksacks_elf[0] if all(c in s for s in racksacks_elf[1:])}
            letter_to_string = ''.join(common_letter)
            priority = list_letters_priorities_values[letter_to_string]
            total_sum_priority+=priority
            racksacks_elf=[]
            elf_counter=0
       
print(total_sum_priority)