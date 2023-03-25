# Importación de librerias
import os
import cv2
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import load_img, img_to_array

# Definir la carpeta donde se guardarán las imágenes generadas y el número de imágenes aumentadas que se generarán
folder = 'Aumento_de_datos'

# Factor de aumento
images_increased = 3

# Se crea la carpeta Aumento de datos
try:
    os.mkdir(folder)
except:
    pass
    
# Definir los parámetros de aumento de datos
train_generator = ImageDataGenerator(
    zoom_range=0.2, # Definimos el rango de zoom que se aplicará aleatoriamente a las imágenes
    horizontal_flip=True, # Definimos si se aplicará o no un volteo horizontal aleatorio a las imágenes
    vertical_flip=True, # Definimos si se aplicará o no un volteo vertical aleatorio a las imágenes
    rotation_range=20, # Definimos el rango de rotación que se aplicará aleatoriamente a las imágenes
)

# Definir la ubicación de las imágenes
data_path = 'Tomato__Tomato_mosaic_virus/' 
data_dir_list = os.listdir(data_path)

# Definir el tamaño de las imágenes
image_size = 256

# Inicializar contador de imágenes generadas
num_images = 0

# Iterar a través de las imágenes en la carpeta
for i, image_file in enumerate(data_dir_list):    
    # Cargar la imagen y redimensionarla al tamaño especificado
    img_path = os.path.join(data_path, image_file)
    image = load_img(img_path)
    
    img = cv2.resize(img_to_array(image), (image_size , image_size ), interpolation=cv2.INTER_AREA)
    x = img/255
    x = np.expand_dims(x, axis=0)
    
    t = 1
    
    # Aplicar aumento de datos a la imagen y guardar las imágenes generadas
    for output_batch in train_generator.flow(x, batch_size=1):
        imagen = output_batch[0]*255
        imgfinal = cv2.cvtColor(imagen.astype('uint8'), cv2.COLOR_BGR2RGB)
        cv2.imwrite(os.path.join(folder, f"{i}{t}.jpg"), imgfinal) 
        t += 1
        
        num_images += 1
        if t > images_increased:
            break
    
print("Total de imágenes generedas:", num_images)