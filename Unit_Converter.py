#!/usr/bin/env python
# coding: utf-8
print "Bienvenido/a. Esta aplicación es una calculadora conversora de kilómetros a millas"
yes = True
while yes:
    km = float(raw_input("Por favor, introduzca número de kilómetros: "))
    milla = km * 0.6214
    print str(km) + " kilómetros corresponden a " + str(milla) + " millas"
    respuesta = str.lower(raw_input("¿Quiere realizar otra coversión? si/no: "))
    if respuesta == "no":
        yes = False
    elif respuesta =="si":
        yes = True
    else:
        print "Respuesta no válida"
        break
print "Muchas gracias por utilizar esta aplicación. FIN"

