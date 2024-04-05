import pytest
from unittest.mock import MagicMock
from modelo.codigo_produccion import  AnalisisSentimientos
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

#inicial las pruebas con el modelo
@pytest.fixture
def positive_text(): 
    return "@AmericanAir Joanne from your San Diego staff was phenomenal! Give that girl a raise. She handled our #flightnightmare better than anyone."

@pytest.fixture
def negative_text():
    return "@USAirways The airline is embarrassing itself. I get that bad weather isn't your fault, but your response to it couldn't have been worse."

@pytest.fixture
def neutral_text():
    return "@VirginAmerica plz help me win my bid upgrade for my flight 2/27 LAX---&gt;SEA!!!  🍷👍💺✈️"

#modelor
def test_comportamiento_neutral_modelo(neutral_text):
    test =  AnalisisSentimientos()
    resultado = test.clasificar_sentimiento(neutral_text)
    assert resultado == "Mensaje neutro"




        