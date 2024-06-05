import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

S = [i for i in range(2, 5000) if is_prime(i)]

count = 0

for i in range(len(S)):
    for j in range(i + 1, len(S)):
        total = S[i] + S[j]
        while total < 5000:
            if is_prime(total):
                count += 1
            total += S[j]
            j -= 1
            while j >= i and not is_prime(S[j]):
                j -= 1

print(str(count).zfill(16))