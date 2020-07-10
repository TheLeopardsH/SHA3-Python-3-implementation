
#python3 code for sha3 cryptographic algorithm
import numpy as np
import random
l = 6  # value of l = {0, 1, 2, 3, 4, 5, 6}
b = 25*(2**l)  # b = state size (value of b = {25, 50, 100, 200, 400, 800, 1600} )
# For SHA-3 the value of ‘l’ was 6 and the
# so rounds turn out to be
rounds = 12 + 2*l  # 24 rounds
print(rounds+' Rounds in SHA-3')
# So SHA-3 has state size of 1600 bits and the number of rounds of computations will be 24


# 1600 bits(1 dimensional array) to 3 dimensional array of 5x5x64
def _1Dto3D(A):
    A_out = np.zeros((5, 5, 64), dtype = int) # Initialize empty 5x5x64 array
    for i in range(5):
        for j in range(5):
            for k in range(64):
                A_out[i][j][k] = A[64*(5*j + i) + k]
    return A_out


def theta(A):
        A_out = np.zeros((5,5,64), dtype = int)  # Initialize empty 5x5x64 array
       #A_out = [[[0 for _ in range(64)] for _ in range(5)] for _ in range(5)] #without numpy
        for i in range(5):
                for j in range(5):
                        for k in range(64):
                            C=sum([A[i-1][ji][k] for ji in range(5)]) % 2 # XOR=mod2 5 bit column "to the left" of the original bit
                            D=sum([A[((i+1) % 5)][ji][k-1] for ji in range(5)]) % 2 #XOR=mod2 5 bit column "to the right"  and one position "to the front" of the original bit
                            temp=C+D+A[i][j][k] % 2 #XORing original bit with A and B
                            A_out[i][j][k]=temp
        return A_out

#Rho : Each word is rotated by a fixed number of position according to table.
def rho(A):
    rhomatrix=[[0,36,3,41,18],[1,44,10,45,2],[62,6,43,15,61],[28,55,25,21,56],[27,20,39,8,14]]
    rhom = np.array(rhomatrix, dtype=int)  # Initialize empty 5x5x64 array
    A_out = np.zeros((5,5,64), dtype = int)
    for i in range(5):
        for j in range(5):
            for k in range(64):
                A_out[i][j][k] = A[i][j][k - rhom[i][j]] #  A[i][j][k − (t + 1)(t + 2)/2] so here rhom[i][j] Use lookup table to "calculate" (t + 1)(t + 2)/2
    return A_out

#Pi: Permutate the 64 bit words
def pi(A):
    A_out = np.zeros((5,5,64), dtype = int) # Initialize empty 5x5x64 array
    for i in range(5):
        for j in range(5):
            for k in range(64):
                A_out[j][(2*i+3*j)%5][k] = A[i][j][k]
    return A_out

# A_out [i][j][k] = A[i][j][k] XOR ( (A[i + 1][j][k] XOR 1) AND (ain[i + 2][j][k]) )
def chi(A):
    A_out = np.zeros((5,5,64), dtype = int) # Initialize empty 5x5x64 array
    for i in range(5):
        for j in range(5):
            for k in range(64):
                A_out = (A[i][j][k]+(((A[(i + 1)%5][j][k] + 1 )% 2) * (A[(i + 2)%5][j][k]))) % 2
    return A_out

#iota: add constants  to word (0,0)
# aout[i][j][k] = ain[i][j][k] ⊕ bit[i][j][k]
# for 0 ≤ ℓ ≤ 6, we have bit[0][0][2ℓ − 1] = rc[ℓ + 7ir]
def iota(A, round):
    # Initialize empty arrays
    A_out = A.copy()
    bit = np.zeros((5,5,64), dtype=int)
    rc = np.zeros((168), dtype=int)

    #generation of rc as Linear Feedback Shift Register
    w = np.array([1,0,0,0,0,0,0,0], dtype = int)
    rc[0] = w[0]
    for i in range(1, 168): #7*24
        w = [w[1],w[2],w[3],w[4],w[5],w[6],w[7], (w[0]+w[4]+w[5]+w[6]) % 2]
        rc[i] = w[0]

    # Calculate A_out
    for l in range(7):
        A_out[0][0][2**l - 1] = (A[0][0][2**l - 1] + rc[l + 7*round])% 2

# 5x5x64 (three-dimensional array) into 1600 bits(one-dimensional array)
def _3Dto1D(A):
    A_out = np.zeros(1600, dtype = int) # Initialize empty array of size 1600
    for i in range(5):
        for j in range(5):
            for k in range(64):
                A_out[64*(5*j+i)+k] = A[i][j][k]
    return A_out

# 24 X (ι ◦ χ ◦ π ◦ ρ ◦ θ)
def SHA3(SHA_in):
    length=len(SHA_in)
    A_3D = _1Dto3D(SHA_in)
    for r in range(24):
        SHA_out_3D = iota(chi(pi(rho(theta(A_3D)))), r)
    SHA_out = _3Dto1D(SHA_out_3D)
    return SHA_out

