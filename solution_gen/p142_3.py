


def solution(x):
    result = []
    for y in range(1, x+1):
        for z in range(y, x+1):
            if x+y + z >= x - y and x + z - y >= x - z and x + y + z <= x - y and x + z - y <= x - z and y + z - x >= y - z and y + z - x <= y -z:
                result.append([x, y, z])
    return result

print(solution(6))
print(solution(25))