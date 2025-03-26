# 🔐 SecureLogger - AI-Enhanced Keystroke Monitoring & Protection

SecureLogger is an advanced cybersecurity tool designed to securely log keystrokes while utilizing AI-based analysis to detect bot-generated inputs. With integrated encryption and machine learning, this project enhances security by preventing unauthorized monitoring and automating bot detection.

---

## 📌 Project Overview

SecureLogger is a **keylogging and bot-detection system** that records keystroke dynamics while ensuring data security through **AES encryption**. It leverages **machine learning models** to classify human vs. bot typing behavior based on keystroke timing, making it an essential tool for **cybersecurity analysis and AI-based user behavior detection**.

---

## 📊 Keystroke Dataset Information

- *Generated From:* Real human keystrokes + synthetic bot keystrokes
- *Collected Features:*
  - Keystroke timing (hold time)
  - Key sequences
  - Typing speed variations

Dataset preprocessing included:
- Removing noisy data
- Generating synthetic bot keystroke patterns

---

## 🤖 Machine Learning Models Used

- ✅ Random Forest Classifier

---

## 🔐 Security Features

- **AES Encryption:** Keystroke logs are encrypted before storage.
- **Automatic Log Clearance:** Ensures fresh logs in every session.
- **AI-Powered Bot Detection:** Differentiates human typing from bots.
- **Real-time Keystroke Logging:** Stores data in `.txt`, `.csv`, and `.enc` formats.

---

## 💻 Tech Stack

- **Python** (pynput, numpy, pandas, scikit-learn)
- **Machine Learning** (RandomForest, joblib)
- **Cybersecurity Libraries** (PyCryptodome for AES encryption)

---

## 🚀 Features

- **Real-time Key Logging**: Captures keystrokes with precise timing.
- **Encrypted Storage**: Logs are stored securely using AES.
- **Machine Learning Model**: AI classifies human vs. bot activity.
- **Automatic Log Management**: Prevents logs from accumulating across sessions.

---

## 🔥 How It Works

1. **Keystrokes are recorded** with their hold time.
2. **Data is encrypted** before being written to log files.
3. **AI model analyzes** keystroke dynamics to detect bots.
4. **Logs are automatically cleared** after every restart for security.

---

## 🙌 Acknowledgements

- Python Community & Open-Source Contributors  
- Scikit-learn for ML Model Implementation  
- PyCryptodome for AES Encryption  

---

🔒 **Enhancing Cybersecurity with AI and Encryption!**  

## 📜 License

This project is licensed under the [MIT License](./LICENSE).  

---

💡 *Stay Secure, Stay Smart! Protect your data with AI-powered monitoring.* 🚀  
