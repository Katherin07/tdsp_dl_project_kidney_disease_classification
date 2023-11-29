# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline.

## Descripción del modelo

El modelo baseline es el primer modelo construido y se utiliza para establecer una línea base para el rendimiento de los modelos posteriores:

Para resolver este problema de vision por computador se utilizara la arquitectura y los pesos del modelo VGG-16 para entrenar el modelo para resolver este problema de clasificación binaria. Se utilizara la técnica de **_Transfer Learning_**, la cual es una técnica comúnmente usada para entrenar redes neuronales de forma más rápida y con resultados más precisos, basándose en modelos previamente construidos y entrenados en tareas similares.  El modelo VGG-16 utiliza una arquitectura de redes convolucionales muy profundas para el reconocimiento de imágenes a gran escala, se usa para casos de uso de clasificación de imágenes, asi como para casos de uso de **_Transfer Learning_** y **_Fine Tuning_**.

Adicional se debe tener en cuenta que el tamaño de entrada predeterminado para este modelo es 224x224. Cada aplicación Keras espera un tipo específico de preprocesamiento de entrada.

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

A partir de esta punto hacia abajo los resultados del modelo en cuanto a evaluación se especificaran mejor en la proxima entrega, ya que se hizo una primera ealuación egenral, se requieren hacer mas ejecuciones y seguimiento de los parametros en mlflow para tener un resumen mas completo de los resultados de evaluación.

### Resultados de evaluación

Tabla que muestra los resultados de evaluación del modelo baseline, incluyendo las métricas de evaluación.

## Análisis de los resultados

Descripción de los resultados del modelo baseline, incluyendo fortalezas y debilidades del modelo.

## Conclusiones

Conclusiones generales sobre el rendimiento del modelo baseline y posibles áreas de mejora.

## Referencias

Lista de referencias utilizadas para construir el modelo baseline y evaluar su rendimiento.

Proyecto de referencia: https://github.com/krishnaik06/Kidney-Disease-Classification-Deep-Learning-Project
