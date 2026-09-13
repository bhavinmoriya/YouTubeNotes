import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import bilinear, freqz

# Load a WAV file (replace 'input.wav' with your file)
sample_rate, signal = wavfile.read('/content/synth.wav')
if len(signal.shape) > 1:
    signal = signal[:, 0]  # Use mono channel if stereo

# Normalize the signal
signal = signal.astype(float) / np.max(np.abs(signal))

# Time domain plot
time = np.arange(len(signal)) / sample_rate
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(time, signal)
plt.title("Time Domain Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Approximate Laplace transform using bilinear transform
# Define a simple low-pass filter as an example Laplace transform
b, a = bilinear([1], [1, 1], fs=sample_rate)  # Low-pass filter: H(s) = 1/(s+1)
w, h = freqz(b, a, fs=sample_rate)

# Frequency domain plot
plt.subplot(2, 1, 2)
plt.plot(w, np.abs(h))
plt.title("Frequency Response (Magnitude of Laplace Transform)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()

plt.tight_layout()
plt.savefig("LAPLACE.png")
plt.show()
