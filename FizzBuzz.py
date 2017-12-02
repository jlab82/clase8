#!/usr/bin/env python
# coding: utf-8
num = int(raw_input("Bienvenidos a FizzBuzz. Por favor, seleccione un número del 1 al 100: "))
for i in range(num):
    if (i+1) % 3 == 0 and (i+1) % 5 == 0:
        print "fizzbuzz"
    elif (i+1) % 3 == 0:
        print "fizz"
    elif (i+1) % 5 == 0:
        print "buzz"
    else:
        print i+1
