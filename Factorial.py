class Factorial:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def calculate_factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is undefined for negative numbers.")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Ejemplo de uso
factorial_calculator = Factorial()
print(factorial_calculator.calculate_factorial(5))  # Salida: 120
