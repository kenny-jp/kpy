_casear_alphab = [chr(i) for i in range(32, 127)] + [chr(i) for i in range(192,254)]

def encrypt(text, shift):
    result = ""
    for ch in text:
        if ch in _casear_alphab:
            i = _casear_alphab.index(ch) + shift
            while i >= len(_casear_alphab):
                i -= len(_casear_alphab)
            result += _casear_alphab[i]
        else:
            result += ch
    return result


def decrypt(text, shift):
    result = ""
    for ch in text:
        if ch in _casear_alphab:
            i = _casear_alphab.index(ch) - shift
            while i < 0:
                i += len(_casear_alphab)
            result += _casear_alphab[i]
        else:
            result += ch
    return result
