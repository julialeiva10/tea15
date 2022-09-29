Total = 0
contador = 0
while True:
    input_str = input("Ingrese un numero: ")
    try:
        if(input_str == "done"):
            break
        else:
            Total = Total + int(input_str)
            contador = contador + 1
            average = Total  / contador
    except:
            print("valor no es válido")
            continue
print("Total: ", Total)
print("contador: ", contador)
print("promedio: ", average)
