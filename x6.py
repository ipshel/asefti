def kvkkvk(verb):
    if len(verb) != 6 or verb[0] in 'aeiu' or not verb[1] in 'aeiu' or verb[2] in 'aeiu' or verb[3] in 'aeiu' or not verb[4] in 'aeiu' or verb[5] in 'aeiu':
        raise ValueError(f"'{verb}' wer yelli ca d kvkkvk")

    k1, v1, k2, k3, v2, k4 = verb
    
    sp = 'a' if v2 == 'a' else ''
    # {k1}{k1}{k2}{k3}{v2}{k4}
    anad = [
        verb, f"{k1}{v1}{k2}{k3}{sp}{k4}em", f"{k1}{v1}{k2}{k3}{sp}{k4}et", f"{k1}{v1}{k2}{k3}{sp}{k4}emt"
    ]

    anad_ussid = [
        f"tt{verb}", f"tt{verb}em", f"tt{verb}t", f"tt{verb}emt"
    ]

    usmid = [
        f"{k1}{v1}{k2}{k3}{sp}{k4}eɣ", f"t{k1}{v1}{k2}{k3}{sp}{k4}ed", f"i{verb}", f"t{verb}",
        f"n{verb}", f"t{k1}{v1}{k2}{k3}{sp}{k4}em", f"t{k1}{v1}{k2}{k3}{sp}{k4}emt", f"{k1}{v1}{k2}{k3}{sp}{k4}en", f"{k1}{v1}{k2}{k3}{sp}{k4}ent"
    ]

    usmid_anabaw = [
        f"wer {form}" for form in usmid
    ]

    arusmid = [
        f"tt{k1}{v1}{k2}{k3}{sp}{k4}eɣ", f"tett{k1}{v1}{k2}{k3}{sp}{k4}ed", f"itt{verb}", f"tett{verb}",
        f"nett{verb}", f"tett{k1}{v1}{k2}{k3}{v2}{k4}em", f"tett{k1}{v1}{k2}{k3}{sp}{k4}emt", f"tt{k1}{v1}{k2}{k3}{sp}{k4}en", f"tt{k1}{v1}{k2}{k3}{sp}{k4}ent"
    ]

    arusmid_anabaw = [
        f"wer {form}" for form in arusmid
    ]

    urmir = [
        f"ad {k1}{v1}{k2}{k3}{sp}{k4}eɣ", f"ad t{k1}{v1}{k2}{k3}{sp}{k4}ed", f"ad i{verb}", f"ad t{verb}", f"a n{verb}",
        f"ad t{k1}{v1}{k2}{k3}{sp}{k4}em", f"ad t{k1}{v1}{k2}{k3}{sp}{k4}emt", f"ad {k1}{v1}{k2}{k3}{sp}{k4}en", f"ad {k1}{v1}{k2}{k3}{sp}{k4}ent"
    ]

    amaghun = [
        f"i{k1}{v1}{k2}{k3}{sp}{k4}en / wer i{k1}{v1}{k2}{k3}{sp}{k4}en", f"yett{k1}{v1}{k2}{k3}a{k4}en / wer yett{k1}{v1}{k2}{k3}a{k4}en"
    ]


    asefti = {
        "root": "",
        "translations": {},
        "conj": {
            "anad": anad,
            "anadussid": anad_ussid,
            "usmid": usmid,
            "usmidanabaw": usmid_anabaw,
            "arusmid": arusmid,
            "arusmidanabaw": arusmid_anabaw,
            "urmir": urmir,
            "amaghun": amaghun
        }
    }

    return asefti
