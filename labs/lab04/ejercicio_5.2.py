maximo = 0
minimo = 0
primer_numero = True
while True:
    try:
        inpu_str = input("Ingresar un número: ")
        if(inpu_str == "done"):
            break
        else:
            if (primer_numero):
                maximo = int(inpu_str)
                minimo = int(inpu_str)
                primer_numero = False
            else:
                if (int(inpu_str) > maximo): maximo = int(inpu_str)
                if (int(inpu_str) < minimo): minimo = int(inpu_str)
    except:
        print("Valor no es válido")
        continue
print("Máximo: ", maximo)
print("Mínimo: ", minimo)
