## Multi-Mode Speech-to-Text (S2T) System
This repository showcases an advanced Speech-to-Text pipeline featuring two distinct implementation strategies: Static File Transcription via high-fidelity APIs and Real-Time Live Transcription using on-device AI models.

## System Overviews
## 1. Simple S2T (API-Driven)
A streamlined module designed for processing pre-recorded audio files with high accuracy. It leverages AssemblyAI's Universal Models to handle complex audio environments, multiple speakers, and automatic language detection.

 Core Script: main.py

 Key Features: Speaker diarization (labels), multi-model support (universal-3-pro), and seamless cloud integration.

 Input Format: Supports various formats including .m4a.

## 2. Live S2T (Edge AI)
A complex, real-time transcription engine built for low-latency feedback. It uses OpenAI's Whisper (Base) model running locally to transcribe speech directly from a microphone input.

Core Script: live_main.py

Key Features: Ambient noise adjustment, phrase-time limiting for real-time responsiveness, and automated history logging with timestamps.

Persistence: All transcriptions are saved locally to transcription_history.txt.

## Technical Stack
AI Models: OpenAI Whisper (Base), AssemblyAI Universal 3 Pro.

Audio Processing: SpeechRecognition, static_ffmpeg, PyAudio.

Programming: Python 3.x.