    PINTAS = ["Corazón", "Diamante", "Trébol", "Pica"]

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        if cantidad >= 0:
            self.balance += cantidad

    def retirar(self, cantidad):
        if cantidad >= 0 and cantidad <= self.balance:
            self.balance -= cantidad

    def aplicar_cuota_manejo(self):
        cuota_manejo = self.balance * 0.02
        self.balance -= abs(cuota_manejo)

    def mostrar_detalles(self):
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Balance: {self.balance:.2f} USD")



# Ejemplo de uso
vehiculo = Vehiculo(200, 50000)
print(f"Velocidad máxima del vehículo: {vehiculo.velocidad_maxima} km/h")
print(f"Kilometraje del vehículo: {vehiculo.kilometraje} km")

punto1 = Punto(0, 0)
punto2 = Punto(3, 4)
punto1.mostrar()
punto2.mostrar()
print(f"Distancia entre los puntos: {punto1.calcular_distancia(punto2):.2f}")

rectangulo = Rectangulo(Punto(1, 1), Punto(4, 5))
print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro()}")
print(f"Área del rectángulo: {rectangulo.calcular_area()}")
print(f"¿Es un cuadrado? {rectangulo.es_cuadrado()}")

circulo = Circulo(Punto(0, 0), 5)
print(f"Área del círculo: {circulo.calcular_area()}")
print(f"Perímetro del círculo: {circulo.calcular_perimetro()}")
punto3 = Punto(3, 3)
print(f"¿El punto pertenece al círculo? {circulo.punto_pertenece(punto3)}")

carta = Carta("As", "Pica")
print(f"Carta: {carta.valor} de {carta.pinta}")

cuenta = CuentaBancaria("1234567890", ["Juan", "Ana"], 5000)
cuenta.depositar(1000)
cuenta.retirar(200)
cuenta.aplicar_cuota_manejo()
cuenta.mostrar_detalles()