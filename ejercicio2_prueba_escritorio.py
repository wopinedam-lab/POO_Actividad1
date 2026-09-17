class SecuenciaNumerica:
    def __init__(self):
        self.total = 0
        self.valor_x = 0
        self.valor_y = 0
    def resolver_secuencia(self) -> float:
        self.total = 0
        self.valor_x = 20
        self.total += self.valor_x
        self.valor_y = 40
        self.valor_x += self.valor_y ** 2
        self.total += self.valor_x / self.valor_y
        return self.total
def main():
    secuencia = SecuenciaNumerica()
    resultado = secuencia.resolver_secuencia()
    print(f"El resultado de la suma es: {resultado}")
if __name__ == "__main__":
    main()
