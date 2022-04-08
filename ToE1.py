# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 22:50:31 2020

@author: subbu
"""
from numpy import sqrt,arccos,cos,pi

def dot(a,b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2] 

'''s11 = input('Enter sigmaxx : ')
s12 = input('Enter sigmayx : ')
s13 = input('Enter sigmazx : ')
s21 = input('Enter sigmaxy : ')
s22 = input('Enter sigmayy : ')
s23 = input('Enter sigmazy : ')
s31 = input('Enter sigmaxz : ')
s32 = input('Enter sigmayz : ')
s33 = input('Enter sigmazz : ')'''

s11 = 2
s12 = 0 
s13 = 0
s21 = 0
s22 = 3
s23 = 4
s31 = 0
s32 = 4
s33 = -3


I1 =  s11 + s22 + s33
I2 = s11*s22 + s22*s33 + s33*s11 - s21*s12 -s31*s13 - s23*s32
I3 = (s11*(s22*s33 - s23*s32)-s12*(s21*s33 - s31*s23)+ s13*(s21*s32 - s22*s31))

Q = (3*I2 - I1**2)/9
R = (2*I1**3 - 9*I1*I2 +27*I3)/54

theta = arccos(R/sqrt(-Q**3))

r1 = 2*sqrt(-Q)*cos(theta/3) + I1/3
r2 = 2*sqrt(-Q)*cos((theta + 2*pi)/3) + I1/3
r3 = 2*sqrt(-Q)*cos((theta + 4*pi)/3) + I1/3

r = [r1,r2,r3]
eigen_vec = [] 

for i in range(0,len(r)):
    if abs(r[i] - s11) < 0.00001:
        l1 = 1
        m1 = 0
        n1 = 0
    elif abs(r[i] - s22) < 0.00001:
        l1 = 0
        m1 = 1
        n1 = 0
    elif abs(r[i] - s33 ) < 0.00001:
        l1 = 0
        m1 = 0
        n1 = 1
    else:
        a1 = s11-r[i]
        a2 = s12
        a3 = s13
        b1 = s21
        b2 = s22-r[i]
        b3 = s23
        if a2 == 0 and a3 == 0:
            l1s = 0
            m1s = b2
            n1s = b3
        else:
            l1s = 1
            m1s = (a1*b3 - a3*b1)/(b2*a3 - a2*b3)
            n1s = (a1*b2 - a2*b1)/(a2*b3 - b2*a3)
        
        mag = sqrt(l1s**2 + m1s**2 + n1s**2)
        l1 = l1s/mag
        m1 = m1s/mag
        n1 = n1s/mag
        
    e1 = [l1,m1,n1]
    eigen_vec.append(e1)
  
E1 = eigen_vec[0]
E2 = eigen_vec[1]
E3 = eigen_vec[2]

dot_prod1 = dot(E1,E2)
dot_prod2 = dot(E2,E3)
dot_prod3 = dot(E3,E1)

print(dot_prod1)
print(dot_prod2)
print(dot_prod3)


    
    

