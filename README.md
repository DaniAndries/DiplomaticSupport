# 🎮 **Simulador de Negociaciones Internacionales** 🌍

¡Bienvenido al **Simulador de Negociaciones Internacionales**! Este proyecto es una sofisticada herramienta de simulación diplomática que recrea negociaciones dinámicas entre dos países (EE.UU. y Ucrania o España). Cada nación comienza con un nivel de confianza inicial y debe tomar decisiones estratégicas en cada ronda de negociación. El elemento sorpresa: una **periodista** aparece inesperadamente con preguntas que pueden alterar significativamente el curso de las conversaciones. ¡Prepárate para sumergirte en un fascinante juego de estrategia, diplomacia y comunicación internacional! 🕹️🤝

<p align="center">
  <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzgxcmJ5a3NrbWh3d3ppZjF5Znc0cWszZDA1Zmo3ZWQyZm5saHU2biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qgQUggAC3Pfv687qPC/giphy.gif" alt="Simulación de negociación diplomática" width="300" height="200">
</p>

## ✨ **Características Principales**

- **Representación realista**: Simula negociaciones entre potencias globales (**EE.UU.**) y otros países (**Ucrania** o **España**) con dinámicas geopolíticas auténticas.
- **Sistema de confianza adaptativo**: Cada nación inicia con un nivel de confianza entre **50** y **100** puntos, que evoluciona orgánicamente según las decisiones tomadas.
- **Acciones estratégicas disponibles**:
  - 📈 **Aumentar exigencias**: Postura firme que reduce 5 puntos de confianza del oponente.
  - 🤝 **Llegar a un compromiso**: Enfoque colaborativo que aumenta 5 puntos de confianza del oponente.
  - 🚪 **Abandonar las negociaciones**: Movimiento definitivo que concluye el proceso diplomático.
- **Factor periodístico disruptivo**: Una periodista interviene con preguntas sorpresa sobre temas diversos:
  - ✅ Respuestas diplomáticas: Mantienen el curso de la negociación sin alteraciones.
  - ❌ Respuestas agresivas: Provocan una caída significativa de 10 puntos en la confianza bilateral.
- **Múltiples escenarios de conclusión**:
  - Retirada unilateral de una de las partes
  - Crisis de confianza (nivel inferior a **20**)
  - Acuerdo exitoso (ambas partes superan **80** puntos de confianza)

## 🛠️ **Stack Tecnológico**

- **Python**: Motor principal del simulador con arquitectura modular y escalable
- **TextBlob**: Análisis de sentimiento avanzado para evaluar respuestas diplomáticas
- **PrettyTable**: Visualización elegante de datos en formato tabular para seguimiento de negociaciones
- **Deep_Translate**: Capacidades multilingües para simulaciones internacionales auténticas

## 💻 **Guía de Instalación**

```bash
# 1. Clona el repositorio
git clone https://github.com/DaniAndries/DiplomaticSupport.git

# 2. Navega al directorio
cd DiplomaticSupport

# 3. Configura un entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 4. Instala dependencias
pip install -r requirements.txt
```

## 🚀 **Instrucciones de Uso**

Para iniciar la simulación:

```bash
python app.py
```

La interfaz te guiará paso a paso en la configuración de:
1. Selección de países participantes
2. Configuración de niveles iniciales de confianza (o uso de valores predeterminados)
3. Desarrollo de rondas de negociación con toma de decisiones interactiva

## 📊 **Visualización de Resultados**

Durante la simulación, se genera una tabla dinámica que muestra el progreso de las negociaciones:

| Ronda | País 1 | Confianza País 1 | País 2  | Confianza País 2 | Acción País 1 | Acción País 2 |
|-------|--------|------------------|---------|------------------|---------------|---------------|
| 1     | EE.UU. | 75               | Ucrania | 65               | Ceder         | Exigencia     |
| 2     | EE.UU. | 70               | Ucrania | 70               | Exigencia     | Ceder         |
| 3     | EE.UU. | 65               | Ucrania | 75               | Ceder         | Ceder         |
| 4     | EE.UU. | 70               | Ucrania | 80               | Ceder         | Ceder         |
| 5     | EE.UU. | 75               | Ucrania | 85               | Ceder         | Ceder         |

### 🎭 **Escenario de intervención periodística:**

```
🎙️ Periodista: "¿Qué opinan sobre las recientes declaraciones de su contraparte sobre política comercial?"

🇺🇸 EE.UU.: "Respetamos sus opiniones aunque diferimos en algunos puntos. Estamos aquí para encontrar terreno común."
🇺🇦 Ucrania: "¡Sus declaraciones son inaceptables y demuestran mala fe en estas negociaciones!"

📉 La confianza de EE.UU. hacia Ucrania disminuye en 10 puntos debido a la respuesta agresiva.
```

## 🔍 **Casos de Uso Educativos**

- **Estudios de Relaciones Internacionales**: Herramienta práctica para comprender dinámicas diplomáticas
- **Formación en Negociación**: Entrenamiento en técnicas de mediación y resolución de conflictos
- **Análisis de Comunicación**: Estudio del impacto de diferentes estilos comunicativos en resultados diplomáticos

## 👥 **Contribuciones**

¡Valoramos tus contribuciones para mejorar este simulador! Para participar:

1. Haz un **fork** del repositorio
2. Crea una **rama** para tu característica (`git checkout -b feature/nueva-funcionalidad`)
3. Implementa tus cambios y añade pruebas unitarias
4. Envía un **pull request** detallado con descripción de las mejoras

### Áreas de mejora sugeridas:
- Ampliación de países disponibles
- Implementación de eventos aleatorios adicionales
- Mejoras en la interfaz gráfica
- Exportación de resultados en formatos adicionales

## 🤝 Colaboradores
Este proyecto ha sido desarrollado en colaboración con:

- [joseangel109](https://github.com/joseangel109)
- [DaniAndries](https://github.com/DaniAndries)

## 📄 **Licencia**

Este proyecto está licenciado bajo la **Licencia MIT** - consulta el archivo [LICENSE](LICENSE) para más detalles.

---

### 🌟 ¡Gracias por participar en esta experiencia diplomática virtual! 🤝🌍
