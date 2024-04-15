class Invoice:
    def __init__(self, total_amount):
        self.total_amount = total_amount

    def generate_invoice(self):
        print(f"Factura generada por un total de ${self.total_amount}.")

class IVAResponsableInvoice(Invoice):
    def generate_invoice(self):
        print(f"Factura para IVA Responsable por un total de ${self.total_amount}.")

class IVANoInscriptoInvoice(Invoice):
    def generate_invoice(self):
        print(f"Factura para IVA No Inscripto por un total de ${self.total_amount}.")

class IVAExentoInvoice(Invoice):
    def generate_invoice(self):
        print(f"Factura para IVA Exento por un total de ${self.total_amount}.")

class InvoiceFactory:
    @staticmethod
    def create_invoice(total_amount, tax_condition):
        if tax_condition == "IVA Responsable":
            return IVAResponsableInvoice(total_amount)
        elif tax_condition == "IVA No Inscripto":
            return IVANoInscriptoInvoice(total_amount)
        elif tax_condition == "IVA Exento":
            return IVAExentoInvoice(total_amount)
        else:
            raise ValueError("Condición impositiva no reconocida.")

# Ejemplo de uso del Factory Method
total_amount = 1000  # Total de la factura
tax_condition = "IVA Responsable"  # Condición impositiva del cliente
invoice = InvoiceFactory.create_invoice(total_amount, tax_condition)
invoice.generate_invoice()  # Salida: Factura para IVA Responsable por un total de $1000.
