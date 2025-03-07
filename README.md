# 🎮 **README - Simulador de Negociaciones Internacionales** 🌍

¡Bienvenido al **Simulador de Negociaciones Internacionales**! Este proyecto es una simulación de negociaciones entre dos países (EE.UU. y Ucrania o España). Cada parte tiene un nivel de confianza inicial y puede realizar diversas acciones en cada ronda de negociación. Durante el proceso, una **periodista** aparece inesperadamente y hace preguntas aleatorias, lo que puede influir en el desarrollo de la negociación. ¡Prepárate para sumergirte en un juego de estrategia y diplomacia! 🕹️🤝

<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzgxcmJ5a3NrbWh3d3ppZjF5Znc0cWszZDA1Zmo3ZWQyZm5saHU2biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qgQUggAC3Pfv687qPC/giphy.gif" alt="Imagen simulación" width="300" height="200" style="display: block; margin-left: auto; margin-right: auto;">

## **Características** 📜

- **Partes involucradas**: El simulador permite seleccionar entre **EE.UU.** y **Ucrania** o **España** como países negociadores.
- **Nivel de confianza**: Cada parte comienza con un nivel de confianza entre **50** y **100**, lo cual afecta las decisiones durante la negociación.
- **Acciones en cada ronda**:
  - **Aumentar exigencias** (−5 puntos a la confianza de la otra parte).
  - **Llegar a un compromiso** (+5 puntos a la confianza de la otra parte).
  - **Abandonar las negociaciones** (termina el proceso de negociación).
- **Intervención de la periodista**: Durante la negociación, una periodista aparece inesperadamente para hacer preguntas sobre temas variados (política, economía, vestimenta, etc.).
  - Si las partes responden educadamente, la negociación continúa sin cambios.
  - Si responden agresivamente, la confianza disminuye en **10 puntos**.
- **Condiciones de finalización**:
  - Si una de las partes se retira.
  - Si el nivel de confianza cae por debajo de **20**.
  - Si ambas partes superan un nivel de confianza de **80**, alcanzando un acuerdo.

## **Tecnologías Usadas** 🔧

- **Python**: El simulador está implementado en **Python**, utilizando bibliotecas para manejar la interacción de las partes y mostrar los resultados de la negociación.
- **TextBlob**: Para realizar análisis de texto y gestionar interacciones de las partes.
- **PrettyTable**: Para visualizar el proceso de la negociación en formato tabular.
- **Deep_Translate**: Para traducir las respuestas y preguntas si se requiere en otros idiomas.

## **Instalación** ⚙️

1. **Clona este repositorio** a tu máquina local.

2. **Navega al directorio** del proyecto.

3. **Instala las dependencias** necesarias.

## **Uso** 🕹️

Para iniciar la simulación, simplemente ejecuta el siguiente comando:

Durante la ejecución, el programa te guiará por el proceso de selección de países y mostrará los resultados de las negociaciones en formato de tabla. A medida que avance la negociación, verás cómo cambian los niveles de confianza entre las partes y cómo la intervención de la periodista afecta el desarrollo del proceso.

## **Ejemplo de Salida** 📊

Durante la simulación, se generará una tabla que muestra el estado actual de la negociación. Un ejemplo podría verse así:

| Ronda | País 1 | Confianza País 1 | País 2  | Confianza País 2 | Acción País 1 | Acción País 2 | Confianza Total |
|-------|--------|------------------|---------|------------------|---------------|---------------|-----------------|
| 1     | EE.UU. | 75               | Ucrania | 65               | Compromiso    | Exigir más    | 70              |
| 2     | EE.UU. | 70               | Ucrania | 60               | Exigir más    | Compromiso    | 65              |
| 3     | EE.UU. | 60               | Ucrania | 50               | Abandonar     |               | -               |

Si la periodista interviene:

- **Pregunta**: "¿Qué opinan sobre la vestimenta del otro?"
- Si uno de los países responde **agresivamente**, la confianza disminuiría en **10 puntos**.

## **Contribuciones** ✨

¡Te invitamos a contribuir al proyecto! Si deseas hacerlo, sigue estos pasos:

1. Haz un **fork** del repositorio.
2. Crea una nueva **rama** para tu característica o arreglo de bug.
3. Realiza tus cambios y prueba el código.
4. Envía un **pull request** describiendo tus cambios.

## **Licencia** 📄

Este proyecto está licenciado bajo la **Licencia MIT** - consulta el archivo [LICENSE](LICENSE) para más detalles.

---

### ¡Gracias por participar en la simulación! 🤝🌍
