from database import get_matches

def match_audio(hashes):
    results = []
    for hash,_ in hashes:
        matches=get_matches(hash)
        results.extend(matches)

    if results:
        song_cnts = {}
        for result in results:
            song_id,_ = result.decode().split(':')
            if song_id in song_cnts:
                song_cnts[song_id]+=1
            else:
                song_cnts[song_id]=1
            
            return max(song_cnts,key=song_cnts.get)
        
    return "No match found"
