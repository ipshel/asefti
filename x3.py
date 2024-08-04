def vkk(verb):
    # ma ɣarneɣ nican vkk
    if len(verb) != 3 or not verb[0] in 'aei' or verb[1] in 'aeiu' or verb[2] in 'aeiu':
        raise ValueError(f"'{verb}' wer yelli ca d vkk, yenni ibeddan s u wer llin ca da")

    # asufeɣ n isekkilen
    k1 = verb[1]
    k2 = verb[2]

    # asefti
    
    anad = [
        verb, f"{k1}{k2}em", f"{verb}et", f"{k1}{k2}emt"
    ]

    #ca n yemyagen am enw d ers wer ssineɣ ma ad yeɛdu anad ussid nsen
    anad_ussid = [
        f"tt{verb}", f"tt{verb}em", f"tt{verb}et", f"tt{verb}emt"
    ]
    
    
    usmid = [
        f"{k1}{k2}iɣ", f"t{verb}id", f"y{verb}a", f"t{verb}a",
        f"n{verb}a", f"t{verb}im", f"t{verb}imt", f"{k1}{k2}in", f"{k1}{k2}int"
    ]
    
    usmid_anabaw = [
        f"wer {form}" for form in usmid[:2] ] +  [f"wer y{verb}i", f"wer t{verb}i", f"wer n{verb}i"] +  [f"wer {form}" for form in usmid[5:] 
    ]
    
    # di 'ecc' din exception ad yeffeɣ d ttecceɣ, uca at neɛdel s ufus
    arusmid = [
        f"tt{verb}eɣ", f"tett{verb}ed", f"itt{verb}", f"tett{verb}",
        f"nett{verb}", f"tett{verb}em", f"tett{verb}emt", f"tt{verb}en", f"tt{verb}ent"
    ]
    
    

    arusmid_anabaw = [f"wer {form}" for form in arusmid]
    
    urmir = [
        f"ad {k1}{k2}eɣ", f"ad t{verb}ed", f"ad y{verb}", f"ad t{verb}", f"a n{verb}",
        f"ad t{verb}em", f"ad t{verb}emt", f"ad {k1}{k2}en", f"ad {k1}{k2}ent"
    ]
    
    amaghun = [
        f"y{verb}in / wer y{verb}in", f"itt{verb}en / wer itt{verb}en"
    ]

    # smun
    asefti = {
            "root": "",
            "translations": {},
            "conj": {
                "anad": anad,
                "anadussid":anad_ussid,
                "usmid":usmid,
                "usmidanabaw":usmid_anabaw,
                "arusmid":arusmid,
                "arusmidanabaw": arusmid_anabaw,
                "urmir":urmir,
                "amaghun":amaghun
            }
        }

    return asefti


#kkv

def kkv(verb):

    if len(verb) != 3:
        raise ValueError(f"ca wer yelli d wenni, '{verb}'")

    k1, k2, v1 = verb
    sp = ''
    
    anad = [
        verb, f"{verb}m", f"{verb}t", f"{verb}mt"
    ]

    if k2 == 'w':
        k2, sp = 'k', 'ʷ'
    
    anad_ussid = [
        f"{k1}e{k2}{k2}{sp}{v1}", f"{k1}e{k2}{k2}{sp}{v1}m", f"{k1}e{k2}{k2}{sp}{v1}t", f"{k1}e{k2}{k2}{sp}{v1}mt"
    ]
    
    k2 = verb[1]
    
    v1 = 'i' if v1 == 'a' else v1
    
    usmid = [
        f"{k1}{k2}{v1}ɣ", f"te{k1}{k2}{v1}d", f"ye{verb}", f"te{verb}",
        f"ne{verb}", f"te{verb}m", f"te{verb}mt", f"{verb}n", f"{verb}nt"
    ]
    
    usmid_anabaw = [
         f"wer {k1}{k2}{v1}ɣ", f"wer te{k1}{k2}{v1}d", f"wer ye{k1}{k2}{v1}", f"wer te{k1}{k2}{v1}",
         f"wer ne{k1}{k2}{v1}", f"wer te{k1}{k2}{v1}m", f"wer te{k1}{k2}{v1}mt", f"wer {k1}{k2}{v1}n", f"wer {k1}{k2}{v1}nt"
    ]
    
    v1 = verb[2]
    
    if k2 == 'w':
        k2, sp = 'k', 'ʷ'
    sp2 = 'i' if v1 == 'a' else v1
    
    arusmid = [
        f"{k1}e{k2}{k2}{sp}{sp2}ɣ", f"t{k1}e{k2}{k2}{sp}{sp2}d", f"i{k1}e{k2}{k2}{sp}{v1}", f"t{k1}e{k2}{k2}{sp}{v1}",
        f"n{k1}e{k2}{k2}{sp}{v1}", f"t{k1}e{k2}{k2}{sp}{v1}m", f"t{k1}e{k2}{k2}{sp}{v1}mt", f"{k1}e{k2}{k2}{sp}{v1}n", f"{k1}e{k2}{k2}{sp}{v1}nt"
    ]
   
    
    v1 = 'i' if v1 == 'a' else v1
    arusmid_anabaw = [
        f"wer {k1}e{k2}{k2}{sp}{sp2}ɣ", f"wer t{k1}e{k2}{k2}{sp}{sp2}d", f"wer i{k1}e{k2}{k2}{sp}{v1}", f"wer t{k1}e{k2}{k2}{sp}{v1}",
        f"wer n{k1}e{k2}{k2}{sp}{v1}", f"wer t{k1}e{k2}{k2}{sp}{v1}m", f"wer t{k1}e{k2}{k2}{sp}{v1}mt", f"wer {k1}e{k2}{k2}{sp}{v1}n", f"wer {k1}e{k2}{k2}{sp}{v1}nt"
    ]
    
    k2, v1 = verb[1], verb[2]
    urmir = [
        f"ad {k1}{k2}{sp2}ɣ", f"ad te{k1}{k2}{sp2}d", f"ad ye{k1}{k2}{v1}", f"ad te{k1}{k2}{v1}", f"a ne{k1}{k2}{v1}",
        f"ad te{k1}{k2}{v1}m", f"ad te{k1}{k2}{v1}mt", f"ad {k1}{k2}{v1}n", f"ad {k1}{k2}{v1}nt"
    ]
    
    if k2 == 'w':
        k2, sp = 'k', 'ʷ'
    
    amaghun = [
        f"ye{k1}{k2}{v1}n / wer ye{k1}{k2}in", f"i{k1}e{k2}{k2}{sp}{v1}n / wer i{k1}e{k2}{k2}{sp}n"
    ]

    # smun
    asefti = {
            "root": "",
            "translations": {},
            "conj": {
                "anad": anad,
                "anadussid":anad_ussid,
                "usmid":usmid,
                "usmidanabaw":usmid_anabaw,
                "arusmid":arusmid,
                "arusmidanabaw": arusmid_anabaw,
                "urmir":urmir,
                "amaghun":amaghun
            }
        }

    return asefti



