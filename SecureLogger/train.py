import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load human keystroke data
if not os.path.exists("keystroke_data.npy"):
    print("Error: No human keystroke data found. Run main.py first.")
    exit()

human_data = np.load("keystroke_data.npy")

# Load bot-generated keystroke data
if not os.path.exists("bot_keystroke_data.npy"):
    print("Error: No bot keystroke data found. Run bot_data_generator.py first.")
    exit()

bot_data = np.load("bot_keystroke_data.npy")

# Label the data: 0 = Human, 1 = Bot
human_labels = np.zeros(len(human_data))
bot_labels = np.ones(len(bot_data))

# Combine datasets
X = np.vstack((human_data, bot_data))
y = np.hstack((human_labels, bot_labels))

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train AI Model
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

# Save trained model
joblib.dump(clf, "keystroke_model.pkl")

print("AI model trained and saved as keystroke_model.pkl")
