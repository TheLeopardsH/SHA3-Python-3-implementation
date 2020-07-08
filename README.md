Note:code is under development
# SHA3-Python-3-
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


# The F-Function Of SHA-3
The f-Function of SHA-3 Consists of 5 theta,rho,pi,chi and iota.
## Theta:
        Each of 1600 state bits are replaced by the XOR sum of 11 bits:
        (The original bit) XOR (5 bit column "to the left" of the bit) XOR  (5 bit column "to the right"  and one position "to the front" of the bit).
