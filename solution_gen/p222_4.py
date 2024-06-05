
import math

import numpy as np

from utils import calculate_volume, calculate_surface_area

pi = math.pi


def calculate_radii(volume: float, diameter: float) -> np.ndarray:
    return 20 * diameter / pi * math.sqrt(volume / 4 / pi)


def answer(diameter: float, tube_volume: float) -> float:
    volumes = calculate_volume(4, radius_1=diameter, radius_2=diameter * 2)
    surfaces = calculate_surface_area(radii=calculate_radii(
        tube_volume, diameter=diameter))
    return volumes[0] * volumes[1] / 2 + areas[0] * areas[1] / 2


if __name__ == '__main__':
    volume = math.pi * (diameter / 2) ** 2 * 3.8  # l
    diameter = 50  # in mm
    print(answer(diameter, volume))
