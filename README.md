### **HTML**

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simulador de Negociaciones Internacionales</title>
</head>
<body>
    <h1>Simulador de Negociaciones Internacionales</h1>
    <p>Este proyecto es una simulación de negociaciones entre dos países (EE.UU. y Ucrania o España) en las que cada parte tiene un nivel de confianza inicial y puede realizar varias acciones en cada ronda de negociación. Durante el proceso, una periodista aparece inesperadamente y hace preguntas aleatorias, lo que puede afectar el desarrollo de la negociación. El objetivo es explorar cómo las decisiones estratégicas, los compromisos y las tensiones pueden influir en las relaciones internacionales.</p>

    <h2>Características</h2>
    <ul>
        <li><strong>Partes involucradas</strong>: El simulador permite seleccionar entre EE.UU. y Ucrania o España como países negociadores.</li>
        <li><strong>Nivel de confianza</strong>: Cada parte comienza con un nivel de confianza entre 50 y 100, lo cual afecta las decisiones durante la negociación.</li>
        <li><strong>Acciones en cada ronda</strong>:
            <ul>
                <li>Aumentar exigencias (−5 puntos a la confianza de la otra parte).</li>
                <li>Llegar a un compromiso (+5 puntos a la confianza de la otra parte).</li>
                <li>Abandonar las negociaciones (termina el proceso de negociación).</li>
            </ul>
        </li>
        <li><strong>Intervención de la periodista</strong>: Durante la negociación, una periodista aparece inesperadamente para hacer preguntas sobre temas variados (política, economía, vestimenta, etc.).
            <ul>
                <li>Si las partes responden educadamente, la negociación continúa sin cambios.</li>
                <li>Si responden agresivamente, la confianza disminuye en 10 puntos.</li>
            </ul>
        </li>
        <li><strong>Condiciones de finalización</strong>:
            <ul>
                <li>Si una de las partes se retira.</li>
                <li>Si el nivel de confianza cae por debajo de 20.</li>
                <li>Si ambas partes superan un nivel de confianza de 80, alcanzando un acuerdo.</li>
            </ul>
        </li>
    </ul>

    <h2>Tecnologías Usadas</h2>
    <ul>
        <li><strong>Python</strong>: El simulador está implementado en Python, utilizando bibliotecas para manejar la interacción de las partes y mostrar los resultados de la negociación.</li>
        <li><strong>TextBlob</strong>: Para realizar análisis de texto y gestionar interacciones de las partes.</li>
        <li><strong>PrettyTable</strong>: Para visualizar el proceso de la negociación en formato tabular.</li>
        <li><strong>Deep_Translate</strong>: Para traducir las respuestas y preguntas si se requiere en otros idiomas.</li>
    </ul>

    <h2>Instalación</h2>
    <ol>
        <li>Clona este repositorio a tu máquina local:</li>
        <pre><code>git clone https://github.com/tu-usuario/negociaciones-internacionales.git</code></pre>
        <li>Navega al directorio del proyecto:</li>
        <pre><code>cd negociaciones-internacionales</code></pre>
        <li>Instala las dependencias necesarias:</li>
        <pre><code>pip install -r requirements.txt</code></pre>
    </ol>

    <h2>Uso</h2>
    <p>Para iniciar la simulación, simplemente ejecuta el siguiente comando:</p>
    <pre><code>python simulador.py</code></pre>
    <p>Durante la ejecución, el programa te guiará por el proceso de selección de países y mostrará los resultados de las negociaciones en formato de tabla. A medida que avance la negociación, verás cómo cambian los niveles de confianza entre las partes y cómo la intervención de la periodista afecta el desarrollo del proceso.</p>

    <h2>Ejemplo de Salida</h2>
    <p>Durante la simulación, se generará una tabla que muestra el estado actual de la negociación. Un ejemplo podría verse así:</p>
    <table border="1">
        <thead>
            <tr>
                <th>Ronda</th>
                <th>País 1</th>
                <th>Confianza País 1</th>
                <th>País 2</th>
                <th>Confianza País 2</th>
                <th>Acción País 1</th>
                <th>Acción País 2</th>
                <th>Confianza Total</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>EE.UU.</td>
                <td>75</td>
                <td>Ucrania</td>
                <td>65</td>
                <td>Compromiso</td>
                <td>Exigir más</td>
                <td>70</td>
            </tr>
            <tr>
                <td>2</td>
                <td>EE.UU.</td>
                <td>70</td>
                <td>Ucrania</td>
                <td>60</td>
                <td>Exigir más</td>
                <td>Compromiso</td>
                <td>65</td>
            </tr>
            <tr>
                <td>3</td>
                <td>EE.UU.</td>
                <td>60</td>
                <td>Ucrania</td>
                <td>50</td>
                <td>Abandonar</td>
                <td></td>
                <td>-</td>
            </tr>
        </tbody>
    </table>

    <h2>Contribuciones</h2>
    <p>Si deseas contribuir al proyecto, por favor sigue estos pasos:</p>
    <ol>
        <li>Haz un fork del repositorio.</li>
        <li>Crea una nueva rama para tu característica o arreglo de bug.</li>
        <li>Realiza tus cambios y prueba el código.</li>
        <li>Envía un pull request describiendo tus cambios.</li>
    </ol>

    <h2>Licencia</h2>
    <p>Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo <a href="LICENSE">LICENSE</a> para más detalles.</p>

    <hr>
    <p>¡Gracias por tu interés en este proyecto!</p>
</body>
</html>