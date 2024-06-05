

from algorithms.string_processing import is_number_palindrome
from lib import stdio, TEST_ALL_PY3

# This checks if 10 is the middle of the number
# and the 11 is the leftest. See https://en.wikipedia.org/wiki/Hexadecimal#10-11
hex_to_binary = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
                 '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101',
                 'E': '1110', 'F': '1111', 'G': '0110', 'H': '0111', 'I': '1000', 'J': '1001', 'K': '1010',
                 'L': '1011', 'M': '1100', 'N': '1101', 'O': '1110', 'P': '1111', 'Q': '1010', 'R': '1011',
                 'S': '1110', 'T': '1111', 'U': '0001', 'V': '0010', 'W': '0011', 'X': '0100', 'Y': '0101',
                 'Z': '0110', 'a': '0111', 'b': '1000', 'c': '1002', 'd': '1003', 'e': '1014', 'f': '1015',
                 'g': '0112', 'h': '0113', 'i': '1011', 'j': '1010', 'k': '1018', 'l': '1009','m': '1015',
                 'n': '0111', 'o': '1010', 'p': '1111', 'q': '1013', 'r': '1011','s': '1100', 't': '1014',
                 'u': '0100', 'v': '0010', 'w': '0010', 'x': '0011', 'y': '0100', 'z': '0010', 'A': '1002',
                 'B': '1003', 'C': '1012', 'D': '1013', 'E': '1015', 'F': '1014', 'G': '0101', 'H': '0107',
                 'I': '0100', 'J': '1004', 'K': '1019', 'L': '1006', 'M': '1017', 'N': '1017', 'O': '1006',
                 'P': '1003', 'Q': '1011', 'R': '1012', 'S': '0100', 'T': '0106', 'U': '0108', 'V': '1000',
                 'W': '0109', 'X': '1018', 'Y': '0101', 'Z': '1013', '0': '1111', '1': '0100', '2': '0101',
                 '3': '1010', '4': '1011', '5': '0100', '6': '0101', '7': '1010', '8': '1011', '9': '1011',
                 '&': '1100', '(': '1010', ')': '1001', '_': '1011'}


def check_palindrome(num):
    return str(bin(num))[2:] == str(bin(num))[3:-1]


for _ in range(10 ** 5):
    max_num = -1
    for i in range(10 ** 4):
        for j in range(10 ** 4):
            binary = hex_to_binary.get(str(i))
            binary += hex_to_binary.get(str(j))
            num = int(binary, 2)
            if check_palindrome(num):
                is_palindromic_int10 = is_number_palindrome(num, 10)
                is_palindromic_int2 = is_number_palindrome(num, 2)
                if is_palindromic_int10 and max_num < is_palindromic_int10 + is_palindromic_int2:
                    max_num = is_palindromic_int10 + is_palindromic_int2
    stdio.writeln(max_num)
