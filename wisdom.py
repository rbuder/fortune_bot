#!/usr/bin/python

import fortune
import os
import random
import config
import codecs

def dbs():
    fortunes = []
    for file in os.listdir(config.REPOPATH):
        if file.endswith(".dat"):
            pass
        elif file.endswith(".u8"):
            pass
        else:
            fortunes.append(os.path.join(config.REPOPATH, file))
    for file in os.listdir(f"{config.REPOPATH}/off"):
        if file.endswith(".dat"):
            pass
        elif file.endswith(".u8"):
            pass
        else:
            fortunes.append(os.path.join(f"{config.REPOPATH}/off", file))
    return fortunes

def get_random_fortune_db():
    fortune_dbs = dbs()
    try:
        r = random.SystemRandom()
    except:
        r = random

    return fortune_dbs[r.randint(0, len(fortune_dbs)-1)]

def get_fortune(random=True, db=None):
    if random:
        return fortune.get_random_fortune(get_random_fortune_db())
    else:
        return fortune.get_random_fortune(db)
