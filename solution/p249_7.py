def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_subsets_with_sum_is_prime(S):
    prime_count = {}
    for num in S:
        if not is_prime(num):
            continue
        for k in range(2, int(num**0.5) + 1):
            if num % k == 0:
                prime_count[k] = prime_count.get(k, 0) + 1
                break
    count = 0
    for i in range(len(S)):
        for j in range(i+1, len(S)+1):
            subset_sum = sum(S[i:j])
            if is_prime(subset_sum):
                count += 1
    return count

S = [2, 3, 5]
for num in range(7, 5000):
    if not is_prime(num):
        continue
    S.append(num)

print(count_subsets_with_sum_is_prime(S))

#