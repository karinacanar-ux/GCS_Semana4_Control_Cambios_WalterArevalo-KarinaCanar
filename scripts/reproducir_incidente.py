from src.pagos import SistemaPagos


def reproducir_incidente():
    sistema = SistemaPagos()

    # Se procesan 99 transacciones diferentes.
    for numero in range(1, 100):
        sistema.registrar_pago(
            id_transaccion=f"TX-{numero:03d}",
            estudiante=f"Estudiante {numero}",
            valor=100.00
        )

    # El sistema reintenta una transacción ya procesada.
    sistema.registrar_pago(
        id_transaccion="TX-050",
        estudiante="Estudiante 50",
        valor=100.00
    )

    pagos = sistema.obtener_pagos()
    identificadores = [pago["id_transaccion"] for pago in pagos]

    total_registros = len(identificadores)
    transacciones_unicas = len(set(identificadores))
    registros_duplicados = total_registros - transacciones_unicas
    porcentaje_duplicacion = registros_duplicados / total_registros * 100

    print("=== REPRODUCCIÓN DEL INCIDENTE INC-001 ===")
    print(f"Operaciones procesadas: {total_registros}")
    print(f"Transacciones únicas: {transacciones_unicas}")
    print(f"Registros duplicados: {registros_duplicados}")
    print(f"Porcentaje de duplicación: {porcentaje_duplicacion:.2f}%")

    if registros_duplicados > 0:
        print("Resultado: INCIDENTE REPRODUCIDO")
        print("Causa: no existe control para impedir IDs repetidos.")


if __name__ == "__main__":
    reproducir_incidente()