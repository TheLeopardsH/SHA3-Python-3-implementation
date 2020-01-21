
#python3 code for sha3 cryptographic algorithm
import random
l = 6  # value of l = {0, 1, 2, 3, 4, 5, 6}
b = 25*(2**l)  # b = state size (value of b = {25, 50, 100, 200, 400, 800, 1600} )
# For SHA-3 the value of ‘l’ was 6 and the
# so rounds turn out to be
rounds = 12 + 2*l  # 24 rounds
print(rounds+' Rounds in SHA-3')
# So SHA-3 has state size of 1600 bits and the number of rounds of computations will be 24