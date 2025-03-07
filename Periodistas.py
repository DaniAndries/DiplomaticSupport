import random
from logger_config import setup_logger
from deep_translator import GoogleTranslator
logger = setup_logger()
translator = GoogleTranslator(source="auto", target="en")

# Lista de periódicos
periodicos = [
    "El País", "El Mundo", "ABC", "La Vanguardia", "La Razón",
    "The New York Times", "The Guardian", "The Washington Post", "The Times", "The Wall Street Journal"
]

class Periodistas:
    # Constructor
    def __init__(self, nombre: str):
        self.nombre = nombre
    # "To-String"
    def __str__(self):
        return f"Somos {self.nombre}" 

    # Escoge un nombre de la lista de los periodicos
    @staticmethod   
    def escogerNombre():
        return periodicos.pop(random.randint(0, len(periodicos) - 1)) if periodicos else "Sin nombre"

    # Pide por teclado una pregunta y la devuelve traducida al ingles para que el TextBlop
    def hacerPregunta(self):
        pregunta = input(f"Pregunta de {self.nombre}: ")
        pregunta = translator.translate(pregunta)
        #pregunta = "How do you assess the progress of the project?"
        logger.info(f"{self.nombre} pregunta: {pregunta}")
        return pregunta
