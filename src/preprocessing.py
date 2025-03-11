import librosa
import numpy as np
from scipy.signal import spectrogram

_sr=44100
_nperseg=2048
_noverlap=1024
_nfft=2048

def load_audio(path,sr=_sr):
    y,sr = librosa.load(path,sr=sr,mono=True)
    return y,sr

def make_spectogram(y,sr):
    f,t,Sxx = spectrogram(y,fs=sr,nperseg=_nperseg,noverlap=_noverlap,nfft=_nfft)
    return f,t,Sxx