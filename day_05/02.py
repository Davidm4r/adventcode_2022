def generate_list_crates(lines):
    crates_dict = {}
    for line in lines:
        splited_line = ([line[i:i+n] for i in range(0, len(line), n) if not 'move' in line])
        for index, element in enumerate(splited_line):
            try:
                crates_dict[index+1]
            except:
                crates_dict[index+1] = []
            check_if_create = re.search(regex, element)
            if check_if_create:
                #print(element,index+1)
                crates_dict[index+1].append(check_if_create.group(1))
    reversed_crates = {key: values[::-1] for key, values in crates_dict.items()}

    return reversed_crates

def do_moves(lines, crates):
    regex = r'(move)\s(\d+)\sfrom\s(\d)\sto\s(\d)'
    for line in lines:
        matcher = re.compile(regex, flags=re.IGNORECASE)
        matchValue = matcher.match(line)
        if matchValue:
            
            crates_moving = crates[int(matchValue.group(3))][-int(matchValue.group(2)):]
            crates[int(matchValue.group(3))] = crates[int(matchValue.group(3))][:-int(matchValue.group(2))]
            print("crates moving", crates_moving)
            crates[int(matchValue.group(4))].extend(crates_moving)
            print("Action : ", matchValue.group(1))
            print("Number of crates : ", matchValue.group(2))
            print("From : ", matchValue.group(3))
            print("To : ", matchValue.group(4))
    return crates



filepath = 'input2.txt'
import re
with open(filepath) as fd:
    total_sum_priority = 0
    lines = fd.read().splitlines()
    regex = r"\[([A-Z])\]"
    n = 4
    
    crates_dict = generate_list_crates(lines)
    print(crates_dict)
    crates_moved = (do_moves(lines, crates_dict))
    print(crates_moved)
    for k, v in crates_moved.items():
        print(v[-1], end = '')
