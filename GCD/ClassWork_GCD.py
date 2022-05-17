#
# Created on Tue May 10 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
def gcd(a,b):
    for i in range(min(a,b), -1, -1):
        if(a == 0 and b == 0):
            return None
        if(a == 0 or b == 0):
            return a + b
        if a%i==0 and b%i == 0:
            return i

def euclidGCD(a,b):
    if(a == 0 and b == 0):
        return None
    if(a == 0 or b == 0):
        return a + b
    else:
        return euclidGCD(max(a,b)%min(a,b), min(a,b))

#print(gcd(0,4))
#print(euclidGCD(12,37))
#print(euclidGCD(0,4))
print(euclidGCD(euclidGCD(2,3), 4))