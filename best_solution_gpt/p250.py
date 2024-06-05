MOD = 10**16

def power_mod(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result

def count_subsets(divisor, max_exponent):
    count = [1] + [0] * divisor
    for i in range(1, max_exponent + 1):
        next_count = count[:]
        addend = power_mod(i, i, divisor)
        for j in range(divisor):
            next_count[(j + addend) % divisor] += count[j]
            next_count[(j + addend) % divisor] %= MOD
        count = next_count
    return (count[0] - 1) % MOD

print(count_subsets(250, 250250))