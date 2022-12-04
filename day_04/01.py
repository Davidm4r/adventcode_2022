filepath = 'input.txt'
import re
with open(filepath) as fd:
    total_sum_priority = 0
    lines = fd.read().splitlines()
    total_points = 0
    count = 0
    for line in lines:
        assigments = re.findall(r'\d+', line)
        number1_first = int(assigments[0])
        number2_first = int(assigments[1])
        number1_second = int(assigments[2])
        number2_second = int(assigments[3])

        list_1 = [x for x in range(number1_first,number2_first+1)]
        list_2 = [x for x in range(number1_second, number2_second+1)]

        list1_contains_list2 = set(list_1).issubset(set(list_2))
        list2_contains_list1 = set(list_2).issubset(set(list_1))
        
        if list1_contains_list2:
            count+=1
        elif list2_contains_list1:
            count+=1
    print(count)