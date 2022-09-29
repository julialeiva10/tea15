def calculoSalario(horas, tarifa):
    MAX_HORAS_SEMANALES = 40
    horas_extras = 0
    horas_extras = horas - MAX_HORAS_SEMANALES
    if (horas_extras > 0):
        pago = (MAX_HORAS_SEMANALES * tarifa) + (horas_extras * (tarifa * 1.5))
    else:
        pago = (horas * tarifa)
    return pago

try:
    horas = int(input("Ingrese cantidad de horas: "))
    tarifa = float(input("Ingrese tarifa: "))
    salario = calculoSalario(horas, tarifa)
    print(salario)
except:
    print("Error, debe ingresar valores numéricos")

