a_n_values = [2, 512]
for i in range(10, 30):
    prev_value = a_n_values[i - 1]
    power_sum = calculate_power_sum(prev_value)
    a_n_values.append(power_sum)

print(a_n_values[29])