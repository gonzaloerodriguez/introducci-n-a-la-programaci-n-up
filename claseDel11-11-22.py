minLapices = 0 
maxLapices = 0
cantOrdenDeLapiceras = 0
cantLapiceras = 0
cantLapices = 0 

#total vendido en pesos
#cantidad min vendida de lapices
#promedio vendido de lapiceras
#el porcentaje vendido de cada item

nroDeOrden = int(input('Ingrese el numero de orden'))

while nroDeOrden != 0:
    cantLapices = int(input('Ingrse la cantidad de lapices'))
    if maxLapices == 0 or cantLapices > maxLapices:
       maxLapices = cantLapices
    if minLapices == 0 or cantLapices < minLapices:
        minLapices = cantLapices
    cantLapiceras = int(input('Ingrse la cantidad de lapiceras'))
    if cantLapices > 0:
        pesosLapices = cantLapices * 15
        cantLapices = cantLapices + cantLapices
    if cantLapiceras > 0:
        pesosLapiceras = cantLapiceras * 10
        cantLapiceras = cantLapiceras + cantLapiceras
        cantOrdenDeLapiceras = cantOrdenDeLapiceras + 1         
    nroDeOrden = int(input('Ingrese el numero de orden'))
    
totalDeItems = cantLapices + cantLapiceras

print(f'La cantidad total vendida en pesos es de {pesosLapices + pesosLapiceras}')
print(f'La cantidad minima vendidad de lapices es {minLapices}')
print(f'El promedio de lapiceras vendidas es de {cantLapiceras / cantOrdenDeLapiceras}')
print(f'El porcentaje vendido de cada item es {(cantLapices*100) / totalDeItems}% de lapices y {(cantLapiceras*100) / totalDeItems}% de lapiceras')
