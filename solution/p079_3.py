def find_shortest_passcode():
    keylog = open('keylog.txt', 'r').read().splitlines()
    
    possible_passcodes = set()
    
    for i in range(len(keylog[0])):
        passcode = ''
        for line in keylog:
            if len(line) > i:
                passcode += str(int(line[i]))
        possible_passcodes.add(passcode)
        
    return min(possible_passcodes, key=len)

print(find_shortest_passcode())
#