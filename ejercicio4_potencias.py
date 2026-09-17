class OperadorPotencias:
    def __init__(self, numero: float):
        self.numero = numero
    def cuadrado(self) -> float:
        return self.numero ** 2
    def cubo(self) -> float:
        return self.numero ** 3
def main():
    numero = float(input("Ingrese un número: "))
    operador = OperadorPotencias(numero)
    print(f"El cuadrado de {numero} es: {operador.cuadrado()}")
    print(f"El cubo de {numero} es: {operador.cubo()}")
if __name__ == "__main__":
    main()
