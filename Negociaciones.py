import Participante

# Acciones posibles
#     Exigir -5
#     Salir  0
#     Ceder   +5
#     Agresivo -10

class Negociaciones ():
    
    # Exigir quita 5 de confianza y en caso de ser menor del minimo se lanza una excepcion controlada
    def exigir(participante: Participante):
        participante.confianza -= 5
        if participante.confianza < 20:
            Negociaciones.salir(participante)
            raise Warning("Confianza demasiado baja")
        
    # Ceder gana 5 de confianza y en caso de ser mayor al maximo se lanza una excepcion controlada
    def ceder(participante: Participante):
        participante.confianza += 5
        if participante.confianza > 100:
            raise Warning("Confianza maxima")
        
    # En caso de que la respuesta del pais a la pregunta de los periodistas sea agresiva se quitaran 10 de confianza al pais
    def agresivo(participante: Participante):
        participante.confianza -= 10
        if participante.confianza < 20:
            raise Warning("Confianza demasiado baja")

    # Se retira un pais de las negociaciones y se termina la ejecucion
    def salir(participante: Participante):
        exit(0)
    