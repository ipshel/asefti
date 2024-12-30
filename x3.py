def vkk(verb):

    if len(verb) != 3:
        raise ValueError(f"ca wer yelli d wenni, '{verb}'")
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
        f"ye{k1}{k2}{v1}n / wer ye{k1}{k2}in", f"i{k1}e{k2}{k2}{sp}{v1}n / wer i{k1}e{k2}{k2}{sp}{v1}n"
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


#kvk

def kvk(verb):

    if len(verb) != 3:
        raise ValueError(f"ca wer yelli d wenni, '{verb}'")

    k1, v1, k2 = verb
    sp = '' if v1 == 'e' else v1
    anad = [
        verb, f"{k1}{sp}{k2}em", f"{k1}{sp}{k2}et", f"{k1}{sp}{k2}emt"
    ]
    
    anad_ussid = [ # dag-s aṭṭas n uxarwed d ubeddel
    ]

    if v1 == 'i':
        sp, sp2, sp3 = v1, 'e', ''
    else:
        sp, sp2, sp3 = '', 'i', 'a'
    usmid = [
        f"{k1}{sp}{k2}{sp2}ɣ", f"te{k1}{sp}{k2}{sp2}d", f"ye{k1}{sp}{k2}{sp3}", f"te{k1}{sp}{k2}{sp3}", 
        f"ne{k1}{sp}{k2}{sp3}", f"te{verb}m", f"te{verb}mt", f"{verb}n", f"{verb}nt"
    ]
    
    usmid_anabaw = [
         f"wer {form[:-1] + 'i'}" if form[-1]=='a' else f"wer {form}" for form in usmid 
           ]
    
    
    k1, v1, k2 = verb.replace('ɣ', 'q', 1)

    arusmid = [
        f"tt{verb}iɣ", f"tett{verb}id", f"itt{verb}a", f"tett{verb}",
        f"nett{verb}a", f"tett{verb}am", f"ttt{verb}amt", f"tt{verb}an", f"tt{verb}ant"
    ] if v1 != 'e' else [
    
        f"{k1}{k1}a{k2}eɣ", f"te{k1}{k1}a{k2}ed", f"ye{k1}{k1}a{k2}", f"te{k1}{k1}a{k2}",
        f"ne{k1}{k1}a{k2}", f"te{k1}{k1}a{k2}em", f"te{k1}{k1}a{k2}emt", f"{k1}{k1}a{k2}en", f"{k1}{k1}a{k2}ent"
    ]
    
    ### ixess-as lxedmet ɛad da, ixess-as wefran
       
         
    k1, v1, k2 = verb
    arusmid_anabaw = [
        f"wer {form}" for form in arusmid
    ] 
    
    urmir = [
        f"ad {verb}eɣ", f"ad t{verb}ed", f"ad i{verb}", f"ad t{verb}", f"a n{verb}",
        f"ad t{verb}em", f"ad t{verb}mt", f"ad {verb}en", f"ad {verb}ent"
    ] if v1 != 'e' else [
        f"ad {k1}{k2}eɣ", f"ad te{k1}{k2}ed", f"ad i{verb}", f"ad t{verb}", f"a n{verb}",
        f"ad te{k1}{k2}em", f"ad te{k1}{k2}emt", f"ad {k1}{k2}en", f"ad {k1}{k2}ent"
    ]
    
    
    
    amaghun = [
        f"i{verb}en / wer ye{verb}en", f"itt{verb}en / wer yett{verb}en"
    ] if v1 != 'e' else [
        f"i{k1}{k2}in / wer ye{k1}{k2}in", f"i{k1}{k1}a{k2}en / wer ye{k1}{k1}a{k2}en"
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

#vkv

def vkv(verb):


    if len(verb) != 3:
        raise ValueError(f"ca wer yelli d wenni, '{verb}'")

    v1, k1, v2 = verb
  
    
    anad = [
        verb, f"{verb}m", f"{verb}t", f"{verb}mt"
    ]


    anad_ussid = [
        f"tt{verb}", f"tt{verb}m", f"tt{verb}t", f"tt{verb}mt"
    ]
    
    sp = 'a' if v2 == 'i' else v2
    sp1 = 'u' if v1 == 'a' else v1
    sp1 = k1 if v1 == 'i' else sp1
    sp2 = 'i' if v2 =='a' else v2
    e = 'e' if v1 == 'i' else ''
   
    usmid = [
        f"{sp1}{k1}{sp2}ɣ", f"t{e}{sp1}{k1}{sp2}d", f"y{e}{sp1}{k1}{sp}", f"t{e}{sp1}{k1}{sp}",
        f"n{e}{sp1}{k1}{sp}", f"t{e}{sp1}{k1}{sp}m", f"t{e}{sp1}{k1}{sp}mt", f"{sp1}{k1}{sp}n", f"{sp1}{k1}{sp}nt"
    ]
    
    sp = 'i' if sp == 'a' else sp
    
    usmid_anabaw = [
        f"wer {sp1}{k1}{sp2}ɣ", f"wer t{e}{sp1}{k1}{sp2}d", f"wer y{e}{sp1}{k1}{sp}", f"wer t{e}{sp1}{k1}{sp}",
        f"wer n{e}{sp1}{k1}{sp}", f"wer t{e}{sp1}{k1}{sp}m", f"wer t{e}{sp1}{k1}{sp}mt", f"wer {sp1}{k1}{sp}n", f"wer {sp1}{k1}{sp}nt"
    ]
    
    
    arusmid = [
        f"tt{verb}ɣ", f"tett{verb}d", f"it{verb}", f"tett{verb}",
        f"nett{verb}", f"tett{verb}m", f"tett{verb}mt", f"tt{verb}n", f"tt{verb}nt"
    ]
   
    

    arusmid_anabaw = [
     
        f"wer {form}" for form in arusmid
           
    ]
    

    urmir = [
        f"ad {verb}ɣ", f"ad t{verb}d", f"ad y{verb}", f"ad t{verb}", f"a n{verb}",
        f"ad t{verb}m", f"ad t{verb}mt", f"ad {verb}n", f"ad {verb}nt"
    ]
    


    amaghun = [
        f"ye{k1}{k1}an / wer ye{k1}{k1}in", f"itti{k1}in / wer yetti{k1}in"
        ] if v1 == v2 else [
        f"yu{k1}an / wer yu{k1}in" , "" # izessas tarezzut iwmaɣun arusmid
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


    

