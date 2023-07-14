# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from telegram.error import NetworkError, Unauthorized
from time import sleep
import logging
import telegram
from PRUEBA import traducir
update_id = None
comandoocupado = False

token = "inserta tu token aquí" 

def main():
    global update_id
    bot = telegram.Bot(token)
    
    try: 
        update_id = bot.get_updates()[0].update_id
    except IndexError: 
        update_id = None
        
    logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    while True: 
        try: 
            echo(bot)
        except  NetworkError: 
            sleep(1)
        except Unauthorized:
            update_id += 1
            
def echo(bot):
    global update_id 
    global comandoocupado
    
    saludos = ["Hola", "Hello", "Good morning"]
    
    
    for update in bot.get_updates(offset = update_id, timeout = 10):
        update_id = update.update_id+1
        if update.message: 
            if comandoocupado: 
                if comandoocupado == 1:
                    comandoocupado = 0
                    traduccion = traducir("es",update.message.text)
                    update.message.reply_text(traduccion)
                if comandoocupado == 2:
                    comandoocupado = 0
                    traduccion = traducir("en",update.message.text)
                    update.message.reply_text(traduccion)
            else: 
            
                #update.message.reply_text(update.message.text)
                if update.message.text == "/traduciresp":
                     comandoocupado = 1
                     update.message.reply_text("Por favor ingrese el texto en inglés que desee traducir :D")
                elif update.message.text == "/traduciren":
                     comandoocupado = 2
                     update.message.reply_text("Please enter your text in Spanish :D")
                elif update.message.text in saludos:
                    update.message.reply_text("Hola ¿En qué puedo ayudarte? \nHello, how can I help you?")
                else:
                     comandoocupado = 0
                     update.message.reply_text("Usted ha ingresado un comando incorrecto. Pruebe una de las siguientes opciones: \n/traduciresp \n/traduciren")
                           
    
    
if __name__ == '__main__': 
    main()
