import streamlit as st
import cv2
import numpy as np
from enhancer import load_model, enhance_image


st.set_page_config(page_title="VisionAI Enhancer", layout="wide")

st.title("🔬 VisionAI - Advanced Image Quality Enhancer")
st.write("Upload an image and enhance it using Real-ESRGAN Super Resolution.")


# Cache model so it loads only once
@st.cache_resource
def get_model():
    return load_model()


model = get_model()


uploaded_file = st.file_uploader("📤 Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(img, channels="BGR", use_container_width=True)

    if st.button("🚀 Enhance Image"):
        with st.spinner("Enhancing image... Please wait..."):

            enhanced = enhance_image(model, img)

            with col2:
                st.subheader("Enhanced Image")
                st.image(enhanced, channels="BGR", use_container_width=True)

            # Download option
            _, buffer = cv2.imencode(".png", enhanced)
            st.download_button(
                label="⬇ Download Enhanced Image",
                data=buffer.tobytes(),
                file_name="enhanced_image.png",
                mime="image/png",
            )
