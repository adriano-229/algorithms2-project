import math


def dot_product(v1, v2):
    dot = 0
    vec_size = len(v1)
    for i in range(vec_size):
        dot += v1[i] * v2[i]
    return dot


def modulus(v):
    mod = 0
    for c in v:
        mod += c ** 2
    return math.sqrt(mod)


def cosine_similarity(v1, v2):
    denominator = modulus(v1) * modulus(v2)
    if denominator == 0:
        print("Warning: division by zero, returning zero")
        return 0
    return round(dot_product(v1, v2) / denominator, 4)


if __name__ == "__main__":
    print(cosine_similarity([0, 0], [234, 0]))
    print(cosine_similarity([100, 3], [234, 3]))
