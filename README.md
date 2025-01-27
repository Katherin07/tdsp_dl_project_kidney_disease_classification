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

## MLflow

A continuación documentación a cerca de MLFlow herramienta utilizada para la experimentación y seguimiento de modelos utilizada en el proyecto:


- [Documentation](https://mlflow.org/docs/latest/index.html)

El siguiente tutorial es del autor del proyecto base en el cual se basa este proyecto:

- [MLflow tutorial](https://youtu.be/qdcHHrsXA48?si=bD5vDS60akNphkem)

##### cmd
- mlflow ui

### Dagshub

A continuación documentación a cerca de Dagshub plataforma de colaboración utilizada para el versionado de datos, código y modelos de ML basada en Git:

- [dagshub](https://dagshub.com/)

Configuración para el seguimiento de MLFlow desde Dagshub:

MLFLOW_TRACKING_URI=https://dagshub.com/Katherin07/tdsp_dl_project_kidney_disease_classification.mlflow \
MLFLOW_TRACKING_USERNAME=Katherin07 \
MLFLOW_TRACKING_PASSWORD=0bc7932c59f69bd8822c408a763da2f45998890c \
python script.py

Ejecutar los siguientes comandos para exportar los datos de configuración como variables de entorno:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Katherin07/tdsp_dl_project_kidney_disease_classification.mlflow

export MLFLOW_TRACKING_USERNAME=Katherin07 

export MLFLOW_TRACKING_PASSWORD=0bc7932c59f69bd8822c408a763da2f45998890c

```

### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag


## Sobre MLflow & DVC

MLflow

 - Es de grado de producción.
 - Registra todos tus experimentos.
 - Realiza registro y etiquetado de tu modelo.


DVC 

 - Es muy ligero, ideal solo para pruebas de concepto (POC).
 - Un rastreador ligero de experimentos.
 - Puede realizar orquestación (creación de pipelines).


# AWS-CICD-Deployment-con-Github-Actions

## 1. Ingresar a la consola AWS.

## 2. Crear un usuario IAM para el deployment

	#con el acceso especifico

	1. EC2 acceso : Es una maquina virtual

	2. ECR: Elastic Container registry, para guardar la imagen de docker en  aws


	#Descripcion: A cerca del deployment (main.yaml)

	1. Construir la imagen de docker con el codigo src

	2. Subir (Push) la imagen de docker hacia ECR

	3. Lanzar la maquina virtual EC2 

	4. Jalar (Pull) la imagen de docker desde ECR hacia la maquina virtual EC2

	5. Ejecutar/lanzar la imagen de docker en la maquina virtual EC2

	#Policys requeridas para el usuario IAM:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Crear un repo de ECR para almacenar/guardar la imagen de docker
    - Guardar la URI: 830939889036.dkr.ecr.us-east-1.amazonaws.com/kidney

	
## 4. Crear la maquina virtual EC2 (Ubuntu) 

## 5. Abrir la maquina virtual EC2 e instalar la imagen de docker en la maquina virtual EC2:
	
	
	#opcional

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#requerido

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configurar EC2 como self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> despues correr el comando uno por uno


# 7. Configurar los github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = 830939889036.dkr.ecr.us-east-1.amazonaws.com

    ECR_REPOSITORY_NAME = kidney
