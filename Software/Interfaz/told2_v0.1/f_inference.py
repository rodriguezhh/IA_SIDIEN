import tensorflow as tf
from tensorflow import keras
import cv2
import numpy as np

model_1 = keras.models.load_model('told2_real.h5')
img = cv2.imread('tomato8.JPG')
img = cv2.resize(img, (256, 256))
img_s = img.astype(np.uint8)
img = img_s.reshape(1, img_s.shape[0], img_s.shape[1], img_s.shape[2])
#print(img_s)

predictions = model_1.predict(img)
print(predictions)

result = np.argmax(predictions)
if result == 0:
    res = 'Mancha marron'

elif result == 1:
    res = 'Hongo'

elif result == 2:
    res = 'Mosaico'

else:
    res = 'Hoja sana'

print(res)