import random, time
from textblob import TextBlob
from participante import Participante
from periodistas import Periodistas
from negociaciones import Negociaciones
from deep_translator import GoogleTranslator
from prettytable.colortable import ColorTable, Themes
import nltk

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

translator = GoogleTranslator(source="auto", target="es")
import logger as R 
R.Logger("logs")

# Para crear la prettytable
table = ColorTable(theme = Themes.HIGH_CONTRAST)
# table.field_names = ["Nombre", "Confianza"]
table.field_names = [
    "Ronda", "País 1", "Confianza País 1", "País 2", "Confianza País 2",
    "Acción País 1", "Acción País 2"
]

table.align["Ronda"] = "c"
table.align["País 1"] = "c"
table.align["Confianza País 1"] = "c"
table.align["País 2"] = "c"
table.align["Confianza País 2"] = "c"
table.align["Acción País 1"] = "c"
table.align["Acción País 2"] = "c"

accion1 = ""
accion2 = ""

# def actualizar_tabla(pais: str, confianza: float):
#     for i, row in enumerate(table._rows):
#         if row[0] == pais:  # Si el país ya existe, actualiza la confianza
#             table._rows[i] = [pais, confianza]
#             return
#     table.add_row([pais, confianza])

def actualizar_tabla(ronda, pais1: Participante ,pais2: Participante):
    table.add_row([
        ronda+1, pais1.pais, pais1.confianza, pais2.pais, pais2.confianza, pais1.accion, pais2.accion
    ])

# Funcion principal del programa
def main():
    R.info("--------------------------Iniciando programa--------------------------")    
    iniciar_negociaciones()

# Se crean la "reunion"
def iniciar_negociaciones():
    R.info("Inicializando Pais 1")   
    rondas = -1
    # Se crean los dos paises
    pais1 = Participante(Participante.iniciarPaises(), Participante.confianzaPaises(), "")
    #print(pais1)
    R.info("Inicializando Pais 2")
    pais2 = Participante(Participante.iniciarPaises(), Participante.confianzaPaises(), "")
    #print(pais2)
    
    actualizar_tabla(rondas, pais1, pais2)
    rondas += 1
    try:
        # Durante 4 vueltas no se van a hacer preguntas
        for i in range(4):
            if (pais1.confianza > 80 and pais2.confianza > 80) or (pais1.confianza < 20 or pais2.confianza < 20):
                print(table)
                raise Warning("Confianza máxima alcanzada, acuerdo completado")

            negociaciones(pais1, pais2, False, i)
            rondas +=1
            time.sleep(1)

        R.info("A partir de ahora responderemos a las posibles preguntas y al final de cada reunión")
        # Se hacen negociaciones con preguntas en bucle hasta que ambos superen 80 de confianza o alguno se retire
        while (pais1.confianza < 80 and pais2.confianza < 80) or (pais1.confianza > 20 or pais2.confianza > 20):
            negociaciones(pais1, pais2, True, rondas)
            rondas+=1
            time.sleep(1)
    except Warning as warning:
        R.info(warning)    
    R.logging("-------------------------Finalizando Programa-------------------------")
# Se hace que cada pais aleatoriamente haga una accion aleatoria
def negociaciones(pais1: Participante, pais2: Participante, preguntas: bool, rondas):
    try:
        elegirPais = random.randrange(2)
        if elegirPais == 0:
            tomar_acciones(pais1, pais2)
        else:
            tomar_acciones(pais2, pais1)
        numero = random.randint(1, 100)
        # Hacemos que si las preguntas estan activadas tengan un 20% de posibilidad de que se hagan preguntas de los periodistas
        if numero < 50 and preguntas:
            entrevista(pais1, pais2)
        actualizar_tabla(rondas, pais1, pais2)
        pais1.accion=""
        pais2.accion=""
        print(table)
    except Warning as warning:
        raise warning

# Se hacen 3 apartados con numeros aleatorios
def tomar_acciones(paisAtacante:Participante, paisAtacado:Participante):
    accion = random.randint(0, 101)
    try:
        # En el primer bloque de numeros se hara exigir
        if accion < 50:
            Negociaciones.exigir(paisAtacado)
            R.info(f"{paisAtacante.pais} ha hecho una exigencia y {paisAtacado.pais} pierde confianza ahora tiene {paisAtacado.confianza}")
            paisAtacante.accion = Negociaciones.accionPais
        # En el segundo se hara ceder 
        elif accion > 50 and accion < 99:
            Negociaciones.ceder(paisAtacado)
            R.info(f"{paisAtacante.pais} ha cedido ante una exigencia y {paisAtacado.pais} gana confianza ahora tiene {paisAtacado.confianza}")
            print()
            paisAtacante.accion = Negociaciones.accionPais
            #print(accion1)
        # En el ultimo salir que es el que menos porcentaje de salir tiene
        else:
            #Se retira de las negociaciones y finaliza el programa
            paisAtacante.confianza = 0
            R.info(f"{paisAtacante.pais} ha salido y pierde toda su confianza ahora tiene {paisAtacante.confianza}")
            print(table)
            Negociaciones.salir(paisAtacante)
    except Warning as warning:
        raise warning

# Para ver a que pais van dirigidas las preguntas
def entrevista(pais1: Participante, pais2: Participante):   
    try:
        listaPaises = [pais1, pais2]
        # Escoge de la lista de paises 1 pais para hacerle la pregunta
        dirigirPregunta = random.choice(listaPaises)
        responder(dirigirPregunta)
    except Warning as warning:
        raise warning 

# El pais responde las preguntas
def responder(pais : Participante):
    try:
        # Guardamos en una variable la respuesta que nos da
        respuesta = pais.responder_a_pregunta(periodistas().hacerPregunta())
        R.info(f"{pais.pais} responde: {respuesta}")
        # Mostramos la respuesta traducida al español, ya que textoblop las analiza en ingles
        print(f"{pais.pais} responde: {translator.translate(respuesta)}")
        connotacion = TextBlob(respuesta).sentiment.polarity
        # Si la respuesta es agresiva
        if connotacion < 0:
            Negociaciones.agresivo(pais)
            #print(pais.confianza)
    except Warning as warning:
        raise warning

# Crea los periodistas con un nombre
def periodistas():
    return Periodistas(Periodistas.escogerNombre())

# Lanzar el programa
if __name__ == "__main__":
    main()
