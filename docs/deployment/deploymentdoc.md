# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** VGG16
- **Plataforma de despliegue:** AWS
- **Requisitos técnicos:** Lista de requisitos técnicos necesarios para el despliegue

1. Cuenta root de acceso a consola AWS.
2. Creación de usuario IAM, repo en ECR e instancia en EC2 para el despliegue.
3. Repositorio Github y configuración de Github actions.
4. Archivos con codigo de despliegue.

- **Requisitos de seguridad:** Lista de requisitos de seguridad necesarios para el despliegue

1.Secrets de AWS configurarlos en Github secrets.

- **Diagrama de arquitectura:** A continuación imagen que muestra la arquitectura del sistema que se utilizará para desplegar el modelo:

![arq](https://github.com/Katherin07/tdsp_dl_project_kidney_disease_classification/blob/master/images/arq.png)

## Código de despliegue

- **Archivo principal:** Nombre del archivo principal que contiene el código de despliegue (main.yaml)
- **Rutas de acceso a los archivos:** Lista de rutas de acceso a los archivos necesarios para el despliegue:
- .github/workflows/main.yaml
- Dockerfile
- **Variables de entorno:** Lista de variables de entorno necesarias para el despliegue: Ver archivos de despliegue


## Documentación del despliegue

La aplicación construida con Flask para la predicción de tumor de riñon en imagenes de resonancia magnetica se desplegara en la plataforma de AWS por medio de un flujo de CI CD con ayuda de Github actions, a continuación las instrucciones del despliegue.

- **Instrucciones de instalación y configuración:** Instrucciones detalladas para instalar y configurar la aplicación del modelo en la plataforma aws:

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


- **Instrucciones de uso:** Instrucciones detalladas para utilizar el modelo en la plataforma aws
Para poder ingresar a la aplicación ya desplegada en la instancia de EC2 de AWS, ingresar a la url http://52.4.93.250:8080/

- **Instrucciones de mantenimiento:** Instrucciones detalladas para mantener el modelo en la plataforma de despliegue

Para el mantenimiento del modelo en la aplicación es necesario estar en constante monitoreo de sus metricas de desempeño, mantenimiento de la aplicación, de las configuraciones del servicio web y las dependencias requeridas.
