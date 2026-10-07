# Generates the voice-over for Castle Grimhold with Piper (offline neural TTS).
# Setup:  pip install piper-tts numpy
#         python -m piper.download_voices --download-dir tools/voice_models cs_CZ-jirka-medium de_DE-thorsten_emotional-medium de_DE-thorsten-high de_DE-karlsson-low
# Run from anywhere:  python tools/make_voices.py             (needs ffmpeg on PATH; regenerates everything)
#                     python tools/make_voices.py --missing   (only clips that have no mp3 yet, e.g. new expansion lines)
# The models can also be taken from the sherpa-onnx GitHub release (tts-models/vits-piper-<name>.tar.bz2): the .onnx + .onnx.json inside.
# Each line: id, voice, text (spoken), subtitle (Czech), options. Writes assets/voices/*.mp3 + assets/voices.js
import os, sys, json, wave, subprocess, base64
import numpy as np
from piper import PiperVoice, SynthesisConfig

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, 'tools', 'voice_models')
OUT = os.path.join(ROOT, 'assets', 'voices')
FF = 'ffmpeg'
os.makedirs(OUT, exist_ok=True)
M = {k: os.path.join(HERE, v) for k, v in {'cs': 'cs_CZ-jirka-medium.onnx', 'emo': 'de_DE-thorsten_emotional-medium.onnx', 'th': 'de_DE-thorsten-high.onnx', 'ka': 'de_DE-karlsson-low.onnx'}.items()}
EMO = {'amused': 0, 'angry': 1, 'disgusted': 2, 'drunk': 3, 'neutral': 4, 'sleepy': 5, 'surprised': 6, 'whisper': 7}
# speaker presets: model, speaker id, length scale, pitch factor, extra ffmpeg filter
SPK = {
    'bj':  ('cs', None, 1.0, .93, 'bass=g=3'),
    'lon': ('cs', None, 1.06, .86, 'highpass=f=380,lowpass=f=2900,compand=attacks=0.02:decays=0.2:points=-80/-80|-30/-15|0/-6,volume=1.4'),
    'off': ('emo', 'neutral', 1.05, .9, ''),
    'offA': ('emo', 'angry', 1.0, .9, ''),
    'offM': ('emo', 'amused', 1.05, .9, ''),
    'grd': ('th', None, .98, 1.04, ''),
    'zem': ('ka', None, 1.12, .88, 'aecho=0.8:0.55:45:0.22'),
    # bark voices: A = Thorsten (emotional), B = Karlsson, C = Thorsten high, pitched up
    'A': ('emo', 'neutral', 1.0, .97, ''), 'B': ('ka', None, 1.0, .95, ''), 'C': ('th', None, .95, 1.1, ''),
    # expansion: Gefreiter Brandt, Feldwebel Krüger (calm / shouting), the castle loudspeaker, Kessler and the squad
    'brn': ('th', None, 1.02, .95, 'bass=g=2'), 'krg': ('emo', 'neutral', 1.04, .84, 'bass=g=3'), 'krgA': ('emo', 'angry', 1.0, .86, 'bass=g=3'),
    'lsp': ('emo', 'angry', 1.0, .9, 'highpass=f=450,lowpass=f=3200,aecho=0.8:0.6:140:0.3,volume=1.6'),
    'kes': ('ka', None, 1.0, 1.02, ''), 'mul': ('ka', None, .97, 1.07, ''), 'web': ('th', None, .95, 1.13, ''), 'hof': ('emo', 'neutral', 1.0, 1.06, ''),
    # Czech-speaking prisoners and partisans
    'P': ('cs', None, .95, 1.0, ''), 'Q': ('cs', None, 1.0, .87, ''),
}
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from voice_lines import LINES, BARKS, CZ_BARKS
voices = {}
def voice(k):
    if k not in voices: voices[k] = PiperVoice.load(M[k])
    return voices[k]
def synth(lid, spk, text, emo=None):
    mk, sid, ls, pitch, flt = SPK[spk]
    if emo is not None and mk == 'emo': sid = emo
    cfg = SynthesisConfig(speaker_id=EMO[sid] if isinstance(sid, str) else sid, length_scale=ls, noise_scale=.6, noise_w_scale=.75)
    wav = os.path.join(HERE, 'out_' + lid + '.wav')
    with wave.open(wav, 'wb') as wf: voice(mk).synthesize_wav(text, wf, syn_config=cfg)
    with wave.open(wav, 'rb') as wf: sr = wf.getframerate(); a = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32)
    loud = np.where(np.abs(a) > 300)[0]
    if len(loud): a = a[max(0, loud[0] - int(sr * .03)): loud[-1] + int(sr * .08)]
    a = np.concatenate([a, np.zeros(int(sr * .15), np.float32)])
    with wave.open(wav, 'wb') as wf: wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(sr); wf.writeframes(np.clip(a, -32767, 32767).astype(np.int16).tobytes())
    af = f'asetrate={int(sr * pitch)},aresample=22050,atempo={1 / pitch:.4f}' + (',' + flt if flt else '')
    mp3 = os.path.join(OUT, lid + '.mp3')
    subprocess.run([FF, '-y', '-loglevel', 'error', '-i', wav, '-af', af, '-ac', '1', '-ar', '22050', '-b:a', '40k', mp3], check=True)
    os.remove(wav); return mp3
def jobs():
    for L in LINES: yield L[0], L[1], L[2], None
    for kind, lst in BARKS.items():
        for v in 'ABC':
            for i, (text, emo) in enumerate(lst): yield f'bark_{kind}_{v}{i}', v, text, emo
    for kind, lst in CZ_BARKS.items():
        for v in 'PQ':
            for i, (text, emo) in enumerate(lst): yield f'czb_{kind}_{v}{i}', v, text, emo
missing = '--missing' in sys.argv
for lid, spk, text, emo in jobs():
    if missing and os.path.exists(os.path.join(OUT, lid + '.mp3')): continue
    print(lid, text); synth(lid, spk, text, emo)
# assets/voices.js: every clip on disk, plus the subtitles (speaker, Czech text)
subs = {L[0]: [L[1], L[3] if len(L) > 3 else L[2]] for L in LINES}
js = ['/* Blázen z Londýna – voice-over (Piper neural TTS: voices "jirka" (cs), "thorsten" & "thorsten_emotional" (de, CC0), "karlsson" (de)). Generated by tools/make_voices.py */', 'window.CASTLE_VOX = {']
n = 0
for lid, *_ in jobs():
    f = os.path.join(OUT, lid + '.mp3')
    if os.path.exists(f): js.append(f' "{lid}": "{base64.b64encode(open(f, "rb").read()).decode()}",'); n += 1
js[-1] = js[-1].rstrip(','); js.append('};')
js.append('window.CASTLE_VOX_SUB = ' + json.dumps(subs, ensure_ascii=False) + ';')
open(os.path.join(ROOT, 'assets', 'voices.js'), 'w', encoding='utf-8').write('\n'.join(js) + '\n')
json.dump(subs, open(os.path.join(ROOT, 'tools', 'subs.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(n, 'clips in assets/voices.js')
