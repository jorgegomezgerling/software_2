class ComidaRapida:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, food_name):
        if not hasattr(self, 'food_name'):
            self.food_name = food_name

    def delivery(self):
        print(f"{self.food_name} entregada por delivery.")

    def counter_pickup(self):
        print(f"{self.food_name} lista para ser retirada en el mostrador.")

    def customer_pickup(self):
        print(f"{self.food_name} lista para ser retirada por el cliente.")

# Ejemplo de uso
hamburguesa1 = ComidaRapida("Hamburguesa")
hamburguesa2 = ComidaRapida("Hamburguesa Doble")

print(hamburguesa1 is hamburguesa2)  # Salida: True
hamburguesa1.delivery()  # Salida: Hamburguesa entregada por delivery.
hamburguesa2.counter_pickup()  # Salida: Hamburguesa lista para ser retirada en el mostrador.
hamburguesa1.customer_pickup()  # Salida: Hamburguesa lista para ser retirada por el cliente.
