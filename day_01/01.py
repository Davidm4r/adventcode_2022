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

print(max(list_calories))