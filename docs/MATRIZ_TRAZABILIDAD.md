# Matriz de trazabilidad de auditoría y release

**Proyecto:** Sistema de matrículas  
**Versión prevista:** v1.1.0  
**Fecha de inicio:** 24 de agosto de 2026  
**Integrantes:** Karina Cañar y Walter Arévalo  

## Objetivo

Relacionar cada responsabilidad de la auditoría con su issue, rama, commits, pull request, release y evidencia verificable.

## Registro de trazabilidad
| Issue | Responsable | Rama | Commit(s) | PR | Release | Evidencia | Estado |
|---|---|---|---|---|---|---|---|
| #3 Auditoría física | Walter Arévalo | `audit/config-items-issue-3` | `0bbbece`, `8f90960`, `8e965a0`, `29667c4` | PR #9 | `v1.1.0` | Informe físico, `.env.example`, licencia y checklist | Completado |
| #4 Auditoría funcional | Karina Cañar | `test/pagos-duplicados-issue-4` | `6084ffb`, `26a8fd6`, `f93a64f` | PR #8 | `v1.1.0` | Workflow, informe funcional y 8 pruebas aprobadas | Completado |
| #5 Trazabilidad | Karina Cañar | `docs/trazabilidad-issue-5` | `ebb7e69`, `40d3189`, `396e136` | PR #7 | `v1.1.0` | Plantilla de PR, convenciones y matriz | Completado |
| #6 Release controlado | Walter Arévalo | `release/v1.1.0-issue-6` | `5cb5583` | Pendiente | `v1.1.0` | Release notes y criterios de entrega | En proceso |

## Línea base auditada

- Rama: `main`
- Commit posterior al PR #9: `b51c007`
- Pruebas funcionales: 8 aprobadas de 8
- Issues completados: #3, #4 y #5
- Release previsto: `v1.1.0`

## Criterios de actualización

1. Sustituir “Pendiente” por los identificadores reales de commits y PR.
2. Incorporar los enlaces de GitHub al elaborar el informe final.
3. Actualizar el estado después de la revisión y el merge.
4. Verificar que el tag `v1.1.0` corresponda a un commit de `main`.
5. Conservar capturas de los issues, revisiones, merges y release.

## Flujo verificable

`Issue → Rama → Commit → Pull request → Revisión cruzada → Merge a main → Tag → Release`
