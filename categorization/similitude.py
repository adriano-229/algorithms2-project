import math


def dot_product(v1, v2):
    result = 0
    for word in v1.keys():
        try:
            result += v1[word] * v2[word]
        except:
            pass #Se pasa ya que la multiplicacion daria 0
    return result


def modulus(v):
    mod = 0
    for c in v.keys():
        mod += v[c] ** 2
    return math.sqrt(mod)

"""
def cosine_similarity(v1, v2):
    denominator = modulus(v1) * modulus(v2)
    if denominator == 0:
        print("Warning: division by zero, returning zero")
        return 0
    return round(dot_product(v1, v2) / denominator, 4)
"""
def cosine_similarity(mainDoc, secondaryDoc):
    denominator = modulus(mainDoc) * modulus(secondaryDoc)
    if denominator == 0:
        return 0
    return dot_product(mainDoc, secondaryDoc) / denominator



