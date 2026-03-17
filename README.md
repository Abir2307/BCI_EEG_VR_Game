# BCI Attention Training Game

## Overview

This project is a Brain-Computer Interface (BCI) based attention training system that integrates an EEG deep learning model with a Unity-based interactive stimulus game.
The system predicts user attention levels from EEG signals using a trained SATS-Net model and adapts the stimulus speed in real time.

The objective is to train and evaluate user attention through reaction-time based stimuli while monitoring brain activity.

---

## System Architecture

EEG Signal
→ Deep Learning Model (SATS-Net `.keras`)
→ Python Bridge (UDP Sender)
→ Unity Game (UDP Receiver)
→ Adaptive Stimulus + Reaction Analysis

The Python bridge continuously predicts an attention score and sends it to Unity via UDP.
Unity receives the score and adjusts stimulus timing dynamically.

---

## Project Structure

```
BCI_Project
│
├── run_bci_game.bat
│
├── BCI_Game
│   └── EEG_VR_Rehab_Prototype.exe
│
└── BCI_Unity_Bridge
    ├── satsnet_unity_bridge.py
    └── SATS_Net_model.keras
```

---

## Features

* EEG attention prediction using a deep learning model
* Real-time communication between Python and Unity via UDP
* Adaptive stimulus timing based on attention score
* Reaction time measurement
* Performance analysis across stimulus intervals
* Simple game-based attention training interface

---

## Requirements

### Software

* Python 3.8+
* Unity (for development only)
* Windows OS

### Python Libraries

```
tensorflow
numpy
socket
```

Install dependencies:

```
pip install tensorflow numpy
```

---

## Running the System

1. Ensure the EEG model file is present:

```
SATS_Net_model.keras
```

2. Run the batch launcher:

```
run_bci_game.bat
```

This will automatically:

* Start the Python EEG bridge
* Launch the Unity game

---

## Game Instructions

1. A stimulus will flash randomly on the screen.
2. Press **SPACE** as quickly as possible when you see the stimulus.
3. Reaction time is recorded.
4. The system adjusts stimulus speed based on your attention level.
5. After the experiment completes, performance statistics are displayed.

---

## Output Metrics

The system records:

* Reaction Time (RT)
* Correct Responses
* Performance per stimulus interval
* Attention score from EEG model

Example output:

```
Interval Performance
0.4s : 5/8 correct
0.8s : 6/10 correct
1.2s : 4/7 correct
```
