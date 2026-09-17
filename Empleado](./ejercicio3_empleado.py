class Trabajador:
    TASA_DESCUENTO = 0.125
    def __init__(self, horas: float, pago_hora: float):
        self.horas = horas
        self.pago_hora = pago_hora
    def salario_bruto(self) -> float:
        return self.horas * self.pago_hora
    def descuento(self) -> float:
        return self.salario_bruto() * self.TASA_DESCUENTO
    def salario_neto(self) -> float:
        return self.salario_bruto() - self.descuento()
def main():
    empleado = Trabajador(horas=48, pago_hora=5000)
    print(f"Salario bruto: ${empleado.salario_bruto():,.2f}")
    print(f"Descuento (12.5%): ${empleado.descuento():,.2f}")
    print(f"Salario neto: ${empleado.salario_neto():,.2f}")
if __name__ == "__main__":
    main()
