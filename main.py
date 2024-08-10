#!/bin/python3

import json

from x3 import vkk, kkv, kvk
from x4 import kkvk
from x5 import kvkvk
from x6 import kvkkvk

def save_to_json(data, filename):

    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)


def match_pattern(word, pattern):

    if len(word) != len(pattern):
        return False

    w_pattern = tuple(c in 'aeiu' for c in word)
    p_pattern = tuple(c == 'v' for c in pattern)

    return w_pattern == p_pattern



verbs = ['ban','del','cuq','ɣez','sel','qim']

asefti = {}

for verb in verbs:
    try:
        if len(verb) == 3:
        
            if match_pattern(verb, 'vkk'):
                conj = vkk(verb)
            elif match_pattern(verb, 'kkv'):
                conj = kkv(verb)
            elif match_pattern(verb, 'kvk'):
                conj = kvk(verb)
            else:
                raise ValueError(f"ca wer yelli d wenni i '{verb}'")
        
        elif len(verb) == 4:
        
            if match_pattern(verb, 'kkvk'):
                conj = kkvk(verb)
            else:
                raise ValueError(f"ca wer yelli d wenni i '{verb}'")
        
        elif len(verb) == 5:
        
            if match_pattern(verb, 'kvkvk'):
                conj = kvkvk(verb)
            else:
                raise ValueError(f"ca wer yelli d wenni i '{verb}'")
        
        elif len(verb) == 6:
            
            if match_pattern(verb,'kvkkvk'):
                conj = kvkkvk(verb)
            else:
                raise ValueError(f"ca wer yelli d wenni i '{verb}'")
        
        else:
            raise ValueError(f"'{verb}' wer ɣers bu wemkan")

                
        asefti[verb] = conj
    except ValueError as e:
        print(e)


save_to_json(asefti, 'asefti.json')
