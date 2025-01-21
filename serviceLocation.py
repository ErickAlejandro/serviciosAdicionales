import geocoder
import time
import datetime
import socket
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import schedule
import os

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
