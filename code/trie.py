class Trie:
	root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False 
    cont = 0

def findKey(L,c):

    for i in range(len(L)):
        if L[i].key==c:
            return L[i]
    return None

def insertR(node,cad):
    k=cad[0]
    cadAux=cad[1:]
    t=TrieNode()
    t.parent=node
    t.key=k
    if node.children is None:
        node.children=[t]
    else:
        node.children.append(t)

    if len(cad)==1:
        t.isEndOfWord=True
        t.cont += 1
        return
    
    insertR(t,cadAux)  

def insert(T,cad):
    n=0
    if T.root==None:
        T.root=TrieNode()
        insertR(T.root,cad)
        return T
    
    node=findKey(T.root.children,cad[n])

    if node is not None:
        n=n+1
        node=node.children

        while findKey(node,cad[n]) is not None:
            node=findKey(node,cad[n])
            if n+1==len(cad):
                node.isEndOfWord=True
                node.cont +=1
                return T
            
            n=n+1
            if node.children is None:
                insertR(node,cad[n:])
                return T
            else:
                node=node.children

        insertR(node[0].parent,cad[n:])
        return T
    else:
        t=TrieNode()
        t.key=cad[0]
        t.parent=T.root
        T.root.children.append(t)
        insertR(t,cad[1:])
        return T
    
def leeTrie(lista, cad, endWord, cont):
    if endWord is True:
        print(cad, "+= ", cont)
    if lista is None:
        return  
    
    for i in range(len(lista)):    
        leeTrie(lista[i].children, cad+lista[i].key,  lista[i].isEndOfWord, lista[i].cont)


t=Trie()

import random

# Palabras aleatorias
palabras_aleatorias = [
    "Elefante", "Avión", "Caramelo", "Montaña", "Radio", "Sombrero", "Guitarra", 
    "Espejo", "Manzana", "Mariposa", "Reloj", "Globo", "Camino", "Castillo", 
    "Silla", "Camisa", "Papel", "Pelota", "Chocolate", "Árbol", "Lámpara", 
    "Ventana", "Perro", "Gato", "Nube", "Flor", "Pájaro", "Tren", "Computadora", 
    "Llave", "Piano", "Tigre", "Luna", "Caracol", "Teléfono", "Helado", "Moneda", 
    "Maleta", "Bufanda", "León", "Zapato", "Carta", "Bastón", "Bandera", "Oso", 
    "Paraguas", "Bolsa", "Martillo", "Dinosaurio", "Abanico"
]

# Generar una lista de 90,000 palabras combinando aleatorias y repetidas
palabras_repetidas = palabras_aleatorias * 2000
palabras_finales = palabras_repetidas + random.choices(palabras_aleatorias, k=88000)

# Mezclar la lista para asegurar aleatoriedad
random.shuffle(palabras_finales)

print(len(palabras_finales))  # Verificar que la lista tenga 90,000 palabras


for p in palabras_finales:
    insert(t,p)
leeTrie(t.root.children,"",False,0)