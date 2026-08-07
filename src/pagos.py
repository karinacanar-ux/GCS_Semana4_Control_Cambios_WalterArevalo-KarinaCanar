class SistemaPagos:
    """Gestiona el registro de pagos de matrículas."""

    def __init__(self):
        self.pagos = []

    def registrar_pago(
        self,
        id_transaccion: str,
        estudiante: str,
        valor: float
    ) -> dict:
        """
        Registra un pago.

        Defecto conocido:
        no valida si el identificador de la transacción ya existe.
        """
        if not id_transaccion:
            raise ValueError("El identificador de la transacción es obligatorio.")

        if not estudiante:
            raise ValueError("El nombre del estudiante es obligatorio.")

        if valor <= 0:
            raise ValueError("El valor del pago debe ser mayor que cero.")

        pago = {
            "id_transaccion": id_transaccion,
            "estudiante": estudiante,
            "valor": float(valor),
            "estado": "APROBADO",
        }

        self.pagos.append(pago)
        return pago

    def obtener_pagos(self) -> list:
        """Retorna los pagos registrados."""
        return self.pagos.copy()

    def contar_pagos(self) -> int:
        """Retorna la cantidad total de registros."""
        return len(self.pagos)

    def calcular_total(self) -> float:
        """Calcula el valor total de los pagos registrados."""
        return sum(pago["valor"] for pago in self.pagos)