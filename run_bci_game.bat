@echo off
echo Starting SATS-Net EEG Bridge...

cd /d E:\BCI_Project\BCI_Unity_Bridge
start cmd /k python satsnet_unity_bridge.py

timeout /t 3

echo Launching Unity Game...

cd /d E:\BCI_Project\BCI_GamePlay
start EEG_VR_Rehab_Prototype.exe

echo System started.