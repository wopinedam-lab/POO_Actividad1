import math
class FiguraCircular:
    def __init__(self, radio: float):
        self.radio = radio
    def calcular_area(self) -> float:
        return math.pi * self.radio ** 2
    def calcular_longitud(self) -> float:
        return 2 * math.pi * self.radio
def main():
    radio = float(input("Ingrese el radio del círculo: "))
    figura = FiguraCircular(radio)
    print(f"Área del círculo: {figura.calcular_area():.4f}")
    print(f"Longitud de la circunferencia: {figura.calcular_longitud():.4f}")
if __name__ == "__main__":
    main()
