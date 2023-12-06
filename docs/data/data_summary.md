# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos

En esta sección se presenta un resumen general de los datos. Se describe el número total de observaciones, variables, el tipo de variables, la presencia de valores faltantes y la distribución de las variables.

Como aporte inicial de la fuente de datos en kaggle se menciona lo siguiente:

"El conjunto de datos se recopiló de PACS (sistema de comunicación y archivo de imágenes) de diferentes hospitales en Dhaka, Bangladesh, donde a los pacientes ya se les diagnosticó un tumor renal, quiste, hallazgos normales o cálculos. Tanto el corte coronal como el axial se seleccionaron a partir de estudios con y sin contraste con protocolo para todo el abdomen y urograma. Luego se seleccionó cuidadosamente el estudio Dicom, un diagnóstico a la vez, y a partir de ellos creamos un lote de imágenes Dicom de la región de interés para cada hallazgo radiológico. Después de eso, excluimos la información y los metadatos de cada paciente de las imágenes Dicom y convertimos las imágenes Dicom a un formato de imagen jpg sin pérdidas."

Segun la fuente la imagenes ya fueron evaluadas por expertos y seleccionadas con el fin de tener la región puntual de interes para la clasificación, adicional se encentran en formato de imagen jpg sin pérdidas.

La variable objetivo principal de este problema de clasificación sera entonces la clase de si tiene o no tumor (YES/NO), una variable categorica.

Imagen con clasificación "normal" sin tumor:
![normal](https://github.com/Katherin07/tdsp_dl_project_kidney_disease_classification/blob/master/images/normal.jpg)

Imagen con clasificación "tumor" con tumor:
![tumor](https://github.com/Katherin07/tdsp_dl_project_kidney_disease_classification/blob/master/images/tumor.jpg)

## Resumen de calidad de los datos

En esta sección se presenta un resumen de la calidad de los datos. Se describe la cantidad y porcentaje de valores faltantes, valores extremos, errores y duplicados. También se muestran las acciones tomadas para abordar estos problemas.

En total se identifico que la imagenes de resonancia del folder normal en total son 240 imagenes y de tumor 225 imagenes todas en formato jpg.
No hay valores faltantes ya que inicialmente se redujo en dataset original seleccionando aproximadamente 200 imagenes por folder de las iniciales.


## Variable objetivo

En esta sección se describe la variable objetivo. Se muestra la distribución de la variable y se presentan gráficos que permiten entender mejor su comportamiento.

La variable objetivo principal de este problema de clasificación sera entonces la clase de si tiene o no tumor (YES/NO), es una variable categorica, su distribución esta representada por etiqueta YES con 240 imagenes y NO con 225 imagenes.

## Variables individuales

No aplica al proyecto.

En esta sección se presenta un análisis detallado de cada variable individual. Se muestran estadísticas descriptivas, gráficos de distribución y de relación con la variable objetivo (si aplica). Además, se describen posibles transformaciones que se pueden aplicar a la variable.

## Ranking de variables

No aplica al proyecto.

En esta sección se presenta un ranking de las variables más importantes para predecir la variable objetivo. Se utilizan técnicas como la correlación, el análisis de componentes principales (PCA) o la importancia de las variables en un modelo de aprendizaje automático.

## Relación entre variables explicativas y variable objetivo

No aplica al proyecto.

En esta sección se presenta un análisis de la relación entre las variables explicativas y la variable objetivo. Se utilizan gráficos como la matriz de correlación y el diagrama de dispersión para entender mejor la relación entre las variables. Además, se pueden utilizar técnicas como la regresión lineal para modelar la relación entre las variables.
