import re

def find_shortest_passcode(filename):
    with open(filename, 'r') as f:
        logins = [re.sub(r'\D+', '', line.strip()) for line in f.readlines()]

    passcodes = set()
    for login in logins:
        if len(login) > 3:
            passcodes.add(int(''.join(sorted(set(login[:3])))))

    return min(passcodes)

print(find_shortest_passcode('keylog.txt'))