# AI-Based Email Fraud Detection System

A rule-based phishing detection system that analyzes email text and image-based emails to detect potential fraud using keyword risk scoring, suspicious link detection, and OCR-based text extraction.

---

## 📖 Project Overview

This project is a cybersecurity-focused web application built using Python and Flask. It detects phishing or fraudulent emails by analyzing:

- Urgency and fear-based language
- Banking and account scam patterns
- Money and lottery-related scams
- Government or authority impersonation
- Suspicious URLs and attachments
- Suspicious formatting patterns
- Image-based phishing emails using OCR

The system classifies emails into:

- ✅ Safe
- ⚠ Suspicious
- 🚨 High Risk

---

## 🧠 Technologies Used

### Backend
- Python
- Flask

### Text Processing
- Regular Expressions (re)
- collections (Counter)

### OCR & Image Processing
- OpenCV
- pytesseract
- Tesseract OCR Engine

---

## 🏗 Project Structure
