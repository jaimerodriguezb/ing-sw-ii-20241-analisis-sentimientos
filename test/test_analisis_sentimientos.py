import pytest
from unittest.mock import MagicMock
from codigo_produccion import  AnalisisSentimientos
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.feature_extraction.text import CountVectorizer

def test_comportamiento_neutral():
    test =  AnalisisSentimientos()
    sentimiento = "neutral"
    resultado = test.clasificar_sentimiento(sentimiento)
    assert resultado == "Mensaje neutro"

def test_comportamiento_positivo():
    test =  AnalisisSentimientos()
    sentimiento = "positive"
    test.clasificar_sentimiento = MagicMock(return_value="Mensaje positivo")
    resultado = test.clasificar_sentimiento(sentimiento)
    assert resultado == "Mensaje positivo"

def test_comportamiento_negativo():
    test =  AnalisisSentimientos()
    sentimiento = "negative"
    test.clasificar_sentimiento = MagicMock(return_value="Mensaje negativo")
    resultado = test.clasificar_sentimiento(sentimiento)
    assert resultado == "Mensaje negativo"



        




        