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

