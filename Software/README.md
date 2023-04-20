# Contenido
Dentro de esta carpeta, se encuentran todos los archivos relacionados con el procesamiento de los datos del proyecto.

## Base de datos
En el siguiente link se encuentra la base de datos:https://drive.google.com/drive/folders/1tE_-uaknxtAyiTTtgUqdADf2sIitAHyi?usp=share_link.

## Inteligencia_Artificial
En la carpeta de Inteligencia_Artificial, Encontramos el algoritmo propuesto de jerarquía reducida, además, de los algoritmos de arqquitecturas de transfer learning, que son VGG19, MobileNetV2 y ResNet50.

## Modelos_IA 
En el siguiente link: https://drive.google.com/drive/folders/1_pJdKnspFUj5AHXt6KV58SqsYDc62IjV?usp=sharing. Se encuentra los .h5 de los diferentes modelos ya entrenados y dispuestos a usar de las distintas arquitecturas de inteligencia artificial. 

## Interfaz
En La carpeta Interfaz contiene los archivos relacionados con el diseño de la PCB del circuito que proporciona la iluminacion del dispositivo. Este diseño nos permite realizar la toma de las imagenes con un ambiente controlado. 

## Procesamiento_de_imagenes
En la carpeta de Procesamiento_de_imagenes, se encuentra el algoritmo de Disivison_datos, con el cual nos permite separar las imagenes en los conjuntos de entrenamiento, validación y prueba, además, se encuentra el algoritmo de Aumento_datos que nos permite generar nuevas imágenes.

*NOTA: para la instalación del software se recomienda utilizar como mínimo una tarjeta SD de 32GB.
# Librerias y dependencias para Jetson nano 4GB.
* Imagen de la tarjeta SD: https://github.com/Qengineering/Jetson-Nano-image.git
* PyQt5 5.15.6


# Librerias y dependencias para Rasbpberry pi 4B 4GB.
* Imagen de la tarjeta SD: 
* Pyqt
* opencv
* Tensorflow


# Como se usa
## Creando un modelo 
1. Dirijase a la carpeta de Dataset y descarguela
2. Dirijase a la carpeta de Procesamiento_de_imagenes, descargue el archivo División_datos.py y ejecutelo.
3. Dirijase a la carpeta de Procesamiento_de_imagenes, descargue el archivo Aumento_datos.py y ejecutelo en la carpeta de entrenamiento. 
4. Suba las carpetas a Google Drive.
5. Cree su modelo en Google Colab, puede tomar como base las arquitecturas propuestas en la carpeta Inteligencia_Artificial
6. Entrene su modelo y guardelo para que se pueda desplegar. 

* NOTA: si quiere evitar el proceso de entreanmiento y creación de un modelo. puede descargar alguno de la carpeta Modelos_IA 

## Despliegue en Jetson nano 4GB.
1. Instale la imagen de la Jetson nano en la memoria SD siguiendo los pasos del repositorio de GitHub https://github.com/Qengineering/Jetson-Nano-image.git
2. Instale las dependenciaas requeridas por la Jetson Nano de 4 GB. Unicamente instale PyQt5 ya que en la imagen instalada anteriormente se encuentran la mayoría de librerias necesarias para el funcionamiento del sistema.
3. Una vez instaladas las librerías necesarias, descargue la carpeta https://github.com/rodriguezhh/IA_SIDIEN/tree/main/Software/Interfaz/told2_v0.1. Esta carpeta contiene los archivos y recursos necesarios para el funcionamiento de la interfaz de detección.
4. Descargue el modelo ResNet50 entrenado del siguiente link https://drive.google.com/file/d/1AAf66BFohPHkJcNdAy4Eeix6V2cA7vEN/view?usp=share_link y agreguelo a la carpeta que descargó en el paso anterior.

## Despliegue en Rasbpberry pi 4B 4GB.
1. 
