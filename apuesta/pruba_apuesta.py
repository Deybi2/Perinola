from clase_apuesta import Apuesta

apuesta = Apuesta()
print(apuesta)
apuesta.ponerFicha(50)
print(apuesta) 
apuesta.ponerFicha()
print(apuesta) 
apuesta.tomarFicha(10)
print(apuesta)
apuesta.tomarTodas()
print(apuesta) 
print(apuesta.estaVacia())
print(apuesta.tieneFicha())

