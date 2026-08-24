# Convenciones de versionado y trazabilidad

**Proyecto:** Sistema de matrículas  
**Versión del documento:** 1.0  
**Fecha:** 24 de agosto de 2026  
**Responsable:** Karina Cañar  

## 1. Objetivo

Establecer reglas para identificar, relacionar y verificar los cambios realizados en el repositorio, garantizando la trazabilidad entre issues, ramas, commits, pull requests y releases.

## 2. Convención para issues

Cada cambio debe originarse en un issue abierto, asignado a un responsable y con criterios de aceptación verificables.

Formato recomendado del título:

`CÓDIGO: descripción breve`

Ejemplos:

- `AUD-01: Auditoría física de los elementos de configuración`
- `FUNC-01: Validar la prevención de pagos duplicados`
- `TRAZ-01: Implementar trazabilidad`
- `REL-01: Publicar release controlado`

## 3. Convención para ramas

Formato:

`tipo/descripcion-issue-numero`

Tipos autorizados:

- `audit/`: auditorías de configuración.
- `test/`: pruebas funcionales.
- `docs/`: documentación y trazabilidad.
- `release/`: preparación de versiones.

Ejemplos:

- `audit/config-items-issue-3`
- `test/pagos-duplicados-issue-4`
- `docs/trazabilidad-issue-5`
- `release/v1.1.0-issue-6`

Las ramas deben crearse desde `main`.

## 4. Convención para commits

Formato:

`tipo: descripción breve (#issue)`

Tipos autorizados:

- `docs`: documentación.
- `test`: pruebas.
- `fix`: correcciones.
- `chore`: configuración o mantenimiento.

Ejemplos:

- `docs: agregar plantilla de pull request (#5)`
- `test: documentar validación de pagos duplicados (#4)`
- `chore: completar elementos de configuración (#3)`

## 5. Convención para pull requests

Todo pull request debe:

1. Utilizar `main` como rama base.
2. Identificar el issue mediante `Closes #número`.
3. Describir los cambios realizados.
4. Incluir evidencia y procedimiento de validación.
5. Completar el checklist de auditoría.
6. Ser revisado por el otro integrante antes del merge.

## 6. Convención para releases

Las versiones utilizarán el formato `vMAYOR.MENOR.PARCHE`.

- **MAYOR:** cambios incompatibles.
- **MENOR:** mejoras compatibles.
- **PARCHE:** correcciones compatibles.

El release debe crearse desde `main` después de fusionar los cambios aprobados. Sus notas deben indicar qué cambió, cómo validar la versión y cuáles issues y PR fueron incorporados.

## 7. Flujo de trazabilidad

`Issue → Rama → Commit → Pull request → Revisión → Merge a main → Tag → Release`

No se incorporarán cambios a `main` sin issue, evidencia y pull request relacionado.
