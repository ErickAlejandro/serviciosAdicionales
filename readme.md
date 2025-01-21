# Documentación del Proyecto: Servicio de Geolocalización

## Descripción General
Este proyecto es un programa sencillo en Python cuyo objetivo principal es realizar la geolocalización del equipo en el que se encuentra instalado. El programa obtiene y muestra la ubicación basada en la IP del dispositivo, así como el nombre del equipo y la fecha y hora actual.

### Ejecución del Programa
El programa no cuenta con una interfaz de usuario. Se ejecuta desde la terminal utilizando el siguiente comando:
```bash
python serviceLocation.py
```
Al ejecutarse, el programa muestra un mensaje similar al siguiente:
```
Nombre de la Computadora: ERI
Ubicación: <[OK] Ipinfo - Geocode [Cuenca, Azuay, EC]> - Fecha y Hora: 2025-01-21 12:09:47.897739
```

---

## Prerrequisitos

### 1. Instalación de Python
- Asegúrate de tener Python (versión 3.8 o superior) instalado en tu sistema.
- Descárgalo desde [python.org](https://www.python.org/) si no lo tienes instalado.

### 2. Configuración del Entorno Virtual
Es recomendable utilizar un entorno virtual para manejar las dependencias del proyecto.

1. **Crear el Entorno Virtual:**
   - Navega al directorio del proyecto en la terminal.
   - Ejecuta el siguiente comando:
     ```bash
     python -m venv venv
     ```

2. **Activar el Entorno Virtual:**
   - En **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - En **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Actualizar `pip`:**
   - Asegúrate de tener la última versión de `pip`:
     ```bash
     pip install --upgrade pip
     ```

### 3. Instalación de Dependencias

El proyecto utiliza algunas bibliotecas externas que deben ser instaladas mediante el archivo `requirements.txt`. Sigue estos pasos:

1. **Archivo `requirements.txt`:**
   Asegúrate de que el archivo contenga lo siguiente:
   ```
   requests
   ```

2. **Instalar las Dependencias:**
   Con el entorno virtual activado, ejecuta:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verificar la Instalación:**
   - Para confirmar que las bibliotecas se instalaron correctamente, puedes listar los paquetes instalados:
     ```bash
     pip freeze
     ```

---

## Estructura del Proyecto
El proyecto contiene los siguientes archivos principales:

1. **`serviceLocation.py`:**
   - Es el archivo principal del programa.
   - Contiene la lógica para obtener el nombre del equipo, la ubicación basada en la IP y la fecha y hora actual.

2. **`requirements.txt`:**
   - Archivo de dependencias necesarias para el programa.

---

## Ejecución Paso a Paso
1. Clona o descarga el proyecto en tu sistema.
2. Configura y activa un entorno virtual.
3. Instala las dependencias usando `requirements.txt`.
4. Ejecuta el programa desde la terminal:
   ```bash
   python serviceLocation.py
   ```
5. Visualiza la información de geolocalización y otros detalles en la consola.

---

## Notas Adicionales
- **API Utilizada:** El programa utiliza el servicio de [Ipinfo.io](https://ipinfo.io/) para obtener la información de geolocalización.
- **Módulos Incluidos:** El código incluye módulos integrados de Python para obtener el nombre del equipo y la fecha y hora actual.

