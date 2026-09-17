class GrupoFamiliar:
    def __init__(self, edad_juan: float):
        self.edad_juan = edad_juan
    def edad_alberto(self) -> float:
        return self.edad_juan * 2 / 3
    def edad_ana(self) -> float:
        return self.edad_juan * 4 / 3
    def edad_mama(self) -> float:
        return (
            self.edad_juan
            + self.edad_alberto()
            + self.edad_ana()
        )
def main():
    edad = float(input("Ingrese la edad de Juan: "))
    familia = GrupoFamiliar(edad)
    print(f"Edad de Juan: {familia.edad_juan:.1f} años")
    print(f"Edad de Alberto: {familia.edad_alberto():.1f} años")
    print(f"Edad de Ana: {familia.edad_ana():.1f} años")
    print(f"Edad de la mamá: {familia.edad_mama():.1f} años")
if __name__ == "__main__":
    main()
