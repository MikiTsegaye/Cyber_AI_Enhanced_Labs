# Unsupervised Semantic Anomaly Detection Pipeline

## Autoencoders, Sentence Transformers, and Explainable AI (XAI) for Phishing Defense

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red)
![MITRE](https://img.shields.io/badge/MITRE-T1566-orange)

---

## 📝 Overview
This project implements a **Proof-of-Concept (POC)** offline pipeline designed to detect advanced "Spear Phishing" attacks. Unlike traditional systems that rely on signatures or blacklisted URLs, this system analyzes the **actual semantic meaning** of email content to identify anomalies.

By training a deep **Autoencoder** on text embeddings of "normal" business communications, the model can flag semantic deviations (social engineering attempts) without requiring labeled attack data (enabling Zero-Day detection).

---

## 🎯 The Problem: The Semantic Gap
Traditional phishing filters rely on static rules:
* Checking known malicious URLs.
* Flagging specific keywords (e.g., "Free money", "Prince of Nigeria").

**The Gap:** Modern attacks (MITRE **T1566**) use sophisticated natural language and social engineering to bypass these static filters. There is a critical need for systems that detect **behavioral and semantic anomalies** rather than just matching rules.

---

## 📐 Architecture & Methodology

The pipeline follows a robust unsupervised learning approach: 

### 1. Feature Engineering (Semantic Embeddings)
* **Tool:** Utilization of **Sentence Transformers** (e.g., `all-MiniLM-L6-v2`) from HuggingFace.
* **Process:** Raw email subjects and bodies are converted into dense vector embeddings.
* **Benefit:** This captures the *context* and *intent* (the semantics) of the message, not just word frequency, providing a highly nuanced representation of the text.

### 2. The Model (Deep Autoencoder)
* **Architecture:** Deep Autoencoder implemented in **PyTorch**.
* **Training Strategy:** The model is trained **exclusively on normal traffic**. It learns to reconstruct the low-error patterns of "safe" business language.
* **Inference (Anomaly Detection):** When a phishing email is processed, the model, unfamiliar with the malicious semantic pattern, **fails to reconstruct it accurately**. This results in a **High Reconstruction Error**—the anomaly score. 

### 3. Explainability (XAI)
* **UMAP:** Used for high-dimensional dimensionality reduction to visually cluster and inspect the physical separation between the "Normal" cluster and "Phishing" outliers in 2D or 3D space.
* **SHAP (SHapley Additive exPlanations):** Used for local feature importance analysis to explain *why* a specific email was flagged (e.g., explaining semantic features related to "Urgency" or "Unusual Request").

---

## ⚙️ Tech Stack

* **Language:** Python
* **Deep Learning Framework:** PyTorch 
* **NLP & Embeddings:** HuggingFace SentenceTransformers
* **Acceleration:** NVIDIA RAPIDS (cuML/cuDF) for GPU-accelerated embedding generation and model training/inference.
* **Visualization & XAI:** Matplotlib, Seaborn, UMAP, SHAP

---

## ✅ Project Scope

### Project Boundaries
* Generation of a synthetic dataset (Normal vs. Semantic Phishing).
* Unsupervised Anomaly Detection using Reconstruction Error as the anomaly score.
* GPU Acceleration for embedding generation and training efficiency.
* Visualization and Explainability of detection results (UMAP & SHAP).

---

## 📚 References
* [MITRE ATT&CK T1566 (Phishing)](https://attack.mitre.org/techniques/T1566/)
* [SentenceTransformers Documentation](https://www.sbert.net/)
* [Kaggle - Phishing Email Dataset](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset)
