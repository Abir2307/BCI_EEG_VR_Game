# satsnet_unity_bridge_request.py
import os
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import socket

# ---- Fix old .keras model loading ----
os.environ["TF_USE_LEGACY_KERAS"] = "1"

# ---- Load SATS-Net model ----
model_path = "best_SATS_NET_model_p300.keras"
model = load_model(model_path, compile=False, safe_mode=False)
print("SATS-Net model loaded successfully.")

# ---- UDP server setup ----
UDP_IP = "127.0.0.1"
UDP_PORT = 5055
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("Waiting for Unity requests for attention score...")

def get_fake_eeg():
    # Replace with real EEG preprocessing if available
    eeg_sample = np.random.rand(1, 100, 8, 1).astype(np.float32)
    return eeg_sample

try:
    while True:
        # Wait for Unity request
        data, addr = sock.recvfrom(1024)
        request = data.decode("utf-8")
        
        if request == "REQUEST_ATTENTION":
            eeg_input = get_fake_eeg()
            prediction = model.predict(eeg_input, verbose=0)
            attention_score = float(prediction[0][1])
            attention_score = max(0.0, min(1.0, attention_score))
            
            # Send back attention score
            sock.sendto(f"{attention_score:.4f}".encode("utf-8"), addr)

except KeyboardInterrupt:
    print("Bridge stopped manually.")

finally:
    sock.close()