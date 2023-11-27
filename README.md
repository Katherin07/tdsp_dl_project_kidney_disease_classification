# Team Data Science Project: Deep Learning Kidney Disease Classification

El proyecto tiene como objetivo principal construir un modelo CNN que clasificara si un paciente tiene un tumor en el riñon o no basandose en una resonancia magnetica. Para lograr esto, se utilizaran conjuntos de datos de imagenes de resonancias magneticas adecuadas para entrenar, validar y probar un modelo CNN que pueda clasificar las imagenes de los pacientes. Se utilizara la arquitectura y pesos del modelo VGG-16 para entrenar el modelo para este problema binario.

Este proyecto esta estructurado acorde a las siguientes carpetas y archivos:

* `src`: Acá esta el código o implementación del proyecto en Python.
* `docs`: En esta carpeta se encuentran los documentos definidos para el proyecto segun la metodología TDSP.
* `scripts`: Acá estan  los scripts/notebooks que se ejecutarán en el proyecto.

## Workflows

A continuación el flujo de trabajo seguido durante el desarrollo del proyecto:

1. Actualización de config.yaml
2. Actualización de secrets.yaml [Opcional]
3. Actualización de params.yaml
4. Actualización de entity
5. Actualización de configuration manager en src config
6. Actualización de componentes (database, preprocessing, models, training, evaluation)
7. Actualización de pipeline 
8. Actualización de main.py
9. Actualización de dvc.yaml
10. Actualización de app.py


# Como ejecutar el proyecto?

### PASOS:

Clonar el repositorio:

```bash
https://github.com/Katherin07/tdsp_dl_project_kidney_disease_classification
```
### PASO 01- Crear un ambiente de Conda despues de abrir el repositorio

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```


### PASO 02- Instalar los requerimientos
```bash
pip install -r requirements.txt
```