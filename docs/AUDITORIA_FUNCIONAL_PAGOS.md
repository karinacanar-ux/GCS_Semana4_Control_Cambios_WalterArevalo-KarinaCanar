# Informe de auditoría funcional: prevención de pagos duplicados

**Proyecto:** Sistema de matrículas  
**Auditor:** Karina Cañar  
**Issue:** #4  
**Rama:** `test/pagos-duplicados-issue-4`  
**Fecha:** 24 de agosto de 2026  
**Estado:** Aprobado  

## 1. Requisito auditado

El sistema debe impedir que un mismo pago sea registrado más de una vez, conservando la integridad de la información de matrículas.

## 2. Criterios de aceptación

| Código | Criterio | Evidencia | Resultado |
|---|---|---|---|
| CA-01 | El sistema acepta el primer registro de un pago con identificador único. | `test_registrar_pago_correctamente` | Cumple |
| CA-02 | El sistema rechaza un segundo registro con el mismo identificador. | `test_rechazar_pago_duplicado_y_conservar_original` | Cumple |
| CA-03 | El intento duplicado no altera la cantidad ni el valor total registrado. | Verificación de un pago y total de USD 150,00 después del intento duplicado | Cumple |

## 3. Procedimiento aplicado

1. Se revisó el archivo `tests/test_pagos.py`.
2. Se configuró un workflow de GitHub Actions.
3. Se instaló Python 3.12 y las dependencias del proyecto.
4. Se ejecutó `python -m pytest -v`.
5. Se verificó individualmente el resultado de las ocho pruebas.

## 4. Entorno de ejecución

- Plataforma: GitHub Actions sobre Linux.
- Python: 3.12.14.
- Pytest: 8.4.1.
- Archivo evaluado: `tests/test_pagos.py`.
- Ejecución: workflow “Auditoría funcional de pagos”, corrida #2.

## 5. Resultado

La ejecución recopiló ocho pruebas y obtuvo el siguiente resultado:

- Pruebas ejecutadas: 8.
- Pruebas aprobadas: 8.
- Pruebas fallidas: 0.
- Porcentaje de aprobación: 100 %.
- Tiempo de ejecución: 0.06 segundos.

También se validaron identificadores vacíos, nombres de estudiantes vacíos, valores inválidos, identificadores diferentes y registros duplicados concurrentes.

## 6. Hallazgo y corrección

La primera ejecución no logró importar el módulo `src` porque la raíz del proyecto no estaba incorporada en la ruta de Python del entorno automatizado. Este evento correspondió a una deficiencia de configuración del workflow, no a un defecto funcional del sistema.

La configuración fue corregida mediante el commit `26a8fd6`, incorporando `PYTHONPATH` y ejecutando las pruebas con `python -m pytest -v`. La segunda ejecución terminó satisfactoriamente.

## 7. Checklist de verificación

- [x] El primer pago fue aceptado.
- [x] El pago duplicado fue rechazado.
- [x] El pago original permaneció sin modificaciones.
- [x] La cantidad de pagos permaneció en uno.
- [x] El valor total permaneció en USD 150,00.
- [x] La prueba de concurrencia impidió el registro simultáneo duplicado.
- [x] Las ocho pruebas fueron aprobadas.

## 8. Conclusión

El requisito funcional de prevención de pagos duplicados cumple los tres criterios de aceptación definidos. La evidencia automatizada demuestra que el sistema conserva el registro original, rechaza transacciones repetidas y mantiene íntegros la cantidad y el valor total de los pagos.
