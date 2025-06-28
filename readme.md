# TP Ingeniería de datos 2

Este proyecto utiliza Docker y Python para levantar y explorar tres bases de datos: **MySQL**, **MongoDB** y **Neo4j**, todas inicializadas automáticamente con datos de ejemplo.

---

## 📦 Requisitos

- Docker + Docker Compose
- Python 3.10+ y [Poetry](https://python-poetry.org/)

---

## 🚀 Cómo levantar todo

### 1. Levantar las bases de datos con Docker

```bash
docker-compose up -d
```

Esto levanta:
- **MySQL** (con `init.sql`)
- **MongoDB** (con `init.js`)
- **Neo4j** (requiere carga manual del script `.cypher` si se desea)

---

### 2. Instalar dependencias de Python con Poetry

```bash
poetry install
```

Esto instalará las dependencias declaradas en `pyproject.toml`.

---

### 3. Ejecutar Jupyter Notebook (o simplemente correrlo local usando el entorno de poetry)

```bash
poetry run jupyter notebook
```

Esto abrirá Jupyter en el navegador. Desde ahí, podés abrir el notebook:

```
notebooks/review.ipynb
```

Este notebook permite verificar que los datos fueron cargados correctamente en las tres bases.

---

## 🔁 Inicialización de datos en Neo4j

Neo4j no ejecuta automáticamente el archivo `init.cypher`, pero podés cargarlo fácilmente con el siguiente comando:

```bash
poetry run python init/neo4j/init_neo.py
```

Este script se conecta a Neo4j, ejecuta todos los comandos del archivo Cypher y luego imprime un resumen con la cantidad de nodos y relaciones cargadas.

---

## 📁 Estructura del proyecto

```
init/
├── mysql/init.sql
├── mongo/init.js
└── neo4j/init.cypher

notebooks/
└── exploracion.ipynb

pyproject.toml
docker-compose.yml
```