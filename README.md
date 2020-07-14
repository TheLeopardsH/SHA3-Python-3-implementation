Note:code is under development
# SHA-3-Python
Python 3 code for SHA-3 cryptographic algorithm
This code has clean and easy to understand the implementation of SHA-3 Cryptographic Algorithm.Comments are done to make it easier to understand for someone who is new to SHA-3 and python.SHA-3 falls under sponge functions while sha-0,sha-1,sha-2 and MD-5 hash functions fall under Merkle Damgard construction.

Note:It's still under progress

![SHA-3 High Level Overview](https://github.com/TheLeopardsH/SHA3-Python-3-/blob/master/SHA3.png)

There are four levels of security in SHA-3 as follows

| Type        |  Output Length   |  Rate (r)     |    Capacity (c)   |
| ----------- |  --------------- | ------------- |  ---------------  | 
| SHA3-224    |       224        |    1152       |       448         |
| SHA3-256    |       256        |    1088       |       512         |
| SHA3-384    |       384        |     832       |       768         |
| SHA3-512    |       512        |     576       |      1024         |

Stage 1:
       Stage 1 is Padding stage
       
Stage 2:
       Stage 2 is State size
 
Stage 3:
       Stage 3 is Aborbing phase
       
Stage 4:
       Stage 4 is Squeezing phase

## Padding:
The input M to the hash algorithm SHA-3 is padded with 10∗1, i.e. two 1’s and as many 0’s in between (possibly none) until the padded length is a multiple of 1088 (= 1600−512)(Rate r Changes with SHA-3 type i.e SHA-256). You must append at least two 1’s, with as many 0’s in between (possibly none) so that the padded length is a multiple of 1088.


# The F-Function Of SHA-3
The f-Function of SHA-3 Consists of 5 sub-Functions which are theta,rho,pi,chi and iota.
In order to understand these 5 sub_functions,we divide the input 1600 bits state into 5x5 matrix and each one of the matrix has 64 bits(64 bit register=1 word) making it 5x5x64.

## Theta:
        Each of 1600 state bits are replaced by the XOR sum of 11 bits:
        (The original bit) XOR (5 bit column "to the left" of the bit) XOR  (5 bit column "to the right"  and one position "to the front" of the bit).
## rho:
     Each word is rotated by a fixed number of position by a fixed table.
     
## pi:
     We Permutate the 64 bit words locations in 5x5 matrix.
  
 
##  chi:
       
      A_out [i][j][k] = A[i][j][k] XOR ( (A[i + 1][j][k] XOR 1) AND (ain[i + 2][j][k]) )
    
## iota:
      Add constants  to word (0,0)
      
