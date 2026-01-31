import random as rand
from math import sin

rand.randint(1, 6)
print(rand.randint(1, 6))
# that "." is an ACCESS CARD to RAND in this code
# meaning it will look in RAND for RANDINT and then use that method for us

sine = sin(1)
print(sine)

cosine = math.cos(2)
# math.cos doesn't exist because we DIDN'T import MATH but ONLY MATH.SIN
# the same can be said for the OTHER functions of MATH
#         so math.pi, math.e, and etc DON'T exist
print(cosine)
