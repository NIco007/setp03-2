def b_search(Arr,Val,inicio,final):
        
	mitad = int((inicio + final)/2)
	
	if Arr[mitad] == Val:
		return mitad
	elif inicio > final or Arr[-1] < Val:
		return -1
	if Arr[mitad] < Val:
		return b_search(Arr,Val,mitad+1,final)
	else:
		return b_search(Arr,Val,inicio,mitad-1)


Arr = [1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,22] # Lista puesta como ejemplo en el algoritmo


print("Si se retorna un -1, es por que el numero no se encuentra en la lista")
inicio = 0
final = None
if final is None:
    final = len(Arr)

Val = int(input("Ingrese el numero que esta buscando"))

print("El numero se encuentra en la posicion ",b_search(Arr,Val,inicio,final)," de la lista ")
