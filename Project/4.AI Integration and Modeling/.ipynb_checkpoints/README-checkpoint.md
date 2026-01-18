# 🛡️ Morpheus Spear Phishing Detection (Enron Corpus)
**Group 7 | NVIDIA AI-Enhanced Cybersecurity Project**

This project implements an AI-native cybersecurity pipeline using the **NVIDIA Morpheus** framework principles. It leverages Unsupervised Deep Learning (Autoencoders) to detect sophisticated spear-phishing attempts that bypass traditional signature-based security.

---

## 💻 Environment & Hardware
To satisfy the computational demands of processing 400k+ records, this project utilizes dedicated GPU acceleration:
* **GPU**: NVIDIA GeForce RTX 3050 (4GB VRAM)
* **CUDA Version**: 12.1
* **Compute Performance**: Achieved ~13.36 it/s during vectorization.
* **Kernel**: Python 3.12 (Cyber_AI Environment)

---

## 🛠️ Technical Implementation

### 1. Stage 5.1: High-Speed Vectorization
Using the `all-MiniLM-L6-v2` SentenceTransformer, we converted unstructured email text into 384-dimensional dense vectors.
* **Training Set**: 313,176 Normal records
* **Test Set**: 96,877 Mixed records

### 2. Stage 5.2: Deep Autoencoder (Fingerprinting)
We built a multi-layer Autoencoder to learn the mathematical "fingerprint" of legitimate Enron communication. 
- **Architecture**: Symmetric Bottleneck (384 → 128 → 64 → 32 → 64 → 128 → 384)
- **Training**: 20 Epochs on **Normal-only** data.
- **Final Reconstruction Loss**: `0.001166` (Proving high-fidelity fingerprinting).

### 3. Stage 5.3: Anomaly Detection & Strategic Tuning
Detection is triggered by **Reconstruction Error (MSE)**. If an email cannot be reconstructed by the "Fingerprint," it is flagged as an anomaly.

---

## 📊 Final Performance Metrics (Group 7 Results)
In accordance with the project rubric, we prioritized **Recall** (Detection Rate) to minimize **False Negatives** (Missed Attacks).

| Metric | Initial (Strict 95th) | Tuned (Morpheus 70th) |
| :--- | :--- | :--- |
| **Recall (Detection Rate)** | 11.47% | **43.51%** |
| **False Positive Rate (FPR)** | 2.13% | 24.01% |
| **False Negatives (Missed)** | 26,352 | **16,816** |

**Observation:** By shifting the anomaly threshold from the 95th to the 70th percentile, we successfully caught an additional **9,536 spear-phishing attempts**.

---

## 🧠 Explainable AI (xAI)
For every alert, Morpheus provides a quantitative reason. In our model, the **MSE Anomaly Score** represents the degree of deviation from the learned business norm. 
- **High Error**: Indicates language, urgency, or intent that does not exist in the legitimate Enron fingerprint.

---

## 📂 Project Structure
- `05_Morpheus_Phishing_Detection_AE.ipynb`: Main modeling & tuning notebook.
- `Splited_data/`: Cleaned and split datasets (Train/Val/Test).
- `models/`: Saved weights for the SpearPhishingAE.
