path = 'Integration/'

Nom_projet = 'Numerical Intergal'
Nom_icon = 'icone.ico'

CHANGE_FONCTION = {'sin(' : 'm.sin(',
                   'cos(' : 'm.cos(',
                   'tan(' : 'm.tan(',
                   'asin(' : 'm.asin(',
                   'acos(' : 'm.acos(',
                   'atan(' : 'm.atan(',
                   'log(' : 'm.log(',
                   'exp(' : 'm.exp(',
                   'pi' : 'm.pi'}

def is_float(txt):
    if txt.count('.') > 1:
        return False
    if txt.count('-') > 1:
        return False
    elif txt.count('-') == 1:
        if txt[0] != '-':
            return False
    if txt.replace(".", "").replace("-", "0").isdigit():
        return True
    return False

def verif_fonction(p1):
    try:
        txt = p1.func
        x = float(p1.xmin.get())
        y = eval(txt)
        x = float(p1.xmax.get())
        y = eval(txt)
        return False
    except:
        return True

def round_str(val):
    exp = 0
    if val > 1e3:
        while val <= 1:
            val *= 0.1
            exp += 1
        exp -= 1
        val *= 10
        txt_val = f'{round(val, 2)} e{exp}'
    elif val < 1e-3:
        while val >= 1:
            val *= 10
            exp -= 1
        txt_val = f'{round(val, 2)} e{exp}'
    else:
        txt_val = f'{round(val, 3)}'

    return txt_val