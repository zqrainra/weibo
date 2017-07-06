import os
import random

def gen_default_head_img(path):
    for i in os.walk(path):
        if i[0] == path:
            return random.choice(i[-1])