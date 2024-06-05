from collections import defaultdict

# Function to read the file and return the contents
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

# Function to deduce the passcode
def deduce_passcode(attempts):
    # Create a dictionary to hold the order of digits
    order = defaultdict(set)
    for attempt in attempts:
        order[attempt[0]].update(attempt[1:])
        order[attempt[1]].add(attempt[2])

    # Create a list to hold the sorted passcode
    passcode = []
    while order:
        # Find the digit that precedes no other digits
        for digit, after in order.items():
            if not any(digit in after_set for after_set in order.values() if after_set != after):
                passcode.append(digit)
                # Remove the digit from the order dictionary
                order.pop(digit)
                # Remove the digit from all other sets
                for after_set in order.values():
                    after_set.discard(digit)
                break

    return ''.join(passcode)

# Main execution
if __name__ == "__main__":
    login_attempts = read_file('keylog.txt')
    print(deduce_passcode(login_attempts))