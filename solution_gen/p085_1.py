

from math import sqrt


def main():
    max_width = 500000
    max_height = 500000
    max_width = int(max_width / (sqrt(2) + 1))

    width = max_width
    height = int(width / sqrt(2) + 0.01)
    while width * height > max_width*max_height:
        width -= 1
        height = int(width / sqrt(2) + 0.01)


    return width*height


print(main())
