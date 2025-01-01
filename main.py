#!/bin/python3

import sys
import json

from x3 import vkk, kkv, kvk, vkv
from x4 import kkvk, kvkk, kvkv, vkvk, vkkv
from x5 import kvkvk, kkkvk, kkvkk
from x6 import kvkkvk

def save_to_json(data, filename):

    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)


def match_pattern(verb, pattern):
    
    if len(verb) != len(pattern):
        return False
    if 'o' in verb:
        return False

    w_pattern = tuple(c in 'aeiu' for c in verb)
    p_pattern = tuple(c == 'v' for c in pattern)

    return w_pattern == p_pattern



verbs = ['ndemm', 'nhezz', 'nxerm']

def sefta(verb):
    
    
    try:
        lenverb = len(verb)
        
        if 'ʷ' in verb:
            raise ValueError(f"{verb}: imyagen idi yella 'ʷ' ffɣen zi leḥsab lextu")
        
        elif lenverb == 2:
            
            raise ValueError(f"{verb} : wa ad iraḥ s ufus.")
        
        elif lenverb == 3:
        
            if match_pattern(verb, 'vkk'):
                conj = vkk(verb)
            elif match_pattern(verb, 'kkv'):
                conj = kkv(verb)
            elif match_pattern(verb, 'kvk'):
                conj = kvk(verb)
            elif match_pattern(verb, 'vkv'):
                conj = vkv(verb)
            else:
                raise ValueError(f"ca wer yelli d wenni i '{verb}'")
        
        elif lenverb == 4:
        
            if match_pattern(verb, 'kkvk'):
                conj = kkvk(verb)
            elif match_pattern(verb, 'kvkk'):
                conj = kvkk(verb)
            elif match_pattern(verb, 'kvkv'):
                conj = kvkv(verb)
            elif match_pattern(verb, 'vkvk'):
                conj = vkvk(verb)
            elif match_pattern(verb, 'vkkv'):
                conj = vkkv(verb)
            else:
                raise ValueError(f"ca wer yelli d wenni i '{verb}'")
        
        elif lenverb == 5:
        
            if match_pattern(verb, 'kvkvk'):
                conj = kvkvk(verb)
            elif match_pattern(verb, 'kkkvk'):
                conj = kkkvk(verb)
            elif match_pattern(verb, 'kkvkk'):
                conj = kkvkk(verb)
            else:
                raise ValueError(f"ca wer yelli d wenni i '{verb}'")
        
        elif lenverb == 6:
            
            if match_pattern(verb,'kvkkvk'):
                conj = kvkkvk(verb)
            else:
                raise ValueError(f"ca wer yelli d wenni i '{verb}'")
        
        elif lenverb == 7:
            
            raise ValueError(f"{verb} : ɛad wer dag-sen nexdim")
        
        elif lenverb == 8:
        
            raise ValueError(f"{verb} : ɛad wer dag-sen nexdim")
        
        elif lenverb == 9:
        
            raise ValueError(f"{verb} : ɛad wer dag-sen nexdim")
        
        else:
                
                raise ValueError(f"'{verb}' wer ɣers bu wemkan")

                
        asefti[verb] = conj
    except ValueError as e:
        print(e)



if __name__ == "__main__":
    asefti = {}
    
    if len(sys.argv) > 1:
        for verb in sys.argv[1:]:
            conj = sefta(verb)
            if conj:
                asefti[verb] = conj
        print(json.dumps(asefti, ensure_ascii=False, indent=4))
    
    else:
        for verb in verbs:
            conj = sefta(verb)
            if conj:
                asefti[verb] = conj
            save_to_json(asefti, 'asefti.json')
