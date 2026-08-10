# Sistema de Matrículas

Proyecto académico para aplicar el control de configuración sobre un incidente de duplicación de pagos.

## Línea base v1.0

La versión inicial permite registrar y consultar pagos de matrículas. Contiene el incidente INC-001, causado por la falta de validación de identificadores de transacción repetidos.

## Ejecutar las pruebas

```powershell
py -m pytest -q

## Hotfix CR-001

Se implementó una corrección para impedir el registro duplicado de pagos cuando una transacción es reenviada o procesada simultáneamente. El sistema valida la unicidad del identificador, conserva el pago original y genera un error controlado ante un reintento.

### Cambios realizados

- Control de identificadores de transacción duplicados.
- Protección frente a solicitudes concurrentes.
- Conservación del primer pago registrado.
- Actualización de las pruebas automatizadas.
- Validación mediante la simulación del incidente INC-001.
- Documentación del análisis de impacto y del plan de rollback.

### Validación

```powershell
py -m pytest -q
py -m scripts.reproducir_incidente
