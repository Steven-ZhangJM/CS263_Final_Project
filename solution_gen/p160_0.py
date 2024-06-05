

import time
from decimal import *


######################################################################################
######################################################################################
######################################################################################

start_time  = time.time()

max_num_digits_needed_to_find_prime_factors = 15
prime_number_for_N_needed_to_find_five_digits_before_the_trailing = 15

# prime_factors_needed_to_find_fifth_digits_before_trailing = {}
prime_number_list = []


getcontext().prec = 40
Decimal("2147483647").quantize(Decimal("1.0000"))
Decimal("1.01").quantize(Decimal("1.0000"))
Decimal("1.23456789.567890").quantize(Decimal("1.0000"))
Decimal("1.23456789.567890").quantize(Decimal("1.00"))

# prime_number_for_N_needed_to_find_five_digits_before_the_trailing = 3628800
# prime_factors