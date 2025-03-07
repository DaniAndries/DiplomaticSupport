import random, json
from entrenamiento import entrenamiento 
from logger_config import setup_logger
logger = setup_logger()

clasificador = entrenamiento()

listaPaises = ["EEUU", "Spain", "Ukraine"]

class Participante:
    # Constructor
    def __init__(self, pais: str, confianza: float):
        self.pais = pais
        self.confianza = confianza

    # "To-String"
    def __str__(self):
        return f"Pais: {self.pais}, Confianza: {self.confianza}"
    
    # Asignamos un número aleatorio entre 50 y 100 para la confianza 
    @staticmethod
    def confianzaPaises():
        return random.randint(40, 70)

    # Sacamos aleatoriamente un país de la lista y lo borramos para que no se repita
    @staticmethod
    def iniciarPaises():
        if listaPaises:
            return listaPaises.pop(random.randint(0, len(listaPaises) - 1))
        return "Sin país"
    
    # Elige una respuesta con sentido
    @staticmethod
    def responder_a_pregunta(pregunta):
        categoria = clasificador.classify(pregunta)
        
        return obtener_respuesta(categoria) or "I don't know what to say."

# Coge la respuesta del JSON donde estan todas las respuestas posibles y analiza si son respuestas educadas o agresivas 
def obtener_respuesta(categoria):
    with open("respuestas.json", "r", encoding="utf-8") as respuestas:
        archivo = json.load(respuestas)
    respuestas = archivo.get(categoria, {})
    if not respuestas:
        return f"There isn't response for {categoria}."
    
    respuestas_cordiales = respuestas.get("polite_response", [])
    respuestas_agresivas = respuestas.get("aggressive_response", [])
    
    if not respuestas_cordiales and not respuestas_agresivas:
        return f"There isn't response for {categoria}."

    opciones = []
    
    if respuestas_cordiales:
        opciones.append(random.choice(respuestas_cordiales))
    if respuestas_agresivas:
        opciones.append(random.choice(respuestas_agresivas))
    
    return random.choice(opciones)
