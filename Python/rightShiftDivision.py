import math

"""
The right shift operation '>>' is similar to floor division by powers of two
x >> y = floor(x / 2^y)
"""

rightShiftDivision = 80 >> 3  # floor(80 / 2^3 ) = floor(80 / 8) = 10
controllDivision = math.floor(80 / 8)  # floor(80 / 8) = 10
print(f"{rightShiftDivision} == {controllDivision}")
