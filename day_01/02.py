from itertools import combinations
from itertools import islice
N = 3
filepath = 'input1.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   sum_line = 0
   list_calories = []
   while line:
        if line.strip():
            print("Line {}: {}".format(cnt, line.strip()))
            sum_line += int(line.strip())
        else:
            print("Line {}: {}".format(cnt, "------empty------"))
            print("Suma {}: {}".format(sum_line, ""))
            list_calories.append(sum_line)
            sum_line = 0
        line = fp.readline()
        cnt += 1
list_calories.append(sum_line)

print(list_calories)
list_calories_sorted = sorted(list_calories, reverse=True)
print(list_calories_sorted)
print(sum(islice(sorted(list_calories_sorted, reverse=True), N)))
