# Especificación de requisitos del Sistema de Matrículas

**Versión:** 1.0  
**Módulo:** Registro de pagos  

## Requisitos funcionales

- RF-PAG-01: El sistema debe registrar el identificador de la transacción, el estudiante y el valor pagado.
- RF-PAG-02: El identificador y el nombre del estudiante son obligatorios.
- RF-PAG-03: El valor del pago debe ser mayor que cero.
- RF-PAG-04: Cada identificador de transacción debe procesarse una sola vez para evitar pagos duplicados.
- RF-PAG-05: El sistema debe permitir consultar la cantidad y el valor total de los pagos registrados.

## Incidente identificado

El incidente INC-001 evidencia que, durante el reintento de una transacción, el sistema acepta nuevamente un identificador ya procesado. En la simulación se obtuvo un pago duplicado en 100 operaciones, equivalente al 1 %.

## Estado de la versión 1.0

Las validaciones generales funcionan correctamente; sin embargo, RF-PAG-04 no se cumple debido a la ausencia de un control de idempotencia. La corrección deberá gestionarse mediante una solicitud de cambio y un hotfix.