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

## Actualización del requisito RF-PAG-04

### RF-PAG-04: Control de pagos duplicados

El sistema deberá impedir que un identificador de transacción previamente procesado sea registrado nuevamente. Ante un reintento, deberá generar un error controlado, conservar intacto el pago original y evitar duplicaciones producidas por solicitudes simultáneas.

**Prioridad:** Alta  
**Versión de incorporación:** v1.0.1  
**Solicitud relacionada:** CR-001  
**Incidente relacionado:** INC-001  

### Criterios de aceptación

- El mismo identificador de transacción no puede registrarse dos veces.
- El segundo intento debe generar el mensaje: `La transacción ya fue procesada.`
- El pago registrado originalmente debe conservar sus datos y valor.
- Los identificadores diferentes deben procesarse normalmente.
- Dos solicitudes simultáneas con el mismo identificador deben producir un solo pago.
- Las validaciones de identificador, estudiante y valor deben continuar funcionando.
- Todas las pruebas automatizadas deben finalizar satisfactoriamente.

### Evidencia de validación

La corrección fue comprobada mediante ocho pruebas automatizadas. Además, se simularon 100 operaciones: 99 fueron aceptadas y un reintento fue rechazado, obteniéndose 99 transacciones únicas y cero registros duplicados.