import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import cv2

# Load pre-trained Keras model
model = tf.keras.models.load_model('/content/best_model.keras')

class_names = ['glioma', 'meningioma', 'notumor', 'pituitary']

st.title("🧠 Brain Tumor Detection")
st.write("Upload a brain MRI image to classify the type of tumor.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("Classifying...")

    img_array = np.array(image)
    img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    img_array = cv2.resize(img_array, (128,128))
    img_array = preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction)
    class_name = class_names[class_idx]
    confidence = np.max(prediction) * 100

    st.subheader(f"Prediction: {class_name}")
    st.write(f"Confidence: {confidence:.2f}%")
