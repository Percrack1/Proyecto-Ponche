import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

y, sr = librosa.load('Fisica/audio.mp3')

plt.figure(figsize=(10,4))
librosa.display.waveshow(y, sr=sr)
plt.title('Forma de Onda: Amplitud en el tiempo')
plt.show()

D = librosa.stft(y)
S_db = librosa.amplitude_to_db(abs(D), ref=np.max)

plt.figure(figsize=(10,4))
librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='hz')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de Frecuencias')
plt.show()

y_harmonic, y_percussive = librosa.effects.hpss(y)