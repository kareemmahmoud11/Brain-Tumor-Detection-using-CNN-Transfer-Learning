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

## 🔍 Grad-CAM Visualization
We applied **Grad-CAM** to our trained model to identify **tumor regions** in the MRI scans:

- Generates a **heatmap** indicating important areas contributing to the prediction.  
- Helps doctors and researchers **understand model decisions**.  
- Example visualizations for all four classes:

| Tumor Type   | Original MRI | Grad-CAM Heatmap | Overlay |
|--------------|--------------|-----------------|---------|
| Glioma       | ![Glioma Original](https://github.com/user-attachments/assets/875921d8-d9e1-45f6-91ca-04f137c84db2) | ![Glioma Heatmap](https://github.com/user-attachments/assets/eff4fc05-f380-4dd8-aca5-52672d03f753) | ![Glioma Overlay](https://github.com/user-attachments/assets/691d8849-608d-4fa3-8631-861782d14c23) |
| Meningioma   | ![Meningioma Original](https://github.com/user-attachments/assets/a84f3b1b-d85f-430a-ac49-b46fa4597352) | ![Meningioma Heatmap](https://github.com/user-attachments/assets/a66def8d-addf-481e-8a04-5cae06ff816e) | ![Meningioma Overlay](https://github.com/user-attachments/assets/61f0ef78-4de0-400b-b1b9-9b40804a07db) |
| No Tumor     | ![No Tumor Original](https://github.com/user-attachments/assets/0b2bcc45-f443-46aa-aa63-f3cec89188b2) | ![No Tumor Heatmap](https://github.com/user-attachments/assets/b57df12b-abb7-4c4a-b9c5-abc21a1f5238) | ![No Tumor Overlay](https://github.com/user-attachments/assets/425057dd-31b7-467c-8ba8-15cb4b30c7bc) |
| Pituitary    | ![Pituitary Original](https://github.com/user-attachments/assets/ed78909d-bb1a-480d-a301-e3c8ebdd03ea) | ![Pituitary Heatmap](https://github.com/user-attachments/assets/7273b4b9-7768-49c9-8d70-b6c0cc2ae5ed) | ![Pituitary Overlay](https://github.com/user-attachments/assets/977b5ad7-289d-47a7-8261-2600c8c9260c) |


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
