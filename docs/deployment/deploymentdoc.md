# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** VGG16
- **Plataforma de despliegue:** AWS
- **Requisitos técnicos:** Lista de requisitos técnicos necesarios para el despliegue

# AWS-CICD-Deployment-con-Github-Actions

## 1. Ingresar a consola AWS.

## 2. Crear usuario IAM para el deployment

	#con el acceso especifico

	1. EC2 acceso : Es una maquina virtual

	2. ECR: Elastic Container registry para guardar una imagen de docker en aws


	#Descripción: A cerca del deployment

	1. Construir imagen de docker del codigo fuente

	2. Publicar la imagen de docker en ECR

	3. Ingresar a EC2 

	4. Extraer imagen desde ECR hacia EC2

	5. Lanzar imagen de docker en EC2

	#Politica:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Crear ECR repo para almacenar/guardar la docker image
    - Guardar la URI.

	
## 4. Crear maquina virtual EC2 (Ubuntu) 

## 5. Abrir EC2 e instalar docker en maquina EC2:
	
	
	#opcional

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#requirido

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configurar EC2 como self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> despues correr comandos uno por uno


 

- **Requisitos de seguridad:** Lista de requisitos de seguridad necesarios para el despliegue

# 7. Configurar github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = 

    ECR_REPOSITORY_NAME =

- **Diagrama de arquitectura:** (imagen que muestra la arquitectura del sistema que se utilizará para desplegar el modelo)

## Código de despliegue

- **Archivo principal:** (nombre del archivo principal que contiene el código de despliegue)
AWS-CICD-Deployment-con-Github-Actions
- **Rutas de acceso a los archivos:** (lista de rutas de acceso a los archivos necesarios para el despliegue)
- **Variables de entorno:** (lista de variables de entorno necesarias para el despliegue)

Ejecutar los siguientes comandos para exportar los datos de configuración como variables de entorno:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Katherin07/tdsp_dl_project_kidney_disease_classification.mlflow

export MLFLOW_TRACKING_USERNAME=Katherin07 

export MLFLOW_TRACKING_PASSWORD=0bc7932c59f69bd8822c408a763da2f45998890c

```

## Documentación del despliegue

Esta documentación se incluira en la proxima entrega, ya que por ahora se ha desplegado localmente mediante Flask con el archivo app.py, a continuación una imagen de la vista de la aplicación para predicción de tumor en riñones de pacientes basandose en una resonancia magnetica:


- **Instrucciones de instalación:** (instrucciones detalladas para instalar el modelo en la plataforma de despliegue)
- **Instrucciones de configuración:** (instrucciones detalladas para configurar el modelo en la plataforma de despliegue)
- **Instrucciones de uso:** (instrucciones detalladas para utilizar el modelo en la plataforma de despliegue)
- **Instrucciones de mantenimiento:** (instrucciones detalladas para mantener el modelo en la plataforma de despliegue)
