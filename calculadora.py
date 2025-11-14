class calculadora1:
    PI = 3.14
    
    @staticmethod #classe estática
    def circunferencia( raio) -> float:
        return 2 * calculadora1.PI * raio
    
    @staticmethod #classe estática
    def area(raio) -> float:
        return calculadora1.PI * raio**2
