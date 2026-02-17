# VisionAI-SuperResolution 🚀

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-1.13.1-red)
![Streamlit](https://img.shields.io/badge/Streamlit-App-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

## 🔬 Advanced AI Image Super Resolution using Real-ESRGAN

VisionAI-SuperResolution is a deep learning-powered image enhancement tool that improves low-resolution images using the Real-ESRGAN neural network model.

Built with:

- PyTorch  
- Real-ESRGAN  
- OpenCV  
- Streamlit  

---

# ✨ Features

- 🔍 4× AI Super Resolution  
- 🧠 Real-ESRGAN Deep Learning Model  
- ⚡ CPU Compatible  
- 🖼 Clean Interactive Web UI  
- ⬇ Download Enhanced Images  
- 🚀 Model Caching for Faster Inference  

---

# 🧠 About the Model

This project uses **Real-ESRGAN (Enhanced Super-Resolution GAN)**.

## What is Real-ESRGAN?

Real-ESRGAN is a state-of-the-art deep learning model designed for:

- Image super-resolution  
- Photo restoration  
- Upscaling low-quality images  
- Removing compression artifacts  
- Recovering fine textures  

It improves visual quality while maintaining realistic details.

---

## 🏗 Model Architecture

- **Backbone:** RRDBNet (Residual-in-Residual Dense Block Network)  
- **Framework:** PyTorch  
- **Technique:** Generative Adversarial Network (GAN)  
- **Upscaling Factor:** 4×  
- **Pretrained Model:** `RealESRGAN_x4plus`  
- **Inference Mode:** CPU (GPU optional)  

### 📐 Scale Explanation

A `256×256` image becomes `1024×1024` with enhanced clarity and reconstructed detail.

Pretrained weights (~60MB) are downloaded automatically on first run.

---

# 📂 Project Structure

```
VisionAI-SuperResolution/
│
├── app.py
├── enhancer.py
├── requirements.txt
└── README.md
```

---

# 📦 Installation Guide (A–Z)

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/VisionAI-SuperResolution.git
cd VisionAI-SuperResolution
```

---

## 2️⃣ Create Virtual Environment (Recommended)

### Windows

```bash
py -3.10 -m venv vision_env
vision_env\Scripts\activate
```

### Mac / Linux

```bash
python3.10 -m venv vision_env
source vision_env/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

⚠️ Recommended Python version: **3.10**

---

## 4️⃣ Run the Application

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

# 📸 How It Works

1. Upload an image  
2. Image is converted to NumPy array  
3. Passed into Real-ESRGAN model  
4. Model enhances resolution by 4×  
5. Enhanced image displayed  
6. Download option available  

---

# ⚡ Performance Notes

- First run downloads ~60MB model weights  
- CPU inference may take a few seconds for large images  
- GPU acceleration can be enabled using CUDA-enabled PyTorch  
- Model caching prevents reloading on every interaction  

---

# 🔮 Future Improvements

- GPU acceleration support  
- Face enhancement (GFPGAN integration)  
- Before/After comparison slider  
- Batch image processing  
- Cloud deployment (Streamlit Cloud / AWS / Azure)  
- Desktop executable (.exe) version  
- API deployment (FastAPI backend)  

---

# 📜 License

This project utilizes the Real-ESRGAN model.  
Refer to the official Real-ESRGAN repository for licensing details.

---

# 👨‍💻 Author

Developed by: **Your Name**  
Project: VisionAI-SuperResolution  
Year: 2026  

---

# ⭐ Support

If you found this project useful, please consider giving it a star ⭐
