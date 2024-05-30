import math


def dot_product(v1, v2): #Calcula el producto escalar entre dos diccionarios
    result = 0
    for word in v1.keys():
        try:
            result += v1[word] * v2[word]
        except:
            pass #Se pasa ya que la multiplicacion daria 0
    return result


def modulus(v): #Realiza la operacion modulo en un diccionario
    mod = 0
    for c in v.keys():
        mod += v[c] ** 2
    return math.sqrt(mod)

def cosine_similarity(mainDoc, secondaryDoc): #Similitud del coseno entre un documento con otro
    denominator = modulus(mainDoc) * modulus(secondaryDoc)
    if denominator == 0:
        return 0
    return dot_product(mainDoc, secondaryDoc) / denominator




