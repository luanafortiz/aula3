import math

def area (raio):
    area = math.pi * raio**2
    return (area)
def comprimento (raio):
    comprimento = 2 * (math.pi * raio)
    return(comprimento)

i = 0
while i==0:
    try:
        raio = float (input ('digite um raio: '))
    except ValueError:
        print('burro')
    else:
        i=1
        
areaa = area(raio)
comprimentoo = comprimento(raio)
print ('uma circunferencia de raio',raio, 'tem uma área de', areaa, 'e um comprimento de',comprimentoo)