# Informe de salida

## Resumen Ejecutivo

Este informe describe los resultados del proyecto de deep learning y presenta los principales logros y lecciones aprendidas durante el proceso.

## Resultados del proyecto

- Resumen de los entregables y logros alcanzados en cada etapa del proyecto.

## 1. Fase 1: Business Understanding
Se realizo el entendimiento del negocio para el proyecto, el objetivo principal era construir un modelo CNN que clasificara si un paciente tiene un tumor en el riñon o no basandose en una resonancia magnetica, con lo cual se utilizo un conjunto de datos de imagenes de resonancias magneticas adecuadas para entrenar, validar y probar un modelo CNN que puediera clasificar las imagenes de los pacientes. Se utilizo la arquitectura y pesos del modelo VGG-16 para este problema binario.

Logros alcanzados en la etapa:
Utilizar inicialmente la metodología TDSP (Team Data Science Project) para definir el entendimiento del negocio, conocer el problema objetivo a solucionar, el cronograma y alcance de ejecución del proyecto.

## 2. Fase 2: Data Ingestion
El dataset original se obtuvo desde kaggle [Kidney Dataset](https://www.kaggle.com/datasets/nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone) el cual contiene conjuntos de datos de imagenes de resonancias magneticas de riñones de los pacientes en 4 folders segun el tipo de diagnostico, se cuenta inicialmente con un archivo comprimido "CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone.zip" el cual se compone de 4 folders y un total de 12.4k imagenes, sin embargo por practicidad y temas de capacidad de computo, se opta por escoger unicamente los folders nombrados Normal y Tumor, y de estos seleccionar al azar aproximadamente 200 imagenes para cada uno, dichos folders almacenan respectivamente las imagenes de las resonancias si tiene o no tumor.

El dataset final escogido se comprimio en un archivo .zip y se alojo en la nube de Google Drive para posterior poder descargargo con ayuda de la libreria gdown, esto con el fin de no incurrir en costos de almacenamiento en alguna nube como por ejemplo storage accounts en Azure o almacenamiento S3 en AWS.

La variable objetivo principal de este problema de clasificación es la clase de si tiene o no tumor (YES/NO), una variable categorica.

Imagen con clasificación "normal" sin tumor:
![normal](https://github.com/Katherin07/tdsp_dl_project_kidney_disease_classification/blob/master/images/normal.jpg)

Imagen con clasificación "tumor" con tumor:
![tumor](https://github.com/Katherin07/tdsp_dl_project_kidney_disease_classification/blob/master/images/tumor.jpg)

Logros alcanzados en la etapa:
Crear un pipeline para la ingestión de la data en un folder nombrado artifacts, en la cual se descarga el dataset desde Google Drive con ayuda de la libreria gdown, se descomprime y se aloja en folder artifacts/data_ingestion/kidney-ct-scan-image en una estructura de subfolders "Normal" y "Tumor" para cada imagen respectivamente.


## 3. Fase 3: Preprocessing, training, modeling and evaluation

Para resolver este problema de vision por computador se utilizara la arquitectura y los pesos del modelo VGG-16 para entrenar el modelo para resolver este problema de clasificación binaria. Se utilizara la técnica de **_Transfer Learning_**, la cual es una técnica comúnmente usada para entrenar redes neuronales de forma más rápida y con resultados más precisos, basándose en modelos previamente construidos y entrenados en tareas similares.  El modelo VGG-16 utiliza una arquitectura de redes convolucionales muy profundas para el reconocimiento de imágenes a gran escala, se usa para casos de uso de clasificación de imágenes, asi como para casos de uso de **_Transfer Learning_** y **_Fine Tuning_**.

Adicional se debe tener en cuenta que el tamaño de entrada predeterminado para este modelo es 224x224. Cada aplicación Keras espera un tipo específico de preprocesamiento de entrada.

A continuación imagen de arquitectura del modelo VGG16:

![arqmodelo3](https://github.com/Katherin07/tdsp_dl_project_kidney_disease_classification/blob/master/images/vgg.png)

Para el preprocesamiento se uso la tecnica de data augmentation con ayuda de la libreria ImageDataGenerator de tensorflow, para el entrenamiento los parametros se ajustaron en el archivo params.yaml y la evaluación del modelo se realizo con ayuda de la plataforma Dagshub la cual es una plataforma de colaboración utilizada para el versionado de datos, código y modelos de ML basada en Git, en dicha plataforma se creo el repo conectado desde la cuenta de Github y en experimentación se creo una URI para MLFlow.

![dagshub](https://github.com/Katherin07/tdsp_dl_project_kidney_disease_classification/blob/master/images/dagshub.png)

En la siguiente imagen se puede observar que se ejecutaron 11 versiones del modelo con ayuda de MLFLow:

![evaluationmodel](https://github.com/Katherin07/tdsp_dl_project_kidney_disease_classification/blob/master/images/mlflow_evaluation.png)

![compare](https://github.com/Katherin07/tdsp_dl_project_kidney_disease_classification/blob/master/images/mlflow_compare.png)

Se aprovecho la capacidad de transferencia de aprendizaje de VGG16, e iterando el parametro de cantidad de épocas con un valor de 5 se logro obtener un accuracy del 95% lo cual es un gran desempeño, este modelo se envio a producción con la versión 11:

![bestmodel](https://github.com/Katherin07/tdsp_dl_project_kidney_disease_classification/blob/master/images/best_model.png)

Para lograr disminuir los tiempo de experimentación y de evaluación se crearon pipelines de orquestación para la ejecución de cada una de las etapas, y se utilizo la herramienta DVC  para hacer el seguimiento del data pipeline con ayuda del archivo dvc.yaml que contiene el flujo de ejecución de los pipelines:

![datapipeline](https://github.com/Katherin07/tdsp_dl_project_kidney_disease_classification/blob/master/images/data_pipeline.png)

Logros alcanzados en la etapa:
- Crear pipelines de orquestación para la ejecución de cada una de las etapas de preprocesamiento, entrenamiento, modelamiento y evaluación del modelo, logrando con el ajuste de hiperparametros un accuracy del 95%.
- Utilizar nuevas herramientas como por ejemplo Dagshub para la experimentación y evaluación de los modelos, asi como MLFlow y herramientas para versionar el codigo como Github, adicional utilizar la herramienta DVC para el seguimieto del data pipeline.

## 4. Fase 4: Deployment

- **Diagrama de arquitectura:** A continuación imagen que muestra la arquitectura del sistema que se utilizará para desplegar el modelo:

![arq](https://github.com/Katherin07/tdsp_dl_project_kidney_disease_classification/blob/master/images/arq.png)

El producto final del proyecto es una aplicación construida con Flask para aplicar este modelo final y lograr la predicción de tumor de riñon en imagenes de resonancia magnetica,la cual se desplego en la plataforma de AWS por medio de un flujo de CI CD con ayuda de Github actions, las instrucciones del despliegue se pueden encontrar en docs/deployment.

Finalmente la aplicación se visualiza de la siguiente manera:

![appaws](https://github.com/Katherin07/tdsp_dl_project_kidney_disease_classification/blob/master/images/app_aws_deployed.png)

Donde el usuario podra cargar la imagen de la resonancia magnetica de riñon dando clic en el boton "Upload" y obtener la predicción dando clic en el boton "Predict", el resultado de la preducción se observara a la derecha en el panel "Prediction Results" en una respuesta en formato json.

Logros alcanzados en la etapa:
- Desplegar la solución en una plataforma en la nube, en este caso AWS implementando CI CD con ayuda de docker y github actions para automatizar este proceso.
- Implementar una aplicación construida con Flask para aplicar este modelo final y lograr la predicción de tumor de riñon en imagenes de resonancia magnetica.

## Lecciones aprendidas

- Identificación de los principales desafíos y obstáculos encontrados durante el proyecto:

-Se identifico como un desafio la capacidad de recursos de computo, debido a esto se opto por reducir el tamaño del dataset a aproximadamente 400 imagenes.
-Lograr estructurar un paquete src para gestionar la interacción entre los modulos y finalmente tener una orquestación de pipelines para lograr la ejecución de cada una de las etapas de ingestión del dataset, preprocesamiento, entrenamiento, modelamiento, evaluación del modelo y despliegue.
-Implementar github actions y configurar los servicios requeridos en AWS para el despliegue.


- Lecciones aprendidas en relación al manejo de los datos, el modelamiento y la implementación del modelo:

-Para lograr una mejor clasificación se puede optar por incrementar el tamaño del dataset e incluir mas modelos de cnn a evaluar.
-Se aprovecho la capacidad de transferencia de aprendizaje de VGG16, e iterando el parametro de cantidad de épocas con un valor de 5 se logro obtener un accuracy del 95% lo cual es un gran desempeño.
-Se podria experimentar con diferentes valores para hiperparámetros clave como la tasa de aprendizaje, el tamaño del lote y la cantidad de épocas. Ajustar estos parámetros puede tener un impacto significativo en el rendimiento del modelo.
-Se podria considera el uso de técnicas de regularización como la disminución de la tasa de aprendizaje o el dropout para evitar el sobreajuste.
-Se opto por implementar técnicas de aumento de datos para generar variedad en el conjunto de entrenamiento. Esto puede ayudar a mejorar la generalización del modelo y reducir el riesgo de sobreajuste.


- Recomendaciones para futuros proyectos de machine learning:

-Seria interesante visualizar las activaciones de las capas intermedias del modelo para comprender qué características están aprendiendo las diferentes capas. Esto puede ayudar a depurar y entender el comportamiento del modelo.
-Se recomienda experimentar con otras arquitecturas de modelos (por ejemplo, modelos más recientes como ResNet, Inception, o EfficientNet) para comparar el rendimiento y ver si alguna de ellas se adapta mejor.
-Seria interesante validar otras plataformas o herramientas para implementar despliegues y mejorar el MLOps.

## Impacto del proyecto

- Descripción del impacto del modelo en el negocio o en la industria:

Esta aplicación podria ayudar a tener un impacto significativo en el sector de la salud y la medicina de las siguientes maneras:

-Mejora en el Diagnóstico Temprano:
El modelo proporciona la capacidad de detectar la presencia de tumores renales en una etapa temprana, lo que permite a los profesionales de la salud intervenir rápidamente para iniciar tratamientos y mejorar las tasas de éxito en la recuperación.

-Reducción de Errores Humanos:
Al utilizar inteligencia artificial para la clasificación de imágenes, se reduce la probabilidad de errores humanos en la interpretación de imágenes médicas. Esto contribuye a una mayor precisión en el diagnóstico.

-Optimización de Recursos Médicos:
La detección automática de tumores renales puede optimizar la asignación de recursos médicos al priorizar casos de mayor urgencia. Esto puede conducir a una gestión más eficiente de la carga de trabajo y tiempos de respuesta más rápidos para los pacientes.

-Impacto en la Planificación del Tratamiento:
La información proporcionada por el modelo puede influir en la planificación del tratamiento al proporcionar a los médicos datos más precisos sobre la naturaleza y la ubicación de los tumores renales. Esto permite desarrollar estrategias de tratamiento más personalizadas.

-Reducción de Costos de Atención Médica:
La detección temprana y la intervención rápida pueden reducir los costos asociados con tratamientos más prolongados y complejos. Además, la disminución de la necesidad de pruebas y procedimientos repetitivos puede contribuir a la eficiencia y la reducción de costos.

- Identificación de las áreas de mejora y oportunidades de desarrollo futuras:

-Mejora en la Diversidad de Datos:
Para garantizar la robustez del modelo, se puede trabajar en mejorar la diversidad del conjunto de datos. Asegurarse de que el modelo haya sido entrenado en imágenes que representen diversas características demográficas y clínicas de la población mejorará su generalización.

-Integración con Sistemas de Historia Clínica Electrónica (HCE):
Integrar el modelo con sistemas de Historia Clínica Electrónica permitiría una colaboración más estrecha con otros datos clínicos del paciente. Esto podría proporcionar un contexto más completo y ayudar en la toma de decisiones médicas.

-Desarrollo de Herramientas de Interpretación:
Crear herramientas de interpretación que expliquen las predicciones del modelo de manera comprensible para los profesionales de la salud podría aumentar la confianza en la adopción del modelo. La transparencia y la interpretabilidad son cruciales en entornos clínicos.

-Enfoque en la Privacidad y la Ética:
Continuar desarrollando prácticas y protocolos que garanticen la privacidad del paciente y cumplan con las normativas éticas y legales en el ámbito de la salud. Esto es especialmente relevante al tratar con datos médicos sensibles.

-Validación Clínica y Colaboración con Profesionales de la Salud:
Realizar validaciones clínicas adicionales y colaborar estrechamente con profesionales de la salud para recopilar retroalimentación sobre la eficacia del modelo en situaciones del mundo real. Esta colaboración puede llevar a mejoras continuas y adaptaciones del modelo.

-Desarrollo de Capacidades de Predicción a Largo Plazo:
Explorar oportunidades para el desarrollo de capacidades predictivas a largo plazo, como la identificación de pacientes en riesgo de desarrollar tumores renales en el futuro. Esto podría contribuir a estrategias preventivas más efectivas.

## Conclusiones

- Se aprovecho la capacidad de transferencia de aprendizaje de VGG16, e iterando el parametro de cantidad de épocas con un valor de 5 se logro obtener un accuracy del 95% lo cual es un gran desempeño.
- Se podria experimentar con diferentes valores para hiperparámetros clave como la tasa de aprendizaje, el tamaño del lote y la cantidad de épocas. Ajustar estos parámetros puede tener un impacto significativo en el rendimiento del modelo.
- Seria interesante visualizar las activaciones de las capas intermedias del modelo para comprender qué características están aprendiendo las diferentes capas. Esto puede ayudar a depurar y entender el comportamiento del modelo.
- Se podria considera el uso de técnicas de regularización como la disminución de la tasa de aprendizaje o el dropout para evitar el sobreajuste.
- Se opto por implementar técnicas de aumento de datos para generar variedad en el conjunto de entrenamiento. Esto puede ayudar a mejorar la generalización del modelo y reducir el riesgo de sobreajuste.
- Se recomienda experimentar con otras arquitecturas de modelos (por ejemplo, modelos más recientes como ResNet, Inception, o EfficientNet) para comparar el rendimiento y ver si alguna de ellas se adapta mejor.
- Se aprovecho el uso de plataformas para MLOps como Github, DVC, MLFLow, Dagshub, y adicional se evaluaron servicios de AWS para despliegue del proyecto.

## Referencias

En esta sección se deben incluir las referencias bibliográficas y fuentes de información utilizadas en el desarrollo del modelo.

Proyecto de referencia: https://github.com/krishnaik06/Kidney-Disease-Classification-Deep-Learning-Project

## Agradecimientos

- Agradecimientos a los docentes y equipo en general del diplomado en Machine Learning and Data Science Avanzado que con sus enseñanzas hicieron posible para mi la ejecución de este proyecto.
