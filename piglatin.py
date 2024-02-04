# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:15:09 2020

@author: Fernando Paipilla
"""

def traducir_a_pig_latin(texto: str)->str:
    vocales = ["a", "e", "i", "o", "u"]
    lista = texto.split()
    final = ""
    for i in lista:
        if i[0] in vocales:
            i += "way"
        else:
            x = 1
            while x < len(i):
                if i[x] in vocales:
                    i = i[x:] + i[:x] + "ay"
                    break
                x += 1
        if final != "":
            final += " " + i
        else:
            final += i
    return final

def ejecutar()->None:
    x = input("p: ")
    rta = traducir_a_pig_latin(x)
    print(rta)

ejecutar()