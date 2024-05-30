
cambios = {'-': '', '¡': '', '!': '', '¿': '', '?': '', 'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
prefixs = {'re', 'sobre', 'sub', 'tras', 'trans', 'ante', 'ex', 'post', 'inter', 'des', 'vice', 'semi'}
suffixs = {"ete","eta", "aje", 'ismo','s','dor', 'al', 'logía', 'imiento', 'ona','oso', 'osa', 'torio', 'toria', 'ita', 'ito','ante', 'ente', 'ar','azo','aza'}


def clean_prefix(w): #Limpia el prefijo de la palabra
    for sym in prefixs:
        if len(w) - len(sym) > 2:
            w = w.removeprefix(sym)
    return w

def clean_suffix(w): #Limpia el sufijo de la palabra
    for sym in suffixs:
        if len(w) - len(sym) > 2:
            w = w.removesuffix(sym)
    return w

def clean_gender(w): #Elimina generos de la palabra
    if len(w)<= 3:
        return w
    if w[-1] == "o":
        w = w.removesuffix("o")
    elif w[-1] == "a":
        w = w.removesuffix("a")
    return w

def clean(word): #Realiza la limpieza profunda
    for sym, rpl in cambios.items():
        word = word.replace(sym, rpl)
        word = clean_prefix(word)
        word = clean_suffix(word)
        word = clean_gender(word)
        try:
            if int(word) not in range(1000, 3001):
                return None
        except:
            pass
    return word

