# 🧾 Sistema de Gestión de Tareas (ToDo List)

![CI Status](https://github.com/julixxcode/todo-list-testing/actions/workflows/tests.yml/badge.svg)

Proyecto desarrollado como **Taller Práctico Integrador** del módulo de *Codificación y Pruebas de Software*.

---

## 🎯 Objetivo del Taller
Desarrollar un sistema completo de gestión de tareas aplicando **principios SOLID**, **TDD (Test Driven Development)** y **Clean Code**, garantizando más del 80 % de cobertura en las pruebas automatizadas.

---

## ⚙️ Tecnologías Utilizadas
- **Python 3.12**
- **pytest** + **pytest-cov**
- **Git / GitHub**
- **GitHub Actions** (CI/CD)
- **VSCode**

---

## 📂 Estructura del Proyecto
```text
todo-list-testing/
│
├── src/
│   └── inventario_tareas/
│       ├── task.py
│       └── task_manager.py
│
├── tests/
│   ├── test_task.py
│   └── test_manager.py
│
├── docs/
│   ├── design.md
│   └── README.md
│
└── .github/workflows/tests.yml
🧠 Modelo de Clases
Task
Representa una tarea individual con:

id: Identificador único

title: Título descriptivo

priority: Enum {LOW, MEDIUM, HIGH}

status: Enum {PENDING, IN_PROGRESS, DONE}

TaskManager
Gestiona las operaciones sobre las tareas:

add_task() → crea una nueva tarea

get_task() → consulta por ID

update_status() → cambia estado

list_tasks() → filtra por estado

as_dict() → exporta todas las tareas

🧪 Pruebas Automatizadas
Las pruebas fueron diseñadas siguiendo el ciclo TDD:

Red phase: escribir un test que falle

Green phase: implementar el código mínimo

Refactor: limpiar sin romper tests

Comandos:

bash
Copiar código
pytest -v
pytest --cov=src --cov-report=term-missing
Cobertura obtenida: 100 %

🔄 Integración Continua (CI/CD)
El pipeline se ejecuta automáticamente en GitHub Actions en cada push o pull request, ejecutando las pruebas y mostrando resultados en la pestaña Actions.

Archivo: .github/workflows/tests.yml

Badge:


🧩 Conclusión
Este proyecto demuestra la aplicación de un ciclo completo de desarrollo profesional:

Diseño orientado a objetos

Codificación limpia y modular

Pruebas unitarias e integración

Integración continua automatizada

El resultado es un sistema confiable, mantenible y completamente probado.

yaml
Copiar código

---

## ✅ 3️⃣ Opcional — incluir el diseño técnico (`docs/design.md`)

Puedes copiar este texto (ya adaptado a tu contexto):

```md
# Diseño del Sistema de Gestión de Tareas

## Arquitectura General
El sistema se diseñó bajo el patrón **Model-Manager**, donde:
- El modelo `Task` encapsula los datos y validaciones.
- El `TaskManager` actúa como capa de lógica de negocio.
- No se maneja persistencia (en memoria) para facilitar pruebas.

## Principios SOLID aplicados
- **S**ingle Responsibility: cada clase tiene una función clara.
- **O**pen/Closed: el sistema permite extender comportamientos sin modificar los existentes.
- **L**iskov Substitution: las funciones usan tipos base (enums, objetos) sin romper comportamiento.
- **I**nterface Segregation: métodos concisos y específicos.
- **D**ependency Inversion: dependencias explícitas, fáciles de simular en tests.

## Estrategia de Testing
- `test_task.py`: valida comportamientos unitarios de la clase Task.
- `test_manager.py`: prueba integración entre Task y TaskManager.
- `pytest-cov`: genera cobertura y reportes HTML/terminal.
