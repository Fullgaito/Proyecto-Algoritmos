# Proyecto de Análisis y Diseño de Algoritmos

## Algoritmos Implementados

Este proyecto implementa y compara diferentes algoritmos para resolver el problema de la suma de subconjuntos. Los algoritmos evaluados son:

1. **Divide y vencerás**
2. **Fuerza bruta**
3. **Programación dinámica**
4. **Backtracking**

## Requisitos

Antes de ejecutar los algoritmos, asegúrate de tener instalado **Python 3.8 o superior**. También es recomendable crear un entorno virtual para manejar las dependencias.

## Instalación

Sigue estos pasos para instalar las dependencias necesarias:

1. **Clonar el repositorio**

   ```sh
   git clone https://github.com/usuario/proyecto-algoritmos.git
   cd proyecto-algoritmos
   ```

2. **Crear y activar un entorno virtual (opcional, pero recomendado)**

   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar las dependencias**

   ```sh
   pip install -r requirements.txt
   ```

## Ejecución de los algoritmos

Cada algoritmo tiene su propio script dentro de la carpeta `algoritmos`. Puedes ejecutarlos de la siguiente manera:

- **Divide y vencerás**

  ```sh
  python algoritmos/divide_y_venceras.py
  ```

- **Fuerza bruta**

  ```sh
  python algoritmos/fuerza_bruta.py
  ```

- **Programación dinámica**

  ```sh
  python algoritmos/programacion_dinamica.py
  ```

- **Backtracking**

  ```sh
  python algoritmos/backtracking.py
  ```

## Pruebas y Benchmarking

Para ejecutar pruebas de rendimiento y comparar la eficiencia de los algoritmos, utiliza el siguiente comando:

```sh
python benchmark.py
```

Este script medirá el tiempo de ejecución y el consumo de memoria de cada algoritmo con diferentes tamaños de entrada.

## Entorno de Pruebas

Los algoritmos han sido probados en los siguientes entornos:

- **Sistema Operativo:** Ubuntu 22.04, Windows 10, macOS Monterey
- **Python:** 3.10.6
- **Procesador:** Intel i7 / AMD Ryzen 7
- **RAM:** 16GB

## Contacto

Para preguntas o colaboración en el proyecto, puedes abrir un **Issue** en el repositorio o contactarnos a los correos jfajardob@unal.edu.co y sgaitanq@unal.edu.co

---

**Licencia:** Este proyecto se distribuye bajo la licencia MIT.
