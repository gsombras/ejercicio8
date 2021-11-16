#Import json
import persistencia_json as pj

#List creation

marca = list()
modelo = list()
combustible = list()
cilindrada = list()
while True:
    entrada = input("Marca (fin para terminar): ")
    dato1 = input("Modelo: ")
    dato2 = input("Combustible: ")
    dato3 = input("Cilindrada: ")
    if entrada != 'fin':
        marca.append(entrada)
        modelo.append(dato1)
        combustible.append(dato2)
        cilindrada.append(dato3)

#Write file

pj.store(lista.coches, "Coches.txt")

#Clear list

list.clear()



