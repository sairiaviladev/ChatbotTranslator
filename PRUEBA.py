# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:52:53 2021

@author: sairi
"""
def traducir (target, text, model = "nmt"):
    import six 
    from google.cloud import translate_v2 as translate 
    translate_client = translate.Client()
    if isinstance(text,six.binary_type):
        text = text.decode("uts-8")
    result = translate_client.translate(text, target_language = target, model = model)
  #  print(u"text {}".format(result ["input"]))
    return (u"{}".format(result["translatedText"]))
    
  
 
    
"""
from googletrans import Translator

texto = "hola"  
traductor = Translator()
print(traductor.translate(texto,src='es',dest='en'))
"""

#import os

#os.environ['GOOGLE_APPLICATION_CREDENTIALS']= "C:/Users/sairi/OneDrive/Documentos/PYTHON/SairiESL-ded24Ecbb353.json"
#print(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])