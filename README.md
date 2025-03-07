# README - Simulador de Negociaciones Internacionales

Este proyecto es una simulación de negociaciones entre dos países (EE.UU. y Ucrania o España) en las que cada parte tiene un nivel de confianza inicial y puede realizar varias acciones en cada ronda de negociación. Durante el proceso, una periodista aparece inesperadamente y hace preguntas aleatorias, lo que puede afectar el desarrollo de la negociación. El objetivo es explorar cómo las decisiones estratégicas, los compromisos y las tensiones pueden influir en las relaciones internacionales.

## **Características**

- **Partes involucradas**: El simulador permite seleccionar entre EE.UU. y Ucrania o España como países negociadores.
- **Nivel de confianza**: Cada parte comienza con un nivel de confianza entre 50 y 100, lo cual afecta las decisiones durante la negociación.
- **Acciones en cada ronda**:
  - Aumentar exigencias (−5 puntos a la confianza de la otra parte).
  - Llegar a un compromiso (+5 puntos a la confianza de la otra parte).
  - Abandonar las negociaciones (termina el proceso de negociación).
- **Intervención de la periodista**: Durante la negociación, una periodista aparece inesperadamente para hacer preguntas sobre temas variados (política, economía, vestimenta, etc.).
  - Si las partes responden educadamente, la negociación continúa sin cambios.
  - Si responden agresivamente, la confianza disminuye en 10 puntos.
- **Condiciones de finalización**:
  - Si una de las partes se retira.
  - Si el nivel de confianza cae por debajo de 20.
  - Si ambas partes superan un nivel de confianza de 80, alcanzando un acuerdo.
  
## **Tecnologías Usadas**

- **Python**: El simulador está implementado en Python, utilizando bibliotecas para manejar la interacción de las partes y mostrar los resultados de la negociación.
- **TextBlob**: Para realizar análisis de texto y gestionar interacciones de las partes.
- **PrettyTable**: Para visualizar el proceso de la negociación en formato tabular.
- **Deep_Translate**: Para traducir las respuestas y preguntas si se requiere en otros idiomas.

## **Instalación**

1. Clona este repositorio a tu máquina local:

```bash
git clone https://github.com/tu-usuario/negociaciones-internacionales.git
Navega al directorio del proyecto:
bash
Copiar
Editar
cd negociaciones-internacionales
Instala las dependencias necesarias:
bash
Copiar
Editar
pip install -r requirements.txt
Uso
Para iniciar la simulación, simplemente ejecuta el siguiente comando:

bash
Copiar
Editar
python simulador.py
Durante la ejecución, el programa te guiará por el proceso de selección de países y mostrará los resultados de las negociaciones en formato de tabla. A medida que avance la negociación, verás cómo cambian los niveles de confianza entre las partes y cómo la intervención de la periodista afecta el desarrollo del proceso.

Ejemplo de Salida
Durante la simulación, se generará una tabla que muestra el estado actual de la negociación. Un ejemplo podría verse así:

Ronda	País 1	Confianza País 1	País 2	Confianza País 2	Acción País 1	Acción País 2	Confianza Total
1	EE.UU.	75	Ucrania	65	Compromiso	Exigir más	70
2	EE.UU.	70	Ucrania	60	Exigir más	Compromiso	65
3	EE.UU.	60	Ucrania	50	Abandonar		-
Si la periodista interviene:

Pregunta: "¿Qué opinan sobre la vestimenta del otro?"
Si uno de los países responde agresivamente, la confianza disminuiría.
Contribuciones
Si deseas contribuir al proyecto, por favor sigue estos pasos:

Haz un fork del repositorio.
Crea una nueva rama para tu característica o arreglo de bug.
Realiza tus cambios y prueba el código.
Envía un pull request describiendo tus cambios.
Licencia
Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.