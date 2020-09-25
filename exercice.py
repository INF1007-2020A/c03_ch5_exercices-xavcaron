#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
    nombre=(float(input('entrer un nombre: ')))
    if nombre<0:
        nombre=-1*nombre
    return nombre


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    liste=[]
    for l in prefixes:
        liste.append(l+suffixes)
    return liste


def prime_integer_summation() -> int:
    x=0
    y=7
    print()
    return 0


def factorial(number: int) -> int:
    fact=1
    if number != 0:
        for i in range(number):
            fact=fact*(number-i)
    return fact


def use_continue() -> None:
    nprime=range(1,11)
    for n in nprime:
        if n==5:
            continue
        print(n)



def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")

    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
