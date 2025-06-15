import cv2
import numpy as np
import streamlit as st
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    preprocess_input,
    decode_predictions
)
from PIL import Image

def load_model():
    model = MobileNetV2(weights="imagenet")
    return model

def preprocess_image(image):
    img = np.array(image) #convert image to numpy array
    img = cv2.resize(img, (224, 224)) #resize image to 224x224
    img = preprocess_input(img) #preprocess image
    img = np.expand_dims(img, axis=0) #add batch dimension
    return img

def classify_image(model,image):
    try:
        processed_image = preprocess_image(image) #preprocess image
        predictions = model.predict(processed_image) #passing the processed image to the model
        decoded_predictions = decode_predictions(predictions, top=3)[0] #decode the predictions and return the top 3 predictions labels
        
        return decoded_predictions
    except Exception as e:
        st.error(f"Error classifying image: {str(e)}")
        return None
    
def main():
    st.set_page_config(page_title="AI Image Classifier", page_icon="🖼️", layout="centered")

    st.title("AI Image Classifier")
    st.write("Upload an image and let AI tell you what is in it!")

    @st.cache_resource #cache the model to avoid reloading it every time the app is run
    def load_cached_model():
        return load_model()
    
    model = load_cached_model()

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

    if uploaded_file is not None:
        image = st.image( #displaying the image
            uploaded_file, caption="Uploaded Image", use_container_width=True
        )

        btn = st.button("Classify Image")

        if btn:
            with st.spinner("Analyzing Image..."):
                 image  = Image.open(uploaded_file)
                 predictions = classify_image(model, image)

                 if predictions:
                    st.subheader("Predictions")
                    for _, label, score in predictions: # we use _ for anonymouse variable, cause we dont care with the first variable
                        st.write(f"**{label}**: {score:.2%}")

if __name__ == "__main__":
    main()