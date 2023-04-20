![Alt Text](https://i.imgur.com/jgLlu2G.png)
# DIAGNÓSTICO DE ENFERMEDADES EN LA HOJA DEL TOMATE MEDIANTE UN SISTEMA EMBEBIDO USANDO INTELIGENCIA ARTIFICIAL E IMÁGENES.

## Descripción del sistema

Este proyecto tiene como objetivo diseñar e implementar un algoritmo de aprendizaje profundo que permita identificar enfermedades en la hoja de la planta del tomate desplegado en un sistema embebido. El sistema está destinado para servir como herramient a agricultores experimentados como a ingenieros agrónomos, con el objetivo de realizar diagnósticos tempranos y asegurar la salud del cultivo.Además, la implementación de este sistema también puede tener fines educativos, permitiendo el estudio de las enfermedades que afectan a las hojas de tomate y apoyando el seguimiento de los cultivos.

Para llevar a cabo este proyecto, se utilizó una base de datos proporcionada por la comunidad Kaggle. Además, se visitaron diferentes invernaderos para capturar imágenes de hojas sanas y enfermas de los cultivos de tomate. Se emplearon herramientas de software libre y código abierto para cada etapa del proyecto.

Se entrenó una inteligencia artificial de jerarquía simplificada y tres modelos de Transfer Learning utilizando Google Colaboratory.

Finalmente, el modelo resultante fue implementado en dos sistemas embebidos, NVIDIA Jetson Nano de 4GB y Raspberry pi 4B. Se realizó un análisis comparativo de los resultados obtenidos para validar su rendimiento en ambas tarjetas de desarrollo.

## Video sobre el desarrollo del proyecto.
https://youtu.be/ES93pp3hpe4

## Drive del proyecto.
https://drive.google.com/drive/folders/18Io3CUIHZYFtg3d0LMKD3wjqCA_87UzG?usp=sharing

## Manual de Usuario 
### Paso a paso del Hardware
1. Accione el interruptor para encender el dispositivo TOLD2.
![Alt Text](https://i.imgur.com/mqMmWQr.png)
2. Si va a hacer uso del porta muestras, accione el interruptor para encender la luz del dispositivo TOLD2.
3. ![Alt Text](https://i.imgur.com/mqMmWQr.png)
4. Seleccione la muestra de hoja de la plante del tomate que desea inspeccionar y asegurela con el alfiler en el porta muestras y depositela. 
5. Diríjase al apartado ’Paso a paso de la interfaz de usuario’ para proceder con el diagnóstico.

 ### NOTA: 
 En caso de que el dispositivo TOLD2 no encienda, conecte el cargador en el puerto al costado del dispositivo TOLD2. 

### Paso a paso de la Interfaz de usuario 
1. Al iniciar el dispositivo, debe observar la siguiente pantalla.
![Alt Text](https://i.imgur.com/vDMGVeG.jpg)
2. Haga doble click sobre el icono "hacer detección". Acontinuación se debe abrir una interfaz como la siguiente. Asegurese de abrir el software unicamente con dos clicks, de lo contrario se abrirá más de una ventana.
![Alt Text](https://i.imgur.com/zbWsorS.png)
3. Captue la imagen haciendo click en el boton "Tomar foto". 
4. Haga click en el botón "hacer detección". 
5. Finalemte podra observar un diagnóstico de su hoja, además. Si desea realizar otra predicción puede hacer click sobre ”Nueva detección" y repita el proceso cuantas veces desee.

## Contribución
Este proyecto se encuentra en constante evolución, por lo que cualquier contribución será bienvenida. Si deseas contribuir, por favor envía un pull request o contacta al equipo de desarrollo.

## Contacto 
* Camilo Andres Santos Ortiz. camilosantos6584@gmail.com
* Harold Hernando Rodriguez Rodriguez. rodriguezhh03@gmail.com
* Wilmer Andres Guerrero Rangel. andresguerrero1204@gmail.com
