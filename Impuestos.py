class Impuestos:
    def calculate_taxes(self, base_amount):
        iva = base_amount * 0.21  # IVA (21%)
        iibb = base_amount * 0.05  # IIBB (5%)
        municipal_contributions = base_amount * 0.012  # Contribuciones municipales (1.2%)
        total_taxes = iva + iibb + municipal_contributions
        return total_taxes

class IVAResponsable(Impuestos):
    def calculate_taxes(self, base_amount):
        iva = base_amount * 0.21  # IVA (21%)
        return iva

class IVANoInscripto(Impuestos):
    def calculate_taxes(self, base_amount):
        iibb = base_amount * 0.05  # IIBB (5%)
        return iibb

class IVAExento(Impuestos):
    def calculate_taxes(self, base_amount):
        return 0  # Impuestos exentos de IVA

class ImpuestosFactory:
    def get_impuestos(self, tipo_contribuyente):
        if tipo_contribuyente == "Responsable":
            return IVAResponsable()
        elif tipo_contribuyente == "No Inscripto":
            return IVANoInscripto()
        elif tipo_contribuyente == "Exento":
            return IVAExento()
        else:
            raise ValueError("Tipo de contribuyente no válido")

# Ejemplo de uso del Factory Method
factory = ImpuestosFactory()
tipo_contribuyente = "Responsable"  # Ejemplo de tipo de contribuyente
impuestos_calculator = factory.get_impuestos(tipo_contribuyente)
base_amount = 1000  # Ejemplo de base imponible
taxes = impuestos_calculator.calculate_taxes(base_amount)
print(f"Total taxes for ${base_amount} (Tipo: {tipo_contribuyente}): ${taxes:.2f}")
