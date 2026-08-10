from src.pagos import SistemaPagos


def ejecutar_simulacion():
    sistema = SistemaPagos()

    operaciones = [
        {
            "id_transaccion": f"TX-{numero:03d}",
            "estudiante": f"Estudiante {numero}",
            "valor": 100.00,
        }
        for numero in range(1, 100)
    ]

    # Reintento de una transacción ya procesada.
    operaciones.append(
        {
            "id_transaccion": "TX-050",
            "estudiante": "Estudiante 50",
            "valor": 100.00,
        }
    )

    operaciones_aceptadas = 0
    operaciones_rechazadas = 0

    for operacion in operaciones:
        try:
            sistema.registrar_pago(
                operacion["id_transaccion"],
                operacion["estudiante"],
                operacion["valor"],
            )
            operaciones_aceptadas += 1
        except ValueError as error:
            operaciones_rechazadas += 1
            print(f"Reintento rechazado: {error}")

    pagos_registrados = sistema.obtener_pagos()

    identificadores_unicos = {
        pago["id_transaccion"]
        for pago in pagos_registrados
    }

    registros_duplicados = (
        len(pagos_registrados) - len(identificadores_unicos)
    )

    print("\nRESULTADO DE LA VALIDACIÓN DEL HOTFIX")
    print(f"Operaciones procesadas: {len(operaciones)}")
    print(f"Operaciones aceptadas: {operaciones_aceptadas}")
    print(f"Operaciones rechazadas: {operaciones_rechazadas}")
    print(f"Transacciones únicas: {len(identificadores_unicos)}")
    print(f"Registros duplicados: {registros_duplicados}")

    if registros_duplicados == 0 and operaciones_rechazadas == 1:
        print("Resultado: INCIDENTE CORREGIDO")
    else:
        print("Resultado: INCIDENTE NO CORREGIDO")


if __name__ == "__main__":
    ejecutar_simulacion()