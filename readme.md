# Documentación del Proyecto: Servicio de Geolocalización

## Descripción General
Este proyecto es un programa en Python diseñado para realizar la geolocalización del equipo donde se encuentra instalado. No cuenta con una interfaz gráfica y funciona mediante la ejecución del archivo `serviceLocation.py` desde la consola.

Al ejecutarse, el programa obtiene la ubicación basada en la dirección IP, el nombre del equipo y la fecha y hora actuales, mostrando esta información en pantalla y registrándola en un archivo de log.

## Características Principales
1. **Obtención de información del equipo**:
   - Nombre del equipo mediante `socket.gethostname()`.
   - Ubicación basada en IP utilizando la biblioteca `geocoder`.
   - Fecha y hora del registro.

2. **Registro en archivo de log**:
   - La información se almacena en el archivo `logLocationPc.txt`.

3. **Ejecución continua**:
   - El programa consulta y registra la información cada 5 segundos.

## Prerrequisitos
1. Tener Python instalado (se recomienda Python 3.8 o superior).
2. Crear y activar un entorno virtual.

### Creación de un Entorno Virtual
```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

### Instalación de Dependencias
Asegúrate de tener el archivo `requirements.txt` en el mismo directorio que el script.

Ejecuta el siguiente comando para instalar las dependencias necesarias:
```bash
pip install -r requirements.txt
```

Contenido del archivo `requirements.txt`:
```
certifi==2023.7.22
charset-normalizer==3.2.0
click==8.1.7
colorama==0.4.6
decorator==5.1.1
future==0.18.3
geocoder==1.38.1
idna==3.4
ratelim==0.1.6
requests==2.31.0
schedule==1.2.0
six==1.16.0
urllib3==2.0.4
```

## Ejecución del Programa
Para ejecutar el programa, abre una terminal, navega al directorio del proyecto y utiliza el siguiente comando:
```bash
python serviceLocation.py
```

### Ejemplo de Salida
En consola:
```
Nombre de la Computadora: ERI
Ubicación: <[OK] Ipinfo - Geocode [Cuenca, Azuay, EC]> - Fecha y Hora: 2025-01-21 12:09:47.897739
```

En el archivo `logLocationPc.txt`:
```
Nombre de la Computadora: ERI
Ubicación: <[OK] Ipinfo - Geocode [Cuenca, Azuay, EC]> - Fecha y Hora: 2025-01-21 12:09:47.897739
```

## Detalles del Archivo `serviceLocation.py`

### Funcionalidades del Archivo
1. **Obtención de Ubicación**:
   - Utiliza la biblioteca `geocoder` para obtener información basada en la IP.
   - Maneja casos en los que no se puede obtener la ubicación.

2. **Información del Equipo**:
   - Obtiene el nombre del equipo mediante `socket.gethostname()`.

3. **Registro de Datos**:
   - Escribe en el archivo `logLocationPc.txt` la información del equipo, ubicación y fecha/hora.

4. **Ejecución Continua**:
   - Solicita información cada 5 segundos.

### Fragmento Principal del Código
```python
import geocoder
import time
import datetime
import socket

# OBTENER INFORMACION NECESARIA PARA EL LOG
def obtener_ubicacion():
    ubicacion = geocoder.ip('me')
    if ubicacion.ok:
        return ubicacion, datetime.datetime.now(), socket.gethostname()
    else:
        return "No se pudo obtener la ubicación.", None, None

if __name__ == "__main__":
    while True:
        ubicacion, fecha_hora, nombre_computadora = obtener_ubicacion()
        
        if ubicacion:
            print(f"Nombre de la Computadora: {nombre_computadora}")
            print(f"Ubicación: {ubicacion} - Fecha y Hora: {fecha_hora}")

            with open("logLocationPc.txt", "a") as archivo:
                archivo.write(f"Nombre de la Computadora: {nombre_computadora}\n")
                archivo.write(f"Ubicación: {ubicacion} - Fecha y Hora: {fecha_hora}\n\n")
        else:
            print("No se pudo obtener la ubicación.")
            with open("logLocationPc.txt", "a") as archivo:
                archivo.write("No se pudo obtener la ubicación.\n")
        
        # Espera 5 segundos antes de la siguiente solicitud
        time.sleep(5)
```

### Dependencias Principales
El script utiliza:
- `geocoder`: Para obtener la ubicación.
- `socket`: Para obtener el nombre del equipo.
- `datetime`: Para registrar la fecha y hora actual.

---

Si necesitas agregar más funcionalidades o realizar modificaciones, asegúrate de actualizar también esta documentación.

