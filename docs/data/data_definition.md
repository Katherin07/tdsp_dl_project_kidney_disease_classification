# Definición de los datos

## Origen de los datos


El dataset original se obtuvo desde kaggle [Kidney Dataset](https://www.kaggle.com/datasets/nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone) el cual contiene conjuntos de datos de imagenes de resonancias magneticas de riñones de los pacientes en 4 folders segun el tipo de diagnostico, se cuenta inicialmente con un archivo comprimido "CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone.zip" el cual se compone de 4 folders y un total de 12.4k imagenes, sin embargo por practicidad y temas de capacidad de computo, se opta por escoger unicamente los folders nombrados Normal y Tumor, y de estos seleccionar al azar aproximadamente 200 imagenes para cada uno, dichos folders almacenan respectivamente las imagenes de las resonancias si tiene o no tumor.

Los datos resultantes de la seleccion se guardaron en un archivo comprimido "kidney_tumor_dataset.zip", el cual se alojo en almacenamiento de Google Drive con el fin de poder descargarlos desde la nube con ayuda de la libreria gdown y poder descomprimirlos.


## Especificación de los scripts para la carga de datos

- Scripts utilizados para la carga de los datos en la ruta (scripts/data_acquisition/main.py)

## Referencias a rutas o bases de datos origen y destino

- La ruta de origen del dataset es source_URL: https://drive.google.com/file/d/1vlhZ5c7abUKF8xXERIw6m9Te8fW7ohw3/view?usp=sharing

### Rutas de origen de datos

- Ubicación de los archivos de origen de los datos: source_URL: https://drive.google.com/file/d/1vlhZ5c7abUKF8xXERIw6m9Te8fW7ohw3/view?usp=sharing
- Estructura de los archivos de origen de los datos: Inicialmente archivo comprimido "kidney_tumor_dataset.zip", una vez descomprimido folders nombrados Normal y Tumor con las imeganes.

### Base de datos de destino

No aplica.

- [ ] Especificar la base de datos de destino para los datos.
- [ ] Especificar la estructura de la base de datos de destino.
- [ ] Describir los procedimientos de carga y transformación de los datos en la base de datos de destino.
