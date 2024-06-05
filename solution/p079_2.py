def find_shortest_passcode(file_name):
    max_length = 0
    possible_passcodes = set()
    
    with open(file_name, 'r') as f:
        for line in f:
            chars = line.strip().split()
            passcode = ''.join(chars)
            length = len(passcode)
            if length > max_length:
                max_length = length
                possible_passcodes = {passcode}
            else:
                possible_passcodes.add(passcode)

    shortest_passcode = None
    for i in range(max_length):
        for j in range(i+1, max_length):
            for k in range(j+1, max_length):
                for passcode in possible_passcodes:
                    if ''.join([passcode[i], passcode[j], passcode[k]]) == chars[1]:
                        if shortest_passcode is None or len(passcode) < len(shortest_passcode):
                            shortest_passcode = passcode
    return shortest_passcode

print(find_shortest_passcode('keylog.txt'))