def kvkvk(verb):
   
   
    if len(verb) != 5:
        raise ValueError(f"'{verb}'. ca wer yelli d wenni")

    k1, v1, k2, v2, k3 = verb
    sp = 'a' if v2 == 'a' else ''

    
    anad = [
        verb, f"{k1}{v1}{k2}{sp}{k3}em", f"{k1}{v1}{k2}{sp}{k3}et", f"{k1}{v1}{k2}{sp}{k3}emt"
    ]
    
    sp = 'a' if v2 == 'a' else v1
    anad_ussid = [
        f"tt{k1}{v1}{k2}{sp}{k3}", f"tt{k1}{v1}{k2}{sp}{k3}em", f"tt{k1}{v1}{k2}{sp}{k3}et", f"tt{k1}{v1}{k2}{sp}{k3}emt"
    ]
    
    sp = 'a' if v2 == 'a' else ''
    sp2 = 'e' if sp != 'a' else ''
    usmid = [
        f"{k1}{v1}{k2}{sp}{k3}eɣ", f"t{k1}{v1}{k2}{sp}{k3}ed", f"i{k1}{v1}{k2}{sp}{sp2}{k3}", f"t{k1}{v1}{k2}{sp}{sp2}{k3}",
        f"n{k1}{v1}{k2}{sp}{sp2}{k3}", f"t{k1}{v1}{k2}{sp}{k3}em", f"t{k1}{v1}{k2}{sp}{k3}emt", f"{k1}{v1}{k2}{sp}{k3}en", f"{k1}{v1}{k2}{sp}{k3}ent"
    ]
    
    v1 = 'i' if v1 == 'a' else v1
    usmid_anabaw = [
        f"wer {k1}{v1}{k2}{sp}{k3}eɣ", f"wer t{k1}{v1}{k2}{sp}{k3}ed", f"wer i{k1}{v1}{k2}{sp}{sp2}{k3}", f"wer t{k1}{v1}{k2}{sp}{sp2}{k3}",
        f"wer n{k1}{v1}{k2}{sp}{sp2}{k3}", f"wer t{k1}{v1}{k2}{sp}{k3}em", f"wer t{k1}{v1}{k2}{sp}{k3}emt", f"wer {k1}{v1}{k2}{sp}{k3}en", f"wer {k1}{v1}{k2}{sp}{k3}ent"
    ]
    
    v1 = verb[1]
    sp = 'a'
    arusmid = [
        f"tt{k1}{v1}{k2}{sp}{k3}eɣ", f"tett{k1}{v1}{k2}{sp}{k3}ed", f"itt{k1}{v1}{k2}{sp}{k3}", f"tett{k1}{v1}{k2}{sp}{k3}",
        f"nett{k1}{v1}{k2}{sp}{k3}", f"tett{k1}{v1}{k2}{sp}{k3}", f"tett{k1}{v1}{k2}{sp}{k3}emt", f"tt{k1}{v1}{k2}{sp}{k3}en", f"tt{k1}{v1}{k2}{sp}{k3}ent"
    ] 
    
    v1 = 'i' if v1 == 'a' else v1
    sp = 'i'
    arusmid_anabaw = [
        f"wer tt{k1}{v1}{k2}{sp}{k3}eɣ", f"wer tett{k1}{v1}{k2}{sp}{k3}ed", f"wer itt{k1}{v1}{k2}{sp}{k3}", f"wer tett{k1}{v1}{k2}{sp}{k3}",
        f"wer nett{k1}{v1}{k2}{sp}{k3}", f"wer tett{k1}{v1}{k2}{sp}{k3}", f"wer tett{k1}{v1}{k2}{sp}{k3}emt", f"wer tt{k1}{v1}{k2}{sp}{k3}en", f"wer tt{k1}{v1}{k2}{sp}{k3}ent"
]
    
    v1 = verb[1]
    sp = 'a' if v2 == 'a' else ''
    urmir = [
        f"ad {k1}{v1}{k2}{sp}{k3}eɣ", f"ad t{k1}{v1}{k2}{sp}{k3}ed", f"ad i{k1}{v1}{k2}e{k3}", f"ad t{k1}{v1}{k2}e{k3}", f"a n{k1}{v1}{k2}e{k3}",
        f"ad t{k1}{v1}{k2}{sp}{k3}em", f"ad t{k1}{v1}{k2}{sp}{k3}emt", f"ad {k1}{v1}{k2}{sp}{k3}en", f"ad {k1}{v1}{k2}{sp}{k3}ent"
    ] 
    
    vs = 'i' if v1 == 'a' else v1
    v2 = 'a' if v1 == 'a' else v2
    amaghun = [
        f"i{k1}{v1}{k2}{k3}en / wer i{k1}{vs}{k2}{k3}en", f"itt{k1}{v1}{k2}{v2}{k3}en / wer itt{k1}{vs}{k2}{vs}{k3}en"
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

