

import sympy
from scipy.misc import comb

print(sum(sympy.ntheory.factorint(comb(200000000000*150000000, 15000000000))[0]))

