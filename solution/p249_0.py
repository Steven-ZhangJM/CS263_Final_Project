S = [i for i in range(2, 5000) if is_prime(i)]
print(int(str(count_prime_sum_subsets(S))[-16:]))