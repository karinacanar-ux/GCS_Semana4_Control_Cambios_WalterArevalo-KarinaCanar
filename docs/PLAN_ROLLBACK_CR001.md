# Plan de rollback de CR-001

## Información general

- Proyecto: Sistema de Matrículas
- Solicitud de cambio: CR-001
- Incidente relacionado: INC-001
- Versión afectada: v1.0
- Versión del hotfix: v1.0.1
- Responsable técnica: Karina Cañar
- Responsable de validación QA: Walter Arévalo

## Objetivo

Establecer el procedimiento para retirar el hotfix CR-001 y recuperar temporalmente la versión v1.0 si la corrección provoca errores que comprometan el registro o la consulta de pagos.

## Criterios de activación

El rollback se aplicará cuando ocurra alguna de estas situaciones:

- Las pruebas de regresión presentan fallos.
- Se rechazan identificadores válidos y diferentes.
- Los pagos originales se modifican o eliminan.
- El cálculo de la cantidad o del total de pagos es incorrecto.
- Se generan excepciones no controladas durante el registro.
- El hotfix provoca una afectación mayor que el incidente original.

## Consideraciones previas

- Confirmar que el tag `v1.0` se encuentre disponible.
- Conservar las evidencias de la falla detectada.
- No eliminar registros de pagos automáticamente.
- Informar la decisión en el issue y en el pull request.
- Obtener la validación de QA antes de cerrar el rollback.

## Procedimiento

### 1. Suspender la liberación

Si el problema se detecta antes de fusionar el pull request, no se realizará la integración con `main`. La rama del hotfix permanecerá disponible para su corrección.

### 2. Verificar el punto de recuperación

Ejecutar:

```powershell
git tag
git show v1.0 --oneline