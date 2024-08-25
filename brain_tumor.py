import json
import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('model/brain_tumor.h5')
categories = ['glioma', 'meningioma', 'notumor', 'pituitary']


def main(new_image_path):
    new_image = cv2.imread(new_image_path)
    resized_image = cv2.resize(new_image, (150, 150))
    input_image = np.expand_dims(resized_image, axis=0)

# Make predictions on the new image
    predictions = model.predict(input_image)
    predicted_category = np.argmax(predictions)
    print(json.dumps({'prediction': categories[predicted_category]}))
    return json.dumps({'prediction': categories[predicted_category]})
