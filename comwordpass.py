#!/usr/bin/env python

import os
import json
import random


PATH_DIR__THIS = os.path.abspath(os.path.dirname(__file__))
PATH_DIR__DATA = os.path.join(PATH_DIR__THIS, 'data')
PATH_FILE__COMWORDS  = os.path.join(PATH_DIR__DATA, 'comwords.json')

NUM_WORDS = 4


def gen_password():
    with open(PATH_FILE__COMWORDS, 'r') as f_comwords:
        comwords = json.loads(f_comwords.read())
    password = ''.join([random.choice(comwords) for word in xrange(NUM_WORDS)])
    return password


if __name__ == '__main__':
    print gen_password()
