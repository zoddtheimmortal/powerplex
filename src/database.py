import redis

db=redis.Redis(host='localhost',port=6379,db=0)

def store(hashes,song_id):
    for hash_val,time in hashes:
        db.sadd(hash_val,f"{song_id}:{time}")

def get_matches(hash_val):
    return list(db.smembers(hash_val))

def clear_db():
    db.flushall()