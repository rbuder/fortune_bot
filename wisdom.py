#!/usr/bin/python

import fortune
import os
import random
import config
import codecs

def dbs(off=False):
    fortunes = []
    for file in os.listdir(config.REPOPATH):
        if file.endswith(".dat"):
            pass
        elif file.endswith(".u8"):
            pass
        else:
            fortunes.append(os.path.join(config.REPOPATH, file))
    if off == True:
        for file in os.listdir(f"{config.REPOPATH}/off"):
            if file.endswith(".dat"):
                pass
            elif file.endswith(".u8"):
                pass
            else:
                fortunes.append(os.path.join(f"{config.REPOPATH}/off", f"off/{file}"))
    return fortunes

def get_random_fortune_db():
    fortune_dbs = dbs(off=False)
    try:
        r = random.SystemRandom()
    except:
        r = random

    return fortune_dbs[r.randint(0, len(fortune_dbs)-1)]

def get_fortune(random=True, db=None):
    if random:
        quote = fortune.get_random_fortune(get_random_fortune_db())
    else:
        quote = fortune.get_random_fortune(db)
        quote = codecs.decode(quote, 'rot_13')
    return quote