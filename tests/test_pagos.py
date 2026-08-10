from concurrent.futures import ThreadPoolExecutor
from threading import Barrier

import pytest

from src.pagos import SistemaPagos


def test_registrar_pago_correctamente():
    sistema = SistemaPagos()

    pago = sistema.registrar_pago(
        "TX-001",
        "Ana López",
        150.00
    )

    assert pago["id_transaccion"] == "TX-001"
    assert pago["estudiante"] == "Ana López"
    assert pago["valor"] == 150.00
    assert pago["estado"] == "APROBADO"
    assert sistema.contar_pagos() == 1


def test_rechazar_identificador_vacio():
    sistema = SistemaPagos()

    with pytest.raises(
        ValueError,
        match="El identificador de la transacción es obligatorio"
    ):
        sistema.registrar_pago(
            "",
            "Ana López",
            150.00
        )


def test_rechazar_estudiante_vacio():
    sistema = SistemaPagos()

    with pytest.raises(
        ValueError,
        match="El nombre del estudiante es obligatorio"
    ):
        sistema.registrar_pago(
            "TX-002",
            "",
            150.00
        )


def test_rechazar_valor_invalido():
    sistema = SistemaPagos()

    with pytest.raises(
        ValueError,
        match="El valor del pago debe ser mayor que cero"
    ):
        sistema.registrar_pago(
            "TX-003",
            "Carlos Ruiz",
            0
        )


def test_calcular_cantidad_y_total_de_pagos():
    sistema = SistemaPagos()

    sistema.registrar_pago(
        "TX-004",
        "Ana López",
        100.00
    )

    sistema.registrar_pago(
        "TX-005",
        "Carlos Ruiz",
        200.00
    )

    assert sistema.contar_pagos() == 2
    assert sistema.calcular_total() == 300.00


def test_rechazar_pago_duplicado_y_conservar_original():
    sistema = SistemaPagos()

    pago_original = sistema.registrar_pago(
        "TX-100",
        "Ana López",
        150.00
    )

    with pytest.raises(
        ValueError,
        match="La transacción ya fue procesada"
    ):
        sistema.registrar_pago(
            "TX-100",
            "Estudiante modificado",
            300.00
        )

    assert sistema.contar_pagos() == 1
    assert sistema.obtener_pagos()[0] == pago_original
    assert sistema.calcular_total() == 150.00


def test_permitir_identificadores_diferentes():
    sistema = SistemaPagos()

    sistema.registrar_pago(
        "TX-101",
        "Ana López",
        100.00
    )

    sistema.registrar_pago(
        "TX-102",
        "Carlos Ruiz",
        200.00
    )

    assert sistema.contar_pagos() == 2
    assert sistema.calcular_total() == 300.00


def test_impedir_duplicados_concurrentes():
    sistema = SistemaPagos()
    barrera = Barrier(2)

    def registrar_simultaneamente():
        barrera.wait()

        try:
            sistema.registrar_pago(
                "TX-200",
                "María Torres",
                250.00
            )
            return "APROBADO"
        except ValueError as error:
            return str(error)

    with ThreadPoolExecutor(max_workers=2) as ejecutor:
        resultados = list(
            ejecutor.map(
                lambda _: registrar_simultaneamente(),
                range(2)
            )
        )

    assert resultados.count("APROBADO") == 1
    assert resultados.count(
        "La transacción ya fue procesada."
    ) == 1
    assert sistema.contar_pagos() == 1
    assert sistema.calcular_total() == 250.00