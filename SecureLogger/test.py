import joblib
import numpy as np
import os

# Ensure model exists
if not os.path.exists("keystroke_model.pkl"):
    print("Error: AI model not found. Run train.py first.")
    exit()

# Load AI model
clf = joblib.load("keystroke_model.pkl")

# Ensure keystroke data exists
if not os.path.exists("keystroke_data.npy"):
    print("Error: No keystroke data found. Run main.py first.")
    exit()

# Load the latest keystroke data
keystroke_data = np.load("keystroke_data.npy")

if len(keystroke_data) == 0:
    print("Error: No keystroke data recorded.")
    exit()

latest_entry = keystroke_data[-1].reshape(1, -1)

# Predict bot vs. human
prediction = clf.predict(latest_entry)

if prediction[0] == 0:
    print("User is Human ✅")
else:
    print("User is a Bot 🤖")
