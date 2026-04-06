import requests
import assemblyai as aai

aai.settings.base_url = "https://api.assemblyai.com"
aai.settings.api_key = "f1d349d1a4064319a9ce005eb074bf96"

audio_file = "oyshe.m4a"

config = aai.TranscriptionConfig(
    speech_models=["universal-3-pro", "universal-2"],
    language_detection=True,
    speaker_labels=True,
)

transcript = aai.Transcriber().transcribe(audio_file, config=config)

if transcript.status == aai.TranscriptStatus.error:
    raise RuntimeError(f"Transcription failed: {transcript.error}")
print(f"\nFull Transcript:\n\n{transcript.text}")
