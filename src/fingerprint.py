import hashlib
from scipy.ndimage import maximum_filter
import numpy as np

def find_peaks(Sxx,f,t):
    local_max = (Sxx == maximum_filter(Sxx, footprint=np.ones((10,10))))
    freqs, times = np.where(local_max)
    return list(zip(f[freqs], t[times]))

def gen_hashes(peaks):
    hashes=[]
    for i in range(len(peaks)-1):
        f1,t1 = peaks[i]
        f2,t2 = peaks[i+1]
        t_delta = t2-t1
        hash_val = hashlib.sha1(f"{f1}{f2}{t_delta}".encode()).hexdigest()[:20]
        hashes.append((hash_val,t1))
    return hashes