import math


def dot_product(v1, v2):
    result = 0
    for word in v1.keys():
        try:
            result += v1[word] * v2[word]
        except:
            continue
    return result


def modulus(v):
    mod = 0
    for c in v.keys():
        mod += v[c] ** 2
    return math.sqrt(mod)


def cosine_similarity(v1, v2):
    denominator = modulus(v1) * modulus(v2)
    if denominator == 0:  # caso indeterminado resuelto arbitrariamente
        return 0
    return dot_product(v1, v2) / denominator


def compare_with_cosine_similarity(vec_set, pivot_vec):
    ans = []
    for v in vec_set:
        simil = cosine_similarity(v, pivot_vec)
        ans.append(simil)
    return ans
