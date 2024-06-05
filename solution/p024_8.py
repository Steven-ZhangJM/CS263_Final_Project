*
```
def permutation_order(digits):
    def permute(i, last):
        if i == len(digits) - 1:
            return [int(''.join(map(str, digits))), 0]
        results = []
        for j in range(i, len(digits)):
            if j != last and digits[j] < digits[last]:
                digits[i], digits[j] = digits[j], digits[i]
                result = permute(i + 1, j)
                if result[0] > result[1]:
                    results.append(result)
                digits[i], digits[j] = digits[j], digits[i]
        return results

    results = permutation_order(0, -1)
    millionth_permutation = sorted([result[0] for result in results])[999999]

    return int(millionth_permutation)

print(permutation_order(range(10)))
```
**