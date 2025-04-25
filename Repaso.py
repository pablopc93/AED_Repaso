""""
Repaso de Python
Listas
"""

lista1 = [1, 2.0,True, 4, 5,['A', 'B', 'C', 'D']]

lista2 = []
lista2.extend(lista1[3:5]) # Extiende lista2 con los elementos de lista1 desde el índice 3 hasta el 5 (sin incluir el 5)
print("Lista2 de enteros: ", lista2)

lista3 = list (lista2) # Crea una copia de lista2 en lista3
lista3.append(lista1[5]) # Añade a lista3 el elemento en la posición 5 de lista1
print("Apend de lista1 ", lista3)
lista3.extend(lista1)
print("Lista3 extendida: ", lista3)

lista4 = [i for i in range(10)]
print("Lista4 (valores del 0-9): ", lista4)

lista5 = sorted (lista4,reverse=True) # Ordena lista4 de forma descendente, sorted no modifica la lista original
print("Lista5 (valores del 9-0): ", lista5)
lista5.sort() # Ordena lista5 de forma ascendente, sort modifica la lista original
print("Lista5 (valores del 0-9): ", lista5)

lista6 = list(reversed(lista5)) # Crea una lista con los elementos de lista5 en orden inverso, reversed no modifica la lista original
print("Lista6 (valores del 9-0): ", lista6)

print("lista6(-1): ",lista6[-1::-1]) # Imprime el último elemento de lista6

#palindromo
diccionario = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
print("claves: ",diccionario.keys())
print("valores: ",diccionario.values())

print(diccionario.get('á')) # Devuelve el valor de la clave 'á'
print(diccionario['í']) # Devuelve el valor de la clave 'í'

for k,v in diccionario.items(): # obtener key desde el value
    if v == 'i':
        print("La clave de i es: ", k)


def esPalindromo(palindromo):
    palindromo_sinEspacio = palindromo.replace(" ", "").lower()
    palindromo_sintildes = ""
    for c in palindromo_sinEspacio:
        palindromo_sintildes += diccionario.get(c,c)
    
    return palindromo_sintildes == palindromo_sintildes[::-1]
    
palindromo = "Anita lava la tiná"

print(palindromo, esPalindromo(palindromo)) 