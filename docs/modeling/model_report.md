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

En la siguiente imagen se puede observar que se ejecutaron 11 versiones del modelo con ayuda de MLFLow:

![evaluationmodel](https://github.com/Katherin07/tdsp_dl_project_kidney_disease_classification/blob/master/images/mlflow_evaluation.png)

Se aprovecho la capacidad de transferencia de aprendizaje de VGG16, e iterando el parametro de cantidad de épocas con un valor de 5 se logro obtener un accuracy del 95% lo cual es un gran desempeño, con se envio a producción la v11 del modelo:
![bestmodel](https://github.com/Katherin07/tdsp_dl_project_kidney_disease_classification/blob/master/images/best_model.png)

## Conclusiones y Recomendaciones

- Se aprovecho la capacidad de transferencia de aprendizaje de VGG16, e iterando el parametro de cantidad de épocas con un valor de 5 se logro obtener un accuracy del 95% lo cual es un gran desempeño.
- Se podria experimentar con diferentes valores para hiperparámetros clave como la tasa de aprendizaje, el tamaño del lote y la cantidad de épocas. Ajustar estos parámetros puede tener un impacto significativo en el rendimiento del modelo.
- Seria interesante visualizar las activaciones de las capas intermedias del modelo para comprender qué características están aprendiendo las diferentes capas. Esto puede ayudar a depurar y entender el comportamiento del modelo.
- Se podria considera el uso de técnicas de regularización como la disminución de la tasa de aprendizaje o el dropout para evitar el sobreajuste.
- Se opto por implementar técnicas de aumento de datos para generar variedad en el conjunto de entrenamiento. Esto puede ayudar a mejorar la generalización del modelo y reducir el riesgo de sobreajuste.
- Se recomienda experimentar con otras arquitecturas de modelos (por ejemplo, modelos más recientes como ResNet, Inception, o EfficientNet) para comparar el rendimiento y ver si alguna de ellas se adapta mejor.

## Referencias

En esta sección se deben incluir las referencias bibliográficas y fuentes de información utilizadas en el desarrollo del modelo.

Proyecto de referencia: https://github.com/krishnaik06/Kidney-Disease-Classification-Deep-Learning-Project
