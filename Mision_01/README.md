# Mision 1

## Tema 1. Tipos de aprendizaje
### Aprendizaje supervisado
El aprendizaje supervisado es como aprender con un maestro. En este enfoque, el modelo se entrena utilizando un conjunto de datos que incluye tanto las entradas (características) como las salidas correctas (etiquetas).
### Aprendizaje No Supervisado
Es como explorar un terreno sin mapa, el modelo se entrena con un conjunto de datos sin etiquetas y el objetivo es descubrir patrones ocultos dentro de los datos.
### Aprendizaje por refuerzo
Es como aprender por ensayo y error, el agente recibe recompensas o penalizaciones dependiendo de las decisiones que tome.

## Tema 2. Historia y ciclo de vida de un aprendizaje de maquina
El desarrollo de una aplicación de aprendizaje de máquina sigue un ciclo de vida estructurado que asegura que el modelo sea efectivo, preciso y útil. Para esto son necesarias varias etapas como: identificación del problema, recolección de datos, preparación de datos, ingeniería de modelos, evaluación del modelo, despliegue, mantenimiento y actualización.

## Tema 3. Identificacion del problema
La definición del objetivo es crucial para la identificación del problema, delimita el uso del aprendizaje de maquina y cuales son las metas especificas. El objetivo debe estar alineado con las necesidades, ser claro y medible.
- Aspectos clave
    - Disponibilidad de Datos.
    - Recursos y Herramientas.
    - Viabilidad Técnica.
    - Riesgos y Limitaciones.

## Tema 4. Recolección de datos
La recolección de los datos es una fase fundamental para el ciclo de vida del machine learning, ya que la calidad y cantidad de datos pueden determinar el éxito del modelo.
Existe multiples fuentes de datos, tales como:
- Datos Públicos: Bases de datos gubernamentales, organizaciones internacionales, y repositorios abiertos.
- Datos Privados: Datos internos de la empresa, registros históricos, datos transaccionales.
- Datos de Sensores: Información recopilada por sensores en plantas de energía, dispositivos IoT, satélites.
- Datos de Redes Sociales: Información extraída de plataformas como X, Facebook e Instagram.

Tipos de Bases de Datos:
- Bases de Datos Relacionales (SQL): MySQL, PostgreSQL, Oracle.
- Bases de Datos NoSQL: MongoDB, Cassandra, Redis.
- Data Warehouses: Amazon Redshift, Google BigQuery.
- Lakes de Datos: Apache Hadoop, Microsoft Azure Data Lake.

Cuando los datos reales son insuficientes o difíciles de obtener, la generación de datos sintéticos puede ser una alternativa útil.

## Tema 5. Visualizacion de datos
La visualización de datos es una herramienta esencial la cual permite entender, analizar y comunicar información compleja de una forma mas efectiva. Gracias a las gráfica y representaciones visuales que muestran tendencias y anomalías que no podrían ser vistas facilmente de otra manera.
Varios de los gráficos más utilizados son:
- Histogramas: son gráficos que muestran la distribución de un conjunto de datos continuos.
- Gráficos de cajas (box plots): son utilizados para mostrar la distribución de un conjunto de datos a través de sus cuartiles. Un gráfico de cajas muestra la mediana, los cuartiles, y los valores atípicos de un conjunto de datos
- Gráficos de densidad de kernel (KDE): son utilizados para estimar la densidad de probabilidad de una variable continua. A diferencia de los histogramas, los gráficos de densidad suavizan los datos y proporcionan una visualización más fluida de la distribución de los datos.

## Tema 6. Analisis exploratorio de datos
La calidad de los datos es crucial para desarrollar aplicaciones de aprendizaje de máquina efectivas. Exiten diferentes técnicas para la detección y tratamiento de datos ausentes, y la normalización de datos, los cuales ayudan a mejorar significativamente la calidad de estos.
1. Dimensiones de la calidad de datos
    - Completitud: Mide si todos los datos necesarios están presentes en el conjunto de datos.
    - Se refiere a la coherencia de los datos en todo el conjunto de datos. Que todos los datos estén en la misma unidad de medida, no es lo mismo mirar la potencia de paneles solares en kWh que en MWh.
    - Mide si los datos representan correctamente la realidad. Los datos deben ser exactos para poder hacer un modelo real.

2. Detección y tratamiento de datos ausentes
    - Media o Mediana: si algunos registros de eficiencia están ausentes, se puede reemplazar esos valores con la media o mediana de los registros disponibles para mantener el conjunto de datos utilizable.
    - Regresión: Se puede usar un modelo de regresion para predecir ciertas variables con el uso de otras que si estén presentes.
    - Hot Deck: En una encuesta, si algunos encuestados no proporcionaron información sobre su nivel de satisfacción, se puede imputar esos valores utilizando la información de encuestados con características similares (por ejemplo, en la misma ciudad).

3. Normalización de datos: Se neutraliza la desviación que generan ciertos rangos atipícos
    - Min-Max: escala de datos entre [0,1].
    - Robust: utiliza los valores de los cuartiles para reducir la distorsión de datos.

4. Ánalisis Univariado: El análisis univariable se centra en el estudio de una sola variable en un conjunto de datos. Se emplea para comprender la distribución, tendencia y dispersión de la variable en cuestión.

5. Análisis Bivariado: Correlación
Se enfoca en estudiar la relación entre dos variables para entender cómo una variable puede afectar o estar relacionada con otra. Uno de los métodos más comunes para llevar a cabo este análisis es la correlación.

6. Análisis Multivariado: Análisis de componentes principales (PCA)
El análisis multivariado se utiliza para entender relaciones entre múltiples variables y reducir la complejidad de los datos. Uno de los métodos más importantes en el análisis multivariado es el Análisis de Componentes Principales (PCA).