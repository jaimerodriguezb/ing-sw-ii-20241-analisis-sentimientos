import pandas as pd
import numpy as np
import joblib
import os
from sklearn.feature_extraction.text import CountVectorizer

def _load_model(self):
    self.__model = joblib.load(os.path.dirname(__file__) + 'modelo/training/Tweets.csv')

vocabulary = {'oral': 6290, 'history': 4305, 'is': 4868, 'what': 9768}

def _funcion_prediccion(self, texto):
    texto_cv = CountVectorizer(vocabulary=vocabulary).transform([texto]).conjugate()
    toxicidad = self.__model.predict(texto_cv)[0]

    if toxicidad == "0":
        return "positive"
    elif toxicidad == "1":
        return "negative"
    else:
        return "neutro"

class AnalisisSentimientos():
    def _load_model(self):
        model_path = os.path.join(os.path.dirname(__file__) + 'modelo/training/Tweets.csv')
        return joblib.load(model_path)
    def _funcion_prediccion(self, texto):
        return _funcion_prediccion(self, texto)
    def clasificar_sentimiento(self, sentimiento):
       
        if sentimiento == "positive":
            return "Mensaje positivo"
        elif sentimiento == "negative":
            return "Mensaje negative"
        else:
            return "Mensaje neutro" 


analizador = AnalisisSentimientos()

resultado = analizador.clasificar_sentimiento("Hola, esto es un mensaje de prueba.")

print(resultado)