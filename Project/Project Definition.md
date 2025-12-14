# 🛡️ Actual Phishing Detection (T1566)

**An Unsupervised Anomaly Detection Pipeline using Autoencoders, Sentence Transformers, and Explainable AI (XAI).**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red)
![MITRE](https://img.shields.io/badge/MITRE-T1566-orange)

## 📋 Overview
This project implements a **Proof-of-Concept (POC)** offline pipeline designed to detect advanced "Spear Phishing" attacks. Unlike traditional systems that rely on signatures or blacklisted URLs, this system analyzes the **actual meaning** of email content to identify anomalies.

By training a deep **Autoencoder** on text embeddings of "normal" business communications, the model can flag semantic deviations (social engineering attempts) without requiring labeled attack data (Zero-Day detection).

## 🧐 The Problem
Traditional phishing filters rely on:
* Checking known malicious URLs.
* Flagging specific keywords (e.g., "Free money", "Prince of Nigeria").

**The Gap:** Modern attacks (MITRE **T1566**) use natural language and social engineering to bypass these filters. There is a critical need for systems that detect **behavioral and semantic anomalies** rather than just matching rules.

## 🏗️ Architecture & Methodology

The pipeline follows an unsupervised learning approach:

1.  **Feature Engineering (Embeddings)**
    * Utilization of **Sentence Transformers** (e.g., `all-MiniLM-L6-v2`) to convert raw email subjects and bodies into dense vector embeddings.
    * This captures the *context* and *intent* of the message, not just word frequency.

2.  **The Model (Autoencoder)**
    * **Architecture:** Deep Autoencoder implemented in PyTorch.
    * **Training Strategy:** Trained **exclusively on normal traffic**. The model learns to reconstruct "safe" business language.
    * **Inference:** When a phishing email is processed, the model fails to reconstruct the semantic pattern accurately, resulting in a **High Reconstruction Error**.

3.  **Explainability (XAI)**
    * **UMAP:** Dimensionality reduction to visualize the physical separation between "Normal" clusters and "Phishing" outliers.
    * **SHAP:** Feature importance analysis to explain *why* a specific email was flagged (e.g., "Urgency" detected in semantics).

## 🛠️ Tech Stack

* **Language:** Python
* **Deep Learning:** PyTorch 
* **NLP:** HuggingFace SentenceTransformers, the standard way to extract the context out of a text.
* **Acceleration:** NVIDIA RAPIDS (cuML/cuDF) for GPU-accelerated processing
* **Visualization:** Matplotlib, Seaborn, UMAP

## 🎯 Project Scope

### Project boundaries ✅
* Generation of a synthetic dataset (Normal vs. Semantic Phishing).
* Unsupervised Anomaly Detection using Reconstruction Error.
* GPU Acceleration for embedding generation and training.
* Visualization of detection results.


## 🔗 References
* [MITRE ATT&CK T1566 (Phishing)](https://attack.mitre.org/techniques/T1566/)
* [SentenceTransformers Documentation](https://www.sbert.net/)
* [Kaggle - Database](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset)


