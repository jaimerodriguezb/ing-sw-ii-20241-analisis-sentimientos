import pytest
from unittest.mock import MagicMock
from modelo.codigo_produccion import  AnalisisSentimientos
import pandas as pd
import pip

def test_comportamiento_neutral(mocker):
    test =  AnalisisSentimientos()
    mocker.patch('modelo.codigo_produccion.AnalisisSentimientos.clasificar_sentimiento',return_value="Mensaje neutro")
    resultado = test.clasificar_sentimiento()
    assert resultado == "Mensaje neutro"

def test_comportamiento_positivo():
    test =  AnalisisSentimientos()
    test.clasificar_sentimiento = MagicMock(return_value="Mensaje positivo")
    resultado = test.clasificar_sentimiento()
    assert resultado == "Mensaje positivo"

def test_comportamiento_negativo():
    test =  AnalisisSentimientos()
    test.clasificar_sentimiento = MagicMock(return_value="Mensaje negativo")
    resultado = test.clasificar_sentimiento()
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


#modelor
def test_comportamiento_negativo_modelo (negative_text):
    test =  AnalisisSentimientos()
    resultado = test.clasificar_sentimiento(negative_text  )
    assert resultado == "Mensaje negative"

#modelor
def test_comportamiento_positivo_modelo (positive_text):
    test =  AnalisisSentimientos()
    resultado = test.clasificar_sentimiento( positive_text )
    assert resultado == "Mensaje positivo"