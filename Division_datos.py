#Importación de librerias necesarias
import os
import random
from math import ceil
import shutil

# Definimos la carpeta de origen y obtenemos la lista de subcarpetas
source = 'images/'
sub_folders = os.listdir(source)

# Obtenemos el número total de subcarpetas
fol_index = len(sub_folders)
folder = os.path.basename(source)


# Definimos una función que divide un vector en tres vectores de entrenamiento, prueba y validación
def split_vector(folder_source):
    # Obtenemos la lista de nombres de archivo en la carpeta de origen
    filenames = os.listdir(folder_source)
    # Calculamos el índice para dividir el vector en un 80% para entrenamiento y un 20% para prueba y validación
    split_index = int(ceil(len(filenames)*0.8))
    # Tomamos una muestra aleatoria del 80% para entrenamiento
    sample_train = random.sample(filenames, split_index)
    # Obtenemos el vector restante (20%) para prueba y validación
    sample = [x for x in filenames if x not in sample_train]
    # Calculamos el índice para dividir el vector de prueba y validación a partes iguales
    split_index_2 = int(ceil(len(sample)*0.5))
    # Tomamos una muestra aleatoria del 50% para prueba
    sample_test = random.sample(sample,split_index_2)
    # Obtenemos el vector restante (50%) para validación
    sample_val = [y for y in sample if y not in sample_test]

    return sample_train, sample_test, sample_val

# Definimos una función para copiar los archivos de la carpeta de origen a la carpeta de entrenamiento
def train_folder(folder_source, folder_train, sample):
    # Creamos la carpeta de entrenamiento si no existe
    if not os.path.exists(folder_train):
        os.makedirs(folder_train)
        # Copiamos cada archivo de la lista de entrenamiento a la carpeta de entrenamiento
        for filename in sample:
            # Obtener la ruta completa del archivo de origen y destino
            source_path = os.path.join(folder_source, filename)
            destination_path = os.path.join(folder_train, filename)

            # Copiar el archivo
            shutil.copy(source_path, destination_path)

# Definimos una función para copiar los archivos de la carpeta de origen a la carpeta de prueba
def test_folder(folder_source, folder_test, sample_test):

    if not os.path.exists(folder_test):
        os.makedirs(folder_test)
        # Copiar cada archivo a la carpeta de destino
        for filename in sample_test:
            # Obtener la ruta completa del archivo de origen y destino
            source_path = os.path.join(folder_source, filename)
            destination_path = os.path.join(folder_test, filename)

            # Copiar el archivo
            shutil.copy(source_path, destination_path)

# Definimos una función para copiar los archivos de la carpeta de origen a la carpeta de validacion
def val_folder(folder_source, folder_val, sample_val):

    if not os.path.exists(folder_val):
        os.makedirs(folder_val)
        # Copiar cada archivo a la carpeta de destino
        for filename in sample_val:
            # Obtener la ruta completa del archivo de origen y destino
            source_path = os.path.join(folder_source, filename)
            destination_path = os.path.join(folder_val, filename)

            # Copiar el archivo
            shutil.copy(source_path, destination_path)

# Iteramos a través de cada subcarpeta
for sub_fol in sub_folders:
    # Obtenemos la ruta de la subcarpeta actual
    sub_fol_dir = source + sub_fol
    # Obtenemos el nombre de la carpeta actual
    folder = os.path.basename(sub_fol_dir)
    
    # Definimos las carpetas de entrenamiento, prueba y validación
    folder_source = source + folder
    folder_train = 'train/' + folder
    folder_test = 'test/' + folder
    folder_val = 'val/' + folder

    # Dividimos la lista de archivos en tres vectores (entrenamiento, prueba y validación)
    sample_train, sample_test, sample_val = split_vector(folder_source)
    
    # Copiamos los archivos de la carpeta de origen a las carpetas de entrenamiento, prueba y validación
    train_folder(folder_source,folder_train,sample_train)
    test_folder(folder_source,folder_test,sample_test)
    val_folder(folder_source,folder_val,sample_val)