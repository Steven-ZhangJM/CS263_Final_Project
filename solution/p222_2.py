def pipe_length(radius):
    total_radius = sum(range(31, 51))
    return (2 * total_radius + 1) / (2 * radius)

length_mm = int(pipe_length(0.05) * 1000000)

print(length_mm)

#