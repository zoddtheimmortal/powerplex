from preprocessing import load_audio, make_spectogram
from fingerprint import find_peaks, gen_hashes
from database import store, clear_db
from match import match_audio

def find_music(path):
    y,sr=load_audio(path)
    f,t,Sxx=make_spectogram(y,sr)
    peaks = find_peaks(Sxx,f,t)
    hashes = gen_hashes(peaks)

    return match_audio(hashes)


def add_song(path,song_id):
    print(f"Adding song to database: {song_id}")

    y,sr=load_audio(path)
    f,t,Sxx=make_spectogram(y,sr)
    peaks = find_peaks(Sxx,f,t)
    hashes = gen_hashes(peaks)

    store(hashes,song_id)
    print(f"Song added to database: {song_id}")

if __name__ == "__main__":
    add_song("./data/main_audio.mp3","duvet")

    song_id = find_music("./data/audio_cover.mp3")
    print(song_id)

    clear_db()