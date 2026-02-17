# Realtime Local Speech Recognition (Offline ASR)

A fully offline real-time speech recognition system using Faster-Whisper.
The application listens to the microphone and transcribes speech live without any internet connection or cloud APIs.

## Features

* Realtime microphone transcription
* Works offline
* Supports English and Persian
* Voice activity detection
* Low-latency streaming
* CPU compatible (no GPU required)

## Use Cases

* Meeting transcription
* Factory voice commands
* Accessibility captions
* Privacy-sensitive environments

## Installation

pip install -r requirements.txt

## Run

python main.py

## Notes

The model is downloaded automatically on first run.

## Why Offline?

Many companies cannot send audio data to external services due to GDPR and privacy policies.
This project demonstrates an on-device speech interface suitable for enterprise deployment.

## Demonstration

Run the program and speak — text will appear in real time.

This repository is a clean-room demonstration inspired by real-world embedded and industrial speech interfaces.
