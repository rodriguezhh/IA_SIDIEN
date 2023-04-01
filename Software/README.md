# Contenido
Dentro de la carpeta de software, se encuentran todos los archivos relacionados con el procesamiento de los datos del proyecto.

## Dataset 
En la carpeta de Dataset, Encontramos la base de datos de 3 enfermedades de la hoja de la planta del tomate y su hoja sana. Se cuenta con la enfermedad A con XXX imágenes, la enfermedad B con XXX imágenes, la enfermedad C con XXX imágenes y la hoja sana con XXX imágenes. 

## Inteligencia_Artificial
En la carpeta de Inteligencia_Artificial, Encontramos el algoritmo propuesto de jerarquía reducida, además, de los algoritmos de arqquitecturas de transfer learning, que son VGG19, MobileNetV2 y ResNet50.

## Modelos de IA 
En la carpeta de Modelos de IA , Encontramos los .h5 de los diferentes modelos ya entrenados y dispuestos a usar de las distintas arquitecturas de inteligencia artificial. 

## Interfaz de usuario 
En La carpeta Interfaz contiene los archivos relacionados con el diseño de la PCB del circuito que proporciona la iluminacion del dispositivo. Este diseño nos permite realizar la toma de las imagenes con un ambiente controlado. 

## Procesamiento_de_imagenes
En la carpeta de Procesamiento_de_imagenes, se encuentra el algoritmo de Disivison_datos, con el cual nos permite separar las imagenes en los conjuntos de entrenamiento, validación y prueba, además, se encuentra el algoritmo de Aumento_datos que nos permite generar nuevas imágenes.

# Como se usa
## Creando un modelo 
NOTA: 

## Desplegando un modelo 

### Librerias y dependencias.
1. Descargar Python 3.

### Procesamiento de imágenes con IA 
1. Dirijase a la carpeta de Dataset y descarguela
2. Dirijase a la carpeta de Procesamiento_de_imagenes, descargue el archivo División_datos.py y ejecutelo.
3. Dirijase a la carpeta de Procesamiento_de_imagenes, descargue el archivo Aumento_datos.py y ejecutelo. Tenga en cuenta que el código de aumento de datos se realiza en una sola carpeta. 
4. Dirijase a la carpeta de Modelos de IA, descargue el archivo del modelo de IA que desea probar y ejecutelo. 

### Proceso de despliegue de la IA e interfaz de usuario
1. Dirijase a la Procesamiento_de_imagenes,  descargue todos los archivos y envielos a impresión 3D.
2. Dirijase a la carpeta SVG,  descargue todos los archivos y envielos a corte laser. 
3. Dirijase a la carptea PCB_LED, descargue los planos de impresión .PDF y fabrique su PCB.
4. Finalmente realice el proceso de ensamblado. 
