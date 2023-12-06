# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline.

## Descripción del modelo

El modelo baseline es el primer modelo construido y se utiliza para establecer una línea base para el rendimiento de los modelos posteriores:

Para resolver este problema de vision por computador se utilizara la arquitectura y los pesos del modelo VGG-16 para entrenar el modelo para resolver este problema de clasificación binaria. Se utilizara la técnica de **_Transfer Learning_**, la cual es una técnica comúnmente usada para entrenar redes neuronales de forma más rápida y con resultados más precisos, basándose en modelos previamente construidos y entrenados en tareas similares.  El modelo VGG-16 utiliza una arquitectura de redes convolucionales muy profundas para el reconocimiento de imágenes a gran escala, se usa para casos de uso de clasificación de imágenes, asi como para casos de uso de **_Transfer Learning_** y **_Fine Tuning_**.

Adicional se debe tener en cuenta que el tamaño de entrada predeterminado para este modelo es 224x224. Cada aplicación Keras espera un tipo específico de preprocesamiento de entrada.

A continuación imagen de arquitectura del modelo VGG16:

![arqmodelo2](https://github.com/Katherin07/tdsp_dl_project_kidney_disease_classification/blob/master/images/vgg.png)

## Variables de entrada

Lista de las variables de entrada utilizadas en el modelo:

Se pueden encontrar en los archivos config.yaml y param.yaml.

## Variable objetivo

Nombre de la variable objetivo utilizada en el modelo:

El resultado de la predicción del modelo en base a el desempeño del modelo medido bajo metricas como accuracy y loss.

## Evaluación del modelo

### Métricas de evaluación

Descripción de las métricas utilizadas para evaluar el rendimiento del modelo:

Accuracy: Exactitud del modelo en la predicción.


### Resultados de evaluación

Tabla que muestra los resultados de evaluación del modelo baseline, incluyendo las métricas de evaluación:

En la siguiente imagen se puede observar que se ejecutaron 11 versiones del modelo con ayuda de MLFLow:

![evaluationmodel](https://github.com/Katherin07/tdsp_dl_project_kidney_disease_classification/blob/master/images/mlflow_evaluation.png)

## Análisis de los resultados

Descripción de los resultados del modelo baseline, incluyendo fortalezas y debilidades del modelo:

Recordemos que el modelo baseline es VGG16 (Visual Geometry Group 16) con una arquitectura de red neuronal convolucional (CNN):

Fortalezas:
- Efectivo para tareas generales de visión por computadora.
- Arquitectura simple y fácil de entender, la arquitectura VGG16 tiene capas convolucionales y capas totalmente conectadas que son fáciles de entender y visualizar.
- Se puede utilizar para la transferencia de aprendizaje.

Debilidades:
- Pesado en términos de recursos computacionales, VGG16 tiene un gran número de parámetros (alrededor de 138 millones), lo que puede hacer que sea costoso en términos de recursos computacionales y memoria. Esto puede ser un desafío en entornos con recursos limitados.
- Propenso a sobreajuste (overfitting), dado su tamaño y complejidad, VGG16 puede ser propensa al sobreajuste, especialmente si se utiliza en conjuntos de datos más pequeños. Se pueden requerir técnicas adicionales, como la regularización, para abordar este problema.
- Problemas con objetos pequeños, debido a las numerosas capas de pooling, VGG16 puede tener dificultades para manejar objetos pequeños en imágenes. Pueden perderse detalles finos en la representación.
- Requiere grandes conjuntos de datos para entrenamiento desde cero.

## Conclusiones

Conclusiones generales sobre el rendimiento del modelo baseline y posibles áreas de mejora.

- Se aprovecho la capacidad de transferencia de aprendizaje de VGG16, e iterando el parametro de cantidad de épocas con un valor de 5 se logro obtener un accuracy del 95% lo cual es un gran desempeño.
- Se podria experimentar con diferentes valores para hiperparámetros clave como la tasa de aprendizaje, el tamaño del lote y la cantidad de épocas. Ajustar estos parámetros puede tener un impacto significativo en el rendimiento del modelo.
- Seria interesante visualizar las activaciones de las capas intermedias del modelo para comprender qué características están aprendiendo las diferentes capas. Esto puede ayudar a depurar y entender el comportamiento del modelo.
- Se podria considera el uso de técnicas de regularización como la disminución de la tasa de aprendizaje o el dropout para evitar el sobreajuste.
- Se opto por implementar técnicas de aumento de datos para generar variedad en el conjunto de entrenamiento. Esto puede ayudar a mejorar la generalización del modelo y reducir el riesgo de sobreajuste.
- Una mejora seria experimentar con otras arquitecturas de modelos (por ejemplo, modelos más recientes como ResNet, Inception, o EfficientNet) para comparar el rendimiento y ver si alguna de ellas se adapta mejor.


## Referencias

Lista de referencias utilizadas para construir el modelo baseline y evaluar su rendimiento.

Proyecto de referencia: https://github.com/krishnaik06/Kidney-Disease-Classification-Deep-Learning-Project
