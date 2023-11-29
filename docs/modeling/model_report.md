# Reporte del Modelo Final

## Resumen Ejecutivo

En esta sección se presentará un resumen de los resultados obtenidos del modelo final. Es importante incluir los resultados de las métricas de evaluación y la interpretación de los mismos.

## Descripción del Problema

Se utilizara una solución basada en redes neuronales convolucionales para visión por computador, buscando clasificar de manera correcta las imagenes de resonancia magnetica de los pacientes, evaluando el modelo con varias capas de neuronas y segun varias metricas de desempeño, usando transfer learning  utilizando la arquitectura y los pesos del modelo VGG-16 para entrenar el modelo para este problema binario.

## Descripción del Modelo

Para resolver este problema de vision por computador se utilizara la arquitectura y los pesos del modelo VGG-16 para entrenar el modelo para resolver este problema de clasificación binaria. Se utilizara la técnica de **_Transfer Learning_**, la cual es una técnica comúnmente usada para entrenar redes neuronales de forma más rápida y con resultados más precisos, basándose en modelos previamente construidos y entrenados en tareas similares.  El modelo VGG-16 utiliza una arquitectura de redes convolucionales muy profundas para el reconocimiento de imágenes a gran escala, se usa para casos de uso de clasificación de imágenes, asi como para casos de uso de **_Transfer Learning_** y **_Fine Tuning_**.

Adicional se debe tener en cuenta que el tamaño de entrada predeterminado para este modelo es 224x224. Cada aplicación Keras espera un tipo específico de preprocesamiento de entrada.

## Evaluación del Modelo

En esta sección se presentará una evaluación detallada del modelo final. Se deben incluir las métricas de evaluación que se utilizaron y una interpretación detallada de los resultados.

Por el momento puede evaluar las tecnicas de evaluación en el archivo src/cnnClassifier/evaluation/model_evaluation_mlflow.py

Por el momento aun se encuentra trabajando en las conclusiones ya que se deben realizar mas experimentos.

## Conclusiones y Recomendaciones

En esta sección se presentarán las conclusiones y recomendaciones a partir de los resultados obtenidos. Se deben incluir los puntos fuertes y débiles del modelo, las limitaciones y los posibles escenarios de aplicación.

## Referencias

En esta sección se deben incluir las referencias bibliográficas y fuentes de información utilizadas en el desarrollo del modelo.

Proyecto de referencia: https://github.com/krishnaik06/Kidney-Disease-Classification-Deep-Learning-Project
