#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class EuclideanAlgorithm:
    
#Encapsulation of the Euclidean algorithm for GCD calculation.

    def calculate_gcd(self, a, b):
        
#Calculate the GCD of two positive integers using the Euclidean algorithm（a is the first input integer,b is the second one)
       
        while b != 0:#the loop should be continue until b=0
            new_b = b#save the b so that it can be calculate again
            b = a % b#get a remainder
            a = new_b#let the a be the formal b
        return a#return to the GCD of a and b
a=186
b=296
answer=EuclideanAlgorithm()
gcd=answer.calculate_gcd(a, b)
print(f"The GCD of {a} and {b} is: {gcd}")