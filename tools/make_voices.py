# Generates the voice-over for Castle Grimhold with Piper (offline neural TTS).
# Setup:  pip install piper-tts numpy
#         python -m piper.download_voices --download-dir tools/voice_models cs_CZ-jirka-medium de_DE-thorsten_emotional-medium de_DE-thorsten-high de_DE-karlsson-low
# Run from anywhere:  python tools/make_voices.py   (needs ffmpeg on PATH)
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
}
LINES = [
    # intro: capture in the woods
    ('bj_01', 'bj', 'Tady Orel. Jsem na místě. Hrad Grimhold je hned za hřebenem.'),
    ('lon_01', 'lon', 'Rozumím, Orle. Buďte opatrný. Hory jsou plné hlídek.'),
    ('off_01', 'offA', 'Hände hoch! Keine Bewegung!', 'Ruce vzhůru! Ani hnout!'),
    ('off_02', 'off', 'Ein amerikanischer Spion. Ganz allein in unseren Bergen.', 'Americký špion. Úplně sám v našich horách.'),
    ('bj_02', 'bj', 'Jen jsem si tu sbíral houby.'),
    ('off_03', 'offM', 'Der Doktor wird sich freuen. Bringt ihn nach Grimhold!', 'Doktor bude mít radost. Odveďte ho na Grimhold!'),
    # intro: the cell
    ('grd_01', 'grd', 'Aufstehen, Ami! Der Doktor will dich sehen.', 'Vstávej, Amíku! Doktor tě chce vidět.'),
    ('bj_03', 'bj', 'Doktor si bude muset počkat.'),
    ('bj_04', 'bj', 'Revolver a klíče. A teď ven z téhle díry.'),
    # episode 2: down the cable car
    ('bj_05', 'bj', 'Londýne, tady Orel. Jsem venku z Grimholdu. Mám plány i Zemanův deník.'),
    ('lon_02', 'lon', 'Výborně, Orle. A co je v tom deníku?'),
    ('bj_06', 'bj', 'Wolfsgrund. Podzemní továrna, kam vede jen železnice. Tam stavějí Finsternis.'),
    ('lon_03', 'lon', 'Pak tam musíte vy. Spojka odboje na vás čeká v hájovně nad údolím. Hodně štěstí.'),
    ('bj_07', 'bj', 'Štěstí si nechte, plukovníku. Mně stačí náboje.'),
    # episode 3: the ramp at Wolfsgrund
    ('zem_01', 'zem', 'Der Übersoldat Mark Zwei ist bereit, Standartenführer. Wir müssen ihn nur noch wecken.', 'Übersoldat Mk II je připraven, Standartenführere. Stačí ho jen probudit.'),
    ('off_04', 'off', 'Und die Raketen, Herr Doktor?', 'A rakety, pane doktore?'),
    ('zem_02', 'zem', 'In drei Tagen fliegt die erste nach London.', 'Za tři dny poletí první na Londýn.'),
    ('bj_08', 'bj', 'Za tři dny. To mám času dost.'),
    # finale
    ('lon_04', 'lon', 'Orle, tady Londýn. Slyšíte nás? Seismografy ve Švýcarsku právě zaznamenaly zemětřesení.'),
    ('bj_09', 'bj', 'To nebylo zemětřesení, Londýne. To byl Wolfsgrund. Operace Finsternis skončila.'),
    ('lon_05', 'lon', 'Skvělá práce, Orle. Je čas vrátit se domů.'),
    ('bj_10', 'bj', 'Domů. To zní dobře.'),
    # in-game: Zeman and B.J.
    ('zem_03', 'zem', 'Wachen! Haltet ihn auf!', 'Stráže! Zastavte ho!'),
    ('bj_obj1', 'bj', 'Mám to.'), ('bj_obj2', 'bj', 'Další odškrtnuto.'), ('bj_obj3', 'bj', 'Tohle se bude v Londýně hodit.'),
]
BARKS = {
    'sus': [('Was war das?', 'surprised'), ('Hallo? Ist da jemand?', 'surprised'), ('Hm? Wer ist da?', 'neutral'), ('Da hat sich was bewegt.', 'neutral')],
    'alert': [('Alarm!', 'angry'), ('Da ist er!', 'angry'), ('Halt! Stehen bleiben!', 'angry'), ('Feind gesichtet!', 'angry')],
    'body': [('Mein Gott, ein Toter!', 'surprised'), ('Hier liegt einer! Alarm!', 'angry')],
    'lost': [('Nichts. Muss der Wind gewesen sein.', 'neutral'), ('Nur eine Ratte.', 'neutral'), ('Ich sehe niemanden.', 'neutral')],
}
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
out = {}; subs = {}
for L in LINES:
    lid, spk, text = L[0], L[1], L[2]
    out[lid] = synth(lid, spk, text); subs[lid] = (spk, L[3] if len(L) > 3 else text)
for kind, lst in BARKS.items():
    for vi, v in enumerate('ABC'):
        for i, (text, emo) in enumerate(lst):
            lid = f'bark_{kind}_{v}{i}'; out[lid] = synth(lid, v, text, emo)
js = ['/* Castle Grimhold - voice-over (Piper neural TTS: voices "jirka" (cs), "thorsten" & "thorsten_emotional" (de, CC0), "karlsson" (de)). Generated by make_voices.py */', 'window.CASTLE_VOX = {']
for lid, f in out.items(): js.append(f' "{lid}": "{base64.b64encode(open(f, "rb").read()).decode()}",')
js[-1] = js[-1].rstrip(','); js.append('};')
open(os.path.join(ROOT, 'assets', 'voices.js'), 'w', encoding='utf-8').write('\n'.join(js) + '\n')
json.dump(subs, open(os.path.join(ROOT, 'tools', 'subs.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(os.path.getsize(f) for f in out.values()); print(len(out), 'clips', tot // 1024, 'KB')
