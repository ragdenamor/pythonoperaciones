#Funcion que recibe una lisya u regresa la sumatoria
def sumar(numeros:list[float]) -> float:
    res=sum(numeros)
    return res

#Funcion que recibe una lista y regresa su promedio
def promediar(numeros:list[float]) ->float:
    if( len(numeros)==0):
        return 0
    prom=sum(numeros) / len(numeros)
    return prom

datos=[10, 20, 34, 1.5, 70.2]
s = sumar(datos)
print("Sumatoria ", s)

p=promediar(datos)
print("Promedio ", p)