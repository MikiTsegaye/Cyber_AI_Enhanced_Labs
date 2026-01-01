# 🛡️ Morpheus Spear Phishing Detection
**Group 7 | NVIDIA AI-Enhanced Cybersecurity Lab**

A GPU-accelerated anomaly detection pipeline built on the NVIDIA Morpheus framework to detect sophisticated spear-phishing attacks in the Enron email corpus.

---

## 📖 Project Overview
Traditional security systems rely on static signatures that modern spear-phishing attacks easily evade. This project implements an **AI-native "Morpheus" pipeline** that learns the mathematical "fingerprint" of legitimate business communication to detect anomalies.

### ✨ Key Features
* **GPU Acceleration**: Leverages **NVIDIA RTX 3050** (CUDA 12.1) for high-speed vectorization and training.
* **SBERT Embeddings**: Uses `all-MiniLM-L6-v2` to convert unstructured email text into 384-dimensional dense vectors.
* **Fingerprinting**: Implements a Deep **Autoencoder (AE)** trained exclusively on benign data to establish a behavioral baseline.
* **Threshold Tuning**: Optimized detection sensitivity to maximize **Recall**, catching nearly 4x more attacks than baseline configurations.

---

## 🚀 Technical Workflow
### 1. Vectorization (Digital Fingerprinting)
We processed over **313,176 records** from the Enron dataset. Using GPU acceleration, we achieved an encoding rate of **~13.36 it/s**, reducing processing time from hours to minutes.

### 2. Autoencoder Architecture
The model uses a symmetric bottleneck architecture to compress email features into a 32-dimensional latent space:
- **Encoder**: 384 → 128 → 64 → 32 (The Fingerprint)
- **Decoder**: 32 → 64 → 128 → 384 (Reconstruction)

### 3. Anomaly Detection Logic
Detection is based on **Reconstruction Error (MSE)**. Legitimate emails match the fingerprint (Low Error), while spear-phishing attempts deviate (High Error).

---

## 📊 Results & Evaluation
Our final model was tuned from the 95th to the **70th percentile** to prioritize the detection of high-risk threats.

| Metric | Initial (Strict) | Tuned (Optimized) |
| :--- | :--- | :--- |
| **Recall (Detection Rate)** | 11.47% | **43.51%** |
| **False Positive Rate (FPR)** | 2.13% | 24.01% |
| **False Negatives (Missed)** | 26,352 | **16,816** |

> **Strategic Note:** We prioritized **Recall** to minimize the "False Negative" penalty, as missing a single spear-phishing attack carries a significantly higher security cost than a false alarm.

---

## 🛠️ Setup & Installation
### Prerequisites
* **OS**: Windows 10/11
* **Hardware**: NVIDIA GPU (RTX 30-series recommended)
* **Environment**: Anaconda (Python 3.12)

### Installation
```bash
# Create environment
conda create -n cyber_ai python=3.12 -y
conda activate cyber_ai

# Install CUDA-enabled PyTorch
pip install torch torchvision torchaudio --index-url [https://download.pytorch.org/whl/cu121](https://download.pytorch.org/whl/cu121)

# Install requirements
pip install sentence-transformers pandas seaborn scikit-learn
