def kkvk(verb):
   
   
    if len(verb) != 4:
        raise ValueError(f"'{verb}'. ca wer yelli d wenni")

    # asufeɣ n isekkilen
    k1, k2, v1, k3 = verb

    # asefti
    
    anad = [
        verb, f"{k1}{k2}{k3}em", f"{k1}{k2}{k3}et", f"{k1}{k2}{k3}emt"
    ] if k1 == k2 else [
        verb, f"{k1}e{k2}{k3}em", f"{k1}e{k2}{k3}et", f"{k1}e{k2}{k3}emt"
    ]

    anad_ussid = [
        f"{k1}e{k2}{k2}e{k3}", f"{k1}e{k2}{k2}{k3}em", f"{k1}e{k2}{k2}{k3}et", f"{k1}e{k2}{k2}{k3}emt"
    ] if k1 != k2 else [
        f"tte{k1}{k2}e{k3}", f"tte{k1}{k2}{k3}em", f"tte{k1}{k2}{k3}et", f"tte{k1}{k2}{k3}emt"
    ]
    
    
    usmid = [
        f"{k1}e{k2}{k3}eɣ", f"t{k1}e{k2}{k3}ed", f"ye{verb}", f"te{verb}",
        f"ne{verb}", f"t{k1}e{k2}{k3}em", f"t{k1}e{k2}{k3}emt", f"{k1}e{k2}{k3}en", f"{k1}e{k2}{k3}ent"
    ] if k1 != k2 else [
        f"{k1}{k2}{k3}eɣ", f"te{k1}{k2}{k3}ed", f"ye{verb}", f"te{verb}",
        f"ne{verb}", f"te{k1}{k2}{k3}em", f"te{k1}{k2}{k3}emt", f"{k1}{k2}{k3}en", f"{k1}{k2}{k3}ent"
    ]
    
    usmid_anabaw = [
        f"wer {form}" for form in usmid[:2] ] +  [f"wer y{verb}i", f"wer t{verb}i", f"wer n{verb}i"] +  [f"wer {form}" for form in usmid[5:] 
    ]
    

    arusmid = [
        f"{k1}e{k2}{k2}{k3}eɣ", f"t{k1}e{k2}{k2}{k3}ed", f"i{k1}e{k2}{k2}e{k3}", f"t{k1}e{k2}{k2}e{k3}",
        f"n{k1}e{k2}{k2}e{k3}", f"t{k1}e{k2}{k2}{k3}em", f"t{k1}e{k2}{k2}{k3}emt", f"{k1}e{k2}{k2}{k3}en", f"{k1}e{k2}{k2}{k3}ent"
    ] if k1 != k2 else [
        f"te{k1}{k2}{k3}eɣ", f"tette{k1}{k2}{k3}ed", f"itte{k1}{k2}{k3}", f"tette{k1}{k2}{k3}",
        f"nette{k1}{k2}{k3}", f"tette{k1}{k2}{k3}em", f"tette{k1}{k2}{k3}emt", f"tte{k1}{k2}{k3}en", f"tte{k1}{k2}{k3}ent"
    ]
    

    arusmid_anabaw = [f"wer {form}" for form in arusmid]
    
    urmir = [
        f"ad {k1}e{k2}{k3}eɣ", f"ad t{k1}e{k2}{k3}ed", f"ad ye{k1}e{k2}{k3}", f"ad te{k1}e{k2}{k3}", f"a ne{k1}e{k2}{k3}",
        f"ad t{k1}e{k2}{k3}em", f"ad t{k1}e{k2}{k3}emt", f"ad {k1}e{k2}{k3}en", f"ad {k1}e{k2}{k3}ent"
    ] if k1 != k2 else [
        f"ad {k1}{k2}{k3}eɣ", f"ad te{k1}{k2}{k3}ed", f"ad ye{k1}{k2}e{k3}", f"ad te{k1}{k2}e{k3}", f"a ne{k1}{k2}e{k3}",
        f"ad te{k1}{k2}{k3}em", f"ad te{k1}{k2}{k3}emt", f"ad {k1}{k2}{k3}en", f"ad {k1}{k2}{k3}ent"
    ]    
    
    amaghun = [
        f"i{k1}e{k2}{k3}en / wer i{k1}e{k2}{k3}en", f"i{k1}e{k2}{k2}{k3}en / wer i{k1}e{k2}{k2}{k3}en"
    ] if k1 != k2 else [
        f"ye{k1}{k2}{k3}en / wer ye{k1}{k2}{k3}en", f"itte{k1}{k2}{k3}en / wer itte{k1}{k2}{k3}en"
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

