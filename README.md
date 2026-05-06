# ⚙ TENGEN TOPPA GURREN LAGANN — Mi Primera Página Web con Reflex

> *"¡Cree en mí que cree en ti!"* — Kamina

Proyecto académico: Primera aplicación web desarrollada con **Reflex** y **Poetry**, usando únicamente Python, con temática del anime **Tengen Toppa Gurren Lagann**.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Reflex](https://img.shields.io/badge/Reflex-0.9.1-orange)
![Poetry](https://img.shields.io/badge/Poetry-2.0-cyan)
![GitHub](https://img.shields.io/badge/GitHub-Publico-black?logo=github)

---

## 📺 Descripción

Aplicación web con estética oscura inspirada en Gurren Lagann. Incluye:

- 🔴 Título principal con el nombre del anime
- ✅ Texto de bienvenida con descripción del proyecto
- ⚡ Botón interactivo que rota frases icónicas de Kamina con contador de clics
- 👤 Selector de personajes — Simon, Kamina, Yoko, Nia, Viral
- 👁 Zona de spoilers con toggle para mostrar/ocultar

---

## 🛠️ Tecnologías usadas

| Herramienta | Versión | Para qué se usa |
|---|---|---|
| Python | 3.11.x | Lenguaje de programación |
| Reflex | 0.9.1 | Framework web full-stack en Python |
| Poetry | 2.0.x | Gestor de dependencias moderno |
| Node.js | 18 LTS | Requerido internamente por Reflex |
| Git | 2.x | Control de versiones |

---

## 🚀 Instalación paso a paso

### Requisitos previos

Antes de empezar instala estas herramientas:

- **Python 3.11** → [python.org](https://python.org) ⚠️ No uses 3.9 ni 3.14 — Reflex requiere >=3.10,<4.0
- **Node.js 18 LTS** → [nodejs.org](https://nodejs.org)
- **Poetry** → gestor de dependencias (instrucciones abajo)
- **Git** → [git-scm.com](https://git-scm.com)

---

### Paso 1 — Instala Poetry

```powershell
# Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

```bash
# macOS / Linux
curl -sSL https://install.python-poetry.org | python3 -
```

Cierra y vuelve a abrir la terminal. Verifica:
```bash
poetry --version
```

---

### Paso 2 — Clona el repositorio

```bash
git clone https://github.com/TU_USUARIO/gurren-lagann-reflex.git
cd gurren-lagann-reflex
```

---

### Paso 3 — Instala las dependencias con Poetry

```bash
poetry install
```

Poetry lee el `pyproject.toml` y el `poetry.lock` e instala exactamente las mismas versiones. No necesitas crear el entorno virtual manualmente — Poetry lo hace solo.

---

### Paso 4 — Inicializa Reflex

```bash
poetry run reflex init
```

> ⚠️ En Poetry 2.0 ya no existe `poetry shell`. Usa siempre `poetry run` como prefijo.

Elige la opción **0 (blank)** si te pregunta por una plantilla.

---

### Paso 5 — Ejecuta la aplicación

```bash
poetry run reflex run
```

La primera vez puede tardar 2-3 minutos descargando dependencias de frontend.

---

### Paso 6 — Abre en el navegador

```
http://localhost:3000
```

Para detener la app: `Ctrl + C` en la terminal.

---

## 📁 Estructura del proyecto

```
gurren-lagann-reflex/
│
├── gurren_reflex/
│   └── gurren_reflex.py     # Código principal — State + componentes UI
│
├── pyproject.toml           # Dependencias gestionadas por Poetry
├── poetry.lock              # Versiones exactas (no editar)
├── rxconfig.py              # Configuración de Reflex
└── README.md                # Este archivo
```

---

## 🧩 Comandos útiles con Poetry 2.0

| Acción | Comando |
|---|---|
| Instalar dependencias | `poetry install` |
| Agregar una librería | `poetry add nombre-libreria` |
| Ejecutar Reflex | `poetry run reflex run` |
| Inicializar Reflex | `poetry run reflex init` |
| Ver entorno virtual | `poetry env info` |
| Ejecutar cualquier script | `poetry run python script.py` |

> **Nota:** En Poetry 2.0 el comando `poetry shell` fue eliminado. Usa `poetry run` como prefijo en su lugar.

---

## ⚠️ Problemas comunes

**Error: Python version incompatible**
```
reflex requires Python <4.0,>=3.10
```
Solución: Instala Python 3.11 y ejecuta `poetry env use python3.11`

**Error: poetry shell no disponible**
```
Looks like you're trying to use a Poetry command that is not available
```
Solución: Usa `poetry run reflex run` en lugar de activar el entorno.

**Error: ModuleNotFoundError**
```
Module mi_primera_web.mi_primera_web not found
```
Solución: Verifica que `app_name` en `rxconfig.py` coincida exactamente con el nombre de la carpeta y el archivo `.py`.

---

## 🎨 Paleta de colores

| Color | Hex | Uso |
|---|---|---|
| Rojo Kamina | `#FF4500` | Títulos, bordes, acentos |
| Dorado | `#FFD700` | Subtítulos, nombres de personajes |
| Negro profundo | `#050505` | Fondo principal |

---

## 👤 Autor

Proyecto desarrollado como ejercicio académico para la asignatura de Desarrollo Web.

*"¡Quien diablos crees que soy!"* — este proyecto fue hecho con determinación digna de Equipo Gurren.

---

## 📄 Licencia

MIT — libre como el espíritu del Equipo Gurren.
