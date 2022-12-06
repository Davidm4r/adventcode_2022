filepath = 'input.txt'

with open(filepath) as fd:
    total_sum_priority = 0
    line = fd.read().splitlines()[0]
    print(line)
    for x in range(len(line)-3):
        packet = line[x:x+4]
        print(f"Packet: {packet}")
        has_repeated_chars = len(set(packet)) != len(packet)
        if not has_repeated_chars:
            print(f"Position {x+4}")
            break
