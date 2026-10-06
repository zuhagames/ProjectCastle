@echo off
rem Regenerates the voice-over with natural Microsoft neural voices (needs internet, Python and ffmpeg)
cd /d %~dp0..
python -m pip install --upgrade edge-tts
python tools\make_voices_neural.py
pause
