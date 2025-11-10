# 🧠 Brain Tumor Classification using CNN & Transfer Learning (DenseNet121)
A deep learning project that detects and classifies brain tumors from MRI scans using Convolutional Neural Networks (CNN) and Transfer Learning (DenseNet121). Built with TensorFlow and Keras.



## 📋 Overview
This project focuses on classifying **brain tumor MRI images** into four main categories:
- 🧩 Glioma  
- 🧩 Meningioma  
- 🧠 No Tumor  
- 🧩 Pituitary  

The model leverages **Transfer Learning** using **DenseNet121** as the backbone.  
Fine-tuning was performed by **unfreezing the last 20 layers** to improve feature extraction and model accuracy.

---

## 🧠 Model Summary
- **Base Model:** DenseNet121 (Pre-trained on ImageNet)  
- **Fine-tuning:** Last 10 layers unfrozen  
- **Optimizer:** Adam  
- **Loss Function:** Categorical Crossentropy  
- **Metrics:** Accuracy, Precision, Recall  

---

## 📊 Dataset
MRI image dataset containing four classes:
`['glioma', 'meningioma', 'notumor', 'pituitary']`  
All images were resized, normalized, and augmented before training.

---

## ⚙️ Training Results

| Dataset        | Accuracy  | Loss    | Precision | Recall  |
|----------------|----------|---------|-----------|---------|
| **Training**   | 95.80%   | 0.1400  | 96.27%    | 95.41% |
| **Validation** | 91.84%   | 0.2343  | 92.97%    | 91.20% |
| **Testing**    | 95.28%   | 0.1453  | 95.79%    | 94.72% |


✅ **Excellent generalization with 95% accuracy on the test set.**

---

## 🖼️ Example Outputs
(You can add sample prediction images or confusion matrix plots here)

---

## 🚀 Features
- CNN-based classification with Transfer Learning  
- High test accuracy and model stability  
- Fine-tuned MobileNetV2 for medical imaging  
- Ready for integration into healthcare systems  

---

## 🧮 Requirements
To install dependencies, run:

```bash
pip install -r requirements.txt
