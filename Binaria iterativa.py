def binary_search(lista, Val, inicio, final): # funcion busqueda binaria iterariva
    if final is None:
        final = len(lista)
    while inicio < final:
        mitad = (inicio+final)//2
        midval = lista[mitad]
        if midval < Val:
            inicio = mitad+1
        elif midval > Val: 
            final = mitad
        else:
            return mitad
    return -1

print("En la busqueda si se retorna un -1 es porque el numero no se encuentra en la lista.")
lista = [1,2,3,4,5,6,7,8,9,10] # Lista puesta como ejemplo.
Val = int(input("Ingrese el numero que busca"))
inicio = 0
final = None

print("Se encuentra en la posicion: ",binary_search(lista, Val,inicio,final))
