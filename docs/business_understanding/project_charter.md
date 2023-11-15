# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Deep Learning Project Kidney Disease Classification

## Objetivo del Proyecto

El proyecto tiene como objetivo principal construir un modelo CNN que clasificara si un paciente tiene un tumor en el riñon o no basandose en una resonancia magnetica. Para lograr esto, se utilizaran conjuntos de datos de imagenes de resonancias magneticas adecuadas para entrenar, validar y probar un modelo CNN que pueda clasificar las imagenes de los pacientes. Se utilizara la arquitectura y pesos del modelo VGG-16 para entrenar el modelo para este problema binario.

## Alcance del Proyecto

### Incluye:

- Se dispone de un conjunto de datos de imagenes de resonancias magneticas de pacientes, donde se tienen dos folder segun la clasificación si tiene tumor la imagen o no.
- Se espera clasificar si un paciente tiene un tumor en el riñon o no basandose en una resonancia magnetica, para esto se utilizara un modelo CNN, en este caso el modelo pre-entrenado VGG-16 para aplicar la técnica de Transfer Learning.
- Criterios de éxito del proyecto:
Tener un conjunto de datos de entrenamiento adecuado para lograr buen desempeño del modelo en clasificación de imagenes de resonancia magnetica de los pacientes evidenciado por el resultado de evaluación de metricas del modelo.

### Excluye:

- El proyecto exluye la ejecución de varias iteraciones para refinamiento del modelo, unicamente debido al corto tiempo se realizara una unica iteración segun la metodología CRISP-DM desde entendimiento del negocio hasta el despliegue.

## Metodología

Para la ejecución de este proyecto se utilizara la metodología CRISP-DM (Cross-Insdustry Standard Process for Data Mining) desde la etapa de entendimiento del negocio hasta la etapa de despliegue pasando por cada etapa. Adicional se complementara la la metodología TDSP (Team Data Science Project) para tener una comprensión del uso de la misma en las empresas.

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 1 semana | Del 6 de Noviembre al 12 de Noviembre |
| Preprocesamiento, análisis exploratorio | 1 semana | Del 13 de Noviembre al 19 de Noviembre |
| Modelamiento y extracción de características | 1 semana | Del 20 de Noviembre al 26 de Noviembre |
| Despliegue | 1 semana | Del 27 de Noviembre al 3 de Diciembre |
| Evaluación y entrega final | 1 semana | Del 4 de Diciembre al 8 de Diciembre |

Hay que tener en cuenta que el tiempo de ejecución del proyecto es corto, con lo cual estas fechas son tentativas, de acuerdo a cada etapa del proyecto pueden cumplirse al 100%.

## Equipo del Proyecto

- Líder del proyecto: Katherine Rodriguez Sánchez

## Presupuesto

No aplica, es un proyecto 100% academico.

## Stakeholders

- No aplica.

## Aprobaciones

- No aplica.
