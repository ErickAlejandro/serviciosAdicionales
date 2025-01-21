import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Configura los detalles del correo electrónico
remitente = "ishida.desarrollo@ishidasoftwarecue.com"  # Reemplaza con tu dirección de correo
contraseña = "ckmx pwoh utan ddxr"       # Reemplaza con tu contraseña
destinatario = "erick2000ayala@gmail.com"  # Reemplaza con la dirección de correo del destinatario

# Configura el archivo que deseas enviar
archivo_adjunto = "logLocationPc.txt"  # Reemplaza con la ruta de tu archivo

while True:
    try:
        msg = MIMEMultipart()
        msg['From'] = remitente
        msg['To'] = destinatario
        msg['Subject'] = "Archivo Adjunto"

        # Cuerpo del correo
        cuerpo_correo = "Adjunto se encuentra el archivo que solicitaste."
        msg.attach(MIMEText(cuerpo_correo, 'plain'))

        # Adjunta el archivo
        archivo = open(archivo_adjunto, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((archivo).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename=archivo.txt")
        msg.attach(part)

        # Envía el correo electrónico
        servidor_smtp = smtplib.SMTP('smtp.gmail.com', 587)
        servidor_smtp.starttls()
        servidor_smtp.login(remitente, contraseña)
        texto = msg.as_string()
        servidor_smtp.sendmail(remitente, destinatario, texto)
        servidor_smtp.quit()

        print("Correo enviado satisfactoriamente.")
    except Exception as e:
        print(f"Error al enviar el correo: {str(e)}")

    # Espera 20 segundos antes del siguiente envío
    time.sleep(20)
