from threading import Lock


class SistemaPagos:
    """Gestiona el registro de pagos de matrículas."""

    def __init__(self):
        self.pagos = []
        self._ids_registrados = set()
        self._lock = Lock()

    def registrar_pago(
        self,
        id_transaccion: str,
        estudiante: str,
        valor: float
    ) -> dict:
        """
        Registra un pago e impide procesar dos veces
        el mismo identificador de transacción.
        """
        if not id_transaccion:
            raise ValueError(
                "El identificador de la transacción es obligatorio."
            )

        if not estudiante:
            raise ValueError(
                "El nombre del estudiante es obligatorio."
            )

        if valor <= 0:
            raise ValueError(
                "El valor del pago debe ser mayor que cero."
            )

        pago = {
            "id_transaccion": id_transaccion,
            "estudiante": estudiante,
            "valor": float(valor),
            "estado": "APROBADO",
        }

        # La validación y el registro se ejecutan de forma protegida.
        with self._lock:
            if id_transaccion in self._ids_registrados:
                raise ValueError(
                    "La transacción ya fue procesada."
                )

            self.pagos.append(pago)
            self._ids_registrados.add(id_transaccion)

        return pago

    def obtener_pagos(self) -> list:
        """Retorna una copia de los pagos registrados."""
        with self._lock:
            return self.pagos.copy()

    def contar_pagos(self) -> int:
        """Retorna la cantidad total de registros."""
        with self._lock:
            return len(self.pagos)

    def calcular_total(self) -> float:
        """Calcula el valor total de los pagos registrados."""
        with self._lock:
            return sum(pago["valor"] for pago in self.pagos)