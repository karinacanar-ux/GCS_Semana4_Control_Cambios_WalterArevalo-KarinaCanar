# Análisis de impacto de CR-001

## Información general

- Proyecto: Sistema de Matrículas
- Solicitud de cambio: CR-001
- Incidente relacionado: INC-001
- Versión afectada: v1.0
- Versión prevista: v1.0.1
- Tipo de cambio: Correctivo urgente (hotfix)
- Prioridad: Alta
- Responsable técnica: Karina Cañar
- Responsable de QA: Walter Arévalo

## Descripción del cambio

La solicitud CR-001 corrige la duplicación de pagos ocasionada por el reintento de una transacción previamente procesada. El cambio incorpora una validación de unicidad del identificador y protege el registro frente a solicitudes concurrentes.

## Elementos de configuración afectados

| Elemento | Impacto | Acción realizada |
|---|---|---|
| `src/pagos.py` | Alto | Se incorporó el control de identificadores duplicados y el bloqueo para operaciones concurrentes. |
| `tests/test_pagos.py` | Alto | Se agregaron pruebas de duplicación, conservación del pago original y concurrencia. |
| `scripts/reproducir_incidente.py` | Medio | Se actualizó la simulación para validar la corrección del incidente. |
| `docs/SRS_MATRICULAS_v1.md` | Medio | Se actualizará el requisito RF-PAG-04 y sus criterios de aceptación. |
| `README.md` | Bajo | Se documentará la versión corregida y su validación. |
| Plan de rollback | Medio | Se documentará el procedimiento para regresar a v1.0. |

## Impacto técnico y operativo

La modificación se limita al módulo de pagos y no cambia la interfaz pública del sistema. Los identificadores diferentes continúan procesándose normalmente, mientras que los reintentos con un identificador registrado generan un error controlado. Las validaciones previas del estudiante, valor e identificador permanecen vigentes.

## Evaluación de riesgos

| Riesgo | Nivel | Tratamiento |
|---|---|---|
| Duplicación causada por solicitudes simultáneas | Crítico | Proteger la validación y el registro mediante un bloqueo. |
| Alteración de las validaciones existentes | Medio | Ejecutar todas las pruebas de regresión. |
| Rechazo de una transacción legítima con ID repetido | Medio | Emitir un mensaje controlado y conservar el pago original. |
| Falla inesperada del hotfix | Alto | Aplicar el plan de rollback hacia v1.0. |
| Permanencia de duplicados anteriores | Alto | Revisar los registros históricos sin eliminarlos automáticamente. |

## Resultados de validación

- Pruebas automatizadas aprobadas: 8.
- Operaciones simuladas: 100.
- Operaciones aceptadas: 99.
- Operaciones rechazadas: 1.
- Transacciones únicas: 99.
- Registros duplicados: 0.
- Resultado: incidente corregido.

## Decisión

Se aprueba técnicamente CR-001 porque la corrección protege la integridad de los pagos, conserva las validaciones existentes y cumple los criterios de aceptación definidos. La integración quedará sujeta a la revisión de QA y a la documentación del plan de rollback.