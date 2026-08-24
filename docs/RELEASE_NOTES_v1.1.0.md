# Release notes — v1.1.0

**Proyecto:** Sistema de matrículas  
**Fecha:** 24 de agosto de 2026  
**Responsable de la emisión:** Walter Arévalo  
**Rama de preparación:** `release/v1.1.0-issue-6`  
**Línea base auditada previa:** `main`, commit `b51c007`  

## 1. Resumen

La versión v1.1.0 incorpora controles documentados de auditoría física y funcional, trazabilidad de cambios, revisión cruzada y automatización de pruebas. La emisión se prepara desde una línea base aprobada en `main`.

## 2. Cambios incorporados

### Auditoría física

- Verificación de los elementos de configuración.
- Incorporación de `.env.example` sin credenciales reales.
- Incorporación de la licencia MIT.
- Creación del informe `docs/AUDITORIA_FISICA.md`.
- Confirmación de ausencia de secretos y archivos temporales.

### Auditoría funcional

- Validación del requisito de prevención de pagos duplicados.
- Incorporación del workflow de GitHub Actions.
- Ejecución automatizada de ocho pruebas.
- Resultado: 8 pruebas aprobadas, 0 fallidas.
- Creación del informe `docs/AUDITORIA_FUNCIONAL_PAGOS.md`.

### Trazabilidad

- Incorporación de una plantilla de pull request.
- Definición de convenciones para ramas y commits.
- Creación de la matriz de trazabilidad.
- Vinculación entre issues, ramas, commits y PR.

## 3. Issues y pull requests relacionados

| Issue | Pull request | Resultado |
|---|---|---|
| #3 Auditoría física | PR #9 | Hallazgos corregidos |
| #4 Auditoría funcional | PR #8 | 8 pruebas aprobadas |
| #5 Trazabilidad | PR #7 | Documentación incorporada |
| #6 Release controlado | PR de preparación pendiente | En proceso |

## 4. Procedimiento de validación

1. Verificar que el tag `v1.1.0` apunte a un commit de `main`.
2. Abrir GitHub Actions.
3. Confirmar que el workflow “Auditoría funcional de pagos” termine satisfactoriamente.
4. Verificar el resultado `8 passed`.
5. Revisar los informes de auditoría física y funcional.
6. Confirmar la existencia de `.env.example`, `LICENSE` y la plantilla de PR.
7. Comprobar las referencias a los issues y PR incluidos.

## 5. Criterios de entrega

- [x] Auditoría física documentada.
- [x] Auditoría funcional ejecutada.
- [x] Pruebas automatizadas aprobadas.
- [x] Issues y PR relacionados.
- [x] Revisión cruzada aplicada.
- [x] Cambios fusionados en `main`.
- [ ] PR de preparación del release aprobado.
- [ ] Tag `v1.1.0` creado desde `main`.
- [ ] Release publicado y verificado.

## 6. Compatibilidad

La versión mantiene compatibilidad con la funcionalidad anterior. Los cambios se concentran en auditoría, documentación, configuración segura y automatización de pruebas.

## 7. Resultado esperado

El release debe proporcionar una versión íntegra, trazable y verificable del sistema, acompañada de notas de entrega y evidencia de calidad.
