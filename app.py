import streamlit as st
from PIL import Image
import easyocr
import numpy as np

# Initialize OCR Reader
reader = easyocr.Reader(['en', 'hi'])

# Streamlit UI
st.title("OCR and Keyword Search Application")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Convert the uploaded image to bytes or NumPy array
    image = np.array(image)

    # Perform OCR
    with st.spinner('Performing OCR...'):
        extracted_text = reader.readtext(image, detail=0)
        st.success('Text extraction successful!')
        st.write("Extracted Text:")
        st.write(extracted_text)

        # Keyword search input
        keyword = st.text_input("Enter keyword to search in extracted text")
        if keyword:
            matching_text = [line for line in extracted_text if keyword.lower() in line.lower()]
            if matching_text:
                st.write("Matching Text:")
                st.write(matching_text)
            else:
                st.write("No matching text found.")
