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
        f"i{k1}e{k2}{k3}en / wer i{k1}e{k2}{k3}en",
        f"i{k1}e{k2}{k2}{k3}en / wer i{k1}e{k2}{k2}{k3}en"
    ] if k1 != k2 else [
        f"ye{k1}{k2}{k3}en / wer ye{k1}{k2}{k3}en",
        f"itte{k1}{k2}{k3}en / wer itte{k1}{k2}{k3}en"
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


#kvkk

def kvkk(verb):
   
   
    if len(verb) != 4:
        raise ValueError(f"'{verb}'. ca wer yelli d wenni")


    # asefti
    
    anad = [
        verb, f"{verb}em", f"{verb}et", f"{verb}emt"
    ]

    anad_ussid = [
         
         f"tt{verb}a", f"tt{verb}am", f"tt{verb}at", f"tt{verb}amt"
    ]
    
    
    usmid = [
        f"{verb}eɣ", f"t{verb}ed", f"i{verb}", f"t{verb}",
        f"n{verb}", f"t{verb}em", f"t{verb}emt", f"{verb}en", f"{verb}ent"
    ]
    
    
    usmid_anabaw = [
        f"wer {form}" for form in usmid
    ]
    

    arusmid = [
        f"tt{verb}iɣ", f"tett{verb}id", f"itt{verb}a", f"tett{verb}a",
        f"net{verb}a", f"tett{verb}am", f"tett{verb}mt", f"tt{verb}an", f"tett{verb}ant"
    ]
    

    arusmid_anabaw = [
        f"wer {form}" for form in arusmid[:2] ] +  [f"wer itt{verb}i", f"wer tett{verb}i", f"wer net{verb}i"] +  [f"wer {form}" for form in arusmid[5:]
        ]
    
    urmir = [
        f"ad {form}" for form in usmid
    ]    
    
    amaghun = [
        f"i{verb}en / wer i{verb}en",
        f"itt{verb}an / wer itt{verb}an"
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

#kvkv

def kvkv(verb):
   
   
    if len(verb) != 4:
        raise ValueError(f"'{verb}'. ca wer yelli d wenni")

    # asufeɣ n isekkilen
    k1, v1, k2, v2 = verb
    
    
    # asefti
    
    anad = [
        verb, f"{verb}m", f"{verb}t", f"{verb}mt"
    ]

    anad_ussid = [
         
         f"tt{verb}", f"tt{verb}m", f"tt{verb}t", f"tt{verb}mt"
    ]
    
    sp2 = 'i' if v2 == 'a' else v2
    usmid = [
        f"{k1}{v1}{k2}{sp2}ɣ", f"t{k1}{v1}{k2}{sp2}d", f"i{verb}", f"t{verb}",
        f"n{verb}", f"t{verb}m", f"t{verb}mt", f"{verb}n", f"{verb}nt"
    ]
    
    sp = 'i' if v1 == 'a' else v1

    usmid_anabaw = [
        f"wer {k1}{sp}{k2}{sp2}ɣ", f"wer t{k1}{sp}{k2}{sp2}d", f"wer i{k1}{sp}{k2}{sp2}", f"wer t{k1}{sp}{k2}{sp2}",
        f"wer n{k1}{sp}{k2}{sp2}", f"wer t{k1}{sp}{k2}{sp2}m", f"wer t{k1}{sp}{k2}{sp2}mt", f"wer {k1}{sp}{k2}{sp2}n", f"wer {k1}{sp}{k2}{sp2}nt"
    ]
    

    arusmid = [
        f"tt{k1}{v1}{k2}{sp2}ɣ", f"tett{k1}{v1}{k2}{sp2}d", f"itt{k1}{v1}{k2}{v2}", f"tett{k1}{v1}{k2}{v2}",
        f"net{k1}{v1}{k2}{v2}", f"tett{k1}{v1}{k2}{v2}m", f"tett{k1}{v1}{k2}{v2}mt", f"tt{k1}{v1}{k2}{v2}n", f"tett{k1}{v1}{k2}{v2}nt"
    ]
    

    arusmid_anabaw = [
        f"wer {form}" for form in arusmid[:2] ] +  [f"wer itt{k1}{v1}{k2}i", f"wer tett{k1}{v1}{k2}i", f"wer net{k1}{v1}{k2}i"] +  [f"wer {form}" for form in arusmid[5:]
        ]
    
    urmir = [
        f"ad {form}" for form in usmid
    ]    

    amaghun = [
        f"i{verb}n / wer i{k1}{sp}{k2}{sp2}n",
        f"itt{verb}n / wer itt{k1}{sp}{k2}{sp2}n"
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

#vkvk

def vkvk(verb):

   
    if len(verb) != 4:
        raise ValueError(f"'{verb}'. ca wer yelli d wenni")

    # asufeɣ n isekkilen
    v1, k1, v2, k2 = verb
    # asefti
    
    sp = '' if v2 == 'e' else v2
    anad = [
        verb, f"{v1}{k1}{sp}{k2}em", f"{v1}{k1}{sp}{k2}et", f"{v1}{k1}{sp}{k2}emt"
    ]

    anad_ussid = [
        f"tt{verb}", f"tt{v1}{k1}{sp}{k2}em", f"tt{v1}{k1}{sp}{k2}et", f"tt{v1}{k1}{sp}{k2}emt"
    ]
    
    psp = 'u' if v1 == 'a' else v1
    usmid = [
        f"{psp}{k1}{sp}{k2}eɣ", f"t{psp}{k1}{sp}{k2}ed", f"y{psp}{k1}{v2}{k2}", f"t{psp}{k1}{v2}{k2}",
        f"n{psp}{k1}{v2}{k2}", f"t{psp}{k1}{sp}{k2}em", f"t{psp}{k1}{sp}{k2}emt", f"{psp}{k1}{sp}{k2}en", f"{psp}{k1}{sp}{k2}ent"
    ] # danita ɣar-neɣ scwa di 3rd.sg d 1st.pl mala texsed ad teksed beddel v2 s sp waha
    
    sp = 'i' if v2 == 'e' else v2
    usmid_anabaw = [
        f"wer {psp}{k1}{sp}{k2}eɣ", f"wer t{psp}{k1}{sp}{k2}ed", f"wer y{psp}{k1}{sp}{k2}", f"wer t{psp}{k1}{sp}{k2}",
        f"wer n{psp}{k1}{sp}{k2}", f"wer t{psp}{k1}{sp}{k2}em", f"wer t{psp}{k1}{sp}{k2}emt", f"wer {psp}{k1}{sp}{k2}en", f"wer {psp}{k1}{sp}{k2}ent"
    ]
    
    sp = '' if v2 == 'e' else v2
    arusmid = [
        f"tt{v1}{k1}{sp}{k2}eɣ", f"tett{v1}{k1}{sp}{k2}ed", f"itt{v1}{k1}{v2}{k2}", f"tett{v1}{k1}{v2}{k2}",
        f"nett{v1}{k1}{v2}{k2}", f"tett{v1}{k1}{sp}{k2}em", f"tett{v1}{k1}{sp}{k2}emt", f"tt{v1}{k1}{sp}{k2}en", f"tt{v1}{k1}{sp}{k2}ent"
    ]
    
    psp = 'i' if v1 == 'a' else v1
    arusmid_anabaw = [
        f"wer tt{psp}{k1}{sp}{k2}eɣ", f"wer tett{psp}{k1}{sp}{k2}ed", f"wer itt{psp}{k1}{v2}{k2}", f"wer tett{psp}{k1}{v2}{k2}",
        f"wer nett{psp}{k1}{v2}{k2}", f"wer tett{psp}{k1}{sp}{k2}em", f"wer tett{psp}{k1}{sp}{k2}emt", f"wer tt{psp}{k1}{sp}{k2}en", f"wer tt{psp}{k1}{sp}{k2}ent"
]
    
    sp = '' if v2 == 'e' else v2
    urmir = [
        f"ad {v1}{k1}{sp}{k2}eɣ", f"ad t{v1}{k1}{sp}{k2}ed", f"ad y{v1}{k1}{v2}{k2}", f"ad t{v1}{k1}{v2}{k2}", f"a n{v1}{k1}{v2}{k2}",
        f"ad t{v1}{k1}{sp}{k2}em", f"ad t{v1}{k1}{sp}{k2}emt", f"ad {v1}{k1}{sp}{k2}en", f"ad {v1}{k1}{sp}{k2}ent"
    ]
    

    ssp = 'u' if v1 == 'a' else v1
    psp = 'i' if v1 == 'a' else v2
    amaghun = [
        f"y{ssp}{k1}{sp}{k2}en / wer y{ssp}{k1}{psp}{k2}en",
        f"itt{v1}{k1}{sp}{k2}en / wer itt{psp}{k1}{sp}{k2}en"
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


def vkkv(verb):
   
   
    if len(verb) != 4:
        raise ValueError(f"'{verb}'. ca wer yelli d wenni")

    # asufeɣ n isekkilen
    v1,k1,k2,v2 = verb
    
    k3 = ''

    # asefti
    
    anad = [
        verb, f"{verb}m", f"{verb}t", f"{verb}mt"
    ]

    anad_ussid = [
        f"tt{verb}", f"tt{verb}m", f"tt{verb}t", f"{verb}mt"
    ]
    
    sp = 'i' if v2 == 'a' else v2
    usmid = [
        f"{v1}{k1}{k2}{sp}ɣ", f"t{v1}{k1}{k2}{sp}d", f"y{v1}{k1}{k2}{v2}", f"t{v1}{k1}{k2}{v2}",
        f"n{v1}{k1}{k2}{v2}", f"t{v1}{k1}{k2}{v2}m", f"t{v1}{k1}{k2}{v2}mt", f"{v1}{k1}{k2}{v2}n", f"{v1}{k1}{k2}{v2}nt"
    ]
    
    usmid_anabaw = [
        f"wer {form}" for form in usmid
    ]
    

    arusmid = [
        f"tt{v1}{k1}{k2}{sp}ɣ", f"tt{v1}{k1}{k2}{sp}d", f"itt{v1}{k1}{k2}{v2}", f"tett{v1}{k1}{k2}{v2}",
        f"nett{v1}{k1}{k2}{v2}", f"tett{v1}{k1}{k2}{v2}m", f"tett{v1}{k1}{k2}{v2}mt", f"tt{v1}{k1}{k2}{v2}n", f"tt{v1}{k1}{k2}{v2}nt"
    ]
    

    arusmid_anabaw = [
        f"wer {form}" for form in arusmid
    ]
    
    urmir = [
       f"ad {form}" for form in usmid
    ]  
    
    amaghun = [
        f"y{verb}n / wer y{v1}{k1}{k2}{sp}n",
        f"itt{verb}n / wer itt{v1}{k1}{k2}{sp}n"
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

