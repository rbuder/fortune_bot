#!/usr/bin/python

import fortune
import os
import random
import config

def dbs():
    fortunes = []
    for file in os.listdir(config.REPOPATH):
        if file.endswith(".dat"):
            pass
        else:
            fortunes.append(os.path.join(config.REPOPATH, file))
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
