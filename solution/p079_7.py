*
```python
def find_shortest_passcode(keylog_file):
    # Open the keylog file and read it line by line
    with open(keylog_file, 'r') as f:
        keylogs = [line.strip() for line in f.readlines()]

    # Initialize an empty set to store all possible characters
    chars = set()

    # Iterate over each keylog
    for keylog in keylogs:
        # Extract the three characters from the keylog
        chars.update(keylog[1:4])

    # Find the length of the shortest passcode by counting the unique characters
    passcode_length = len(chars)

    return passcode_length

# Call the function with the keylog file
shortest_passcode = find_shortest_passcode('keylog.txt')
print(shortest_passcode)
```
**