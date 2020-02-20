import math
raio = float (input ('digite um raio: '))

def area (raio):
    area = math.pi * raio**2
    return (area)
def comprimento (raio):
    comprimento = 2 * (math.pi * raio)
    return(comprimento)
areaa = area(raio)
comprimentoo = comprimento(raio)
print ('uma circunferencia de raio',raio, 'tem uma área de', areaa, 'e um comprimento de',comprimentoo)