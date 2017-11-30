#!/usr/bin/python
# -*- coding: utf-8 -*-

# Enviar correo Gmail con Python

import smtplib

fromaddr = 'tucorreo@gmail.com'
toaddrs  = 'destino@gmail.com'
msg = 'Correo enviado utilizano Python + smtplib'


# Datos
username = 'tucorreo@gmail.com'
password = 'contraseña'

# Enviando el correo
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()