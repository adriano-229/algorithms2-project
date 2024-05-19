class Trie:
	root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False 
    cont = 0


def PalabrasArbol(T):
  if T.root==None or T.root.children==None:
    return None
  else:
    Children = T.root
    ListaP = []
    PalabrasArbolR(Children,"",ListaP)
    return ListaP

def PalabrasArbolR(Children,palabra,ListaP):
  
  n = len(Children.children)
  palabravieja = palabra
  i = 0
  while i!=n:
    palabra = palabra + Children.children[i].key
    if Children.children[i].isEndOfWord==True:
        ListaP.append(palabra)
    if Children.children[i].children!=None:
      PalabrasArbolR(Children.children[i],palabra,ListaP)
    palabra = palabravieja
    i = i + 1

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

def Prefix(T,prefijo):
  ListaPalabras = []
  if T.root==None:
      return ListaPalabras
  Children = T.root
  t = len(prefijo)
  if t!=0:
    i = 0
    k = 0
    palabra = ""
    while True:
        if i==len(Children.children):
            return ListaPalabras
        else:
            if Children.children[i].key==prefijo[k]:
               
                palabra = palabra + Children.children[i].key
                if Children.children[i].isEndOfWord==True:
                    if CarcularParecido(palabra,prefijo,ListaPalabras,Children)==False:
                        return ListaPalabras
                Children = Children.children[i]
                i = 0
                k = k + 1
                if k==t:
                    break
            else:
                i = i + 1
    PrefixR(ListaPalabras,Children,prefijo,prefijo)
    return ListaPalabras
    
def PrefixR(ListaPalabras,Children,palabra,prefijo):

    if Children.children==None:
       q = 1
    else:
       q = len(Children.children)
    i = 0
    vieja = palabra
    while q!=i:
      if Children.isEndOfWord==True:
        if len(palabra)-len(prefijo)<=len(palabra)//2:
            if CarcularParecido(palabra,prefijo,ListaPalabras,Children)==False:
                return ListaPalabras
            
      if Children.children!=None:
        palabra = palabra + Children.children[i].key
        PrefixR(ListaPalabras,Children.children[i],palabra,prefijo)
      i = i + 1
      palabra = vieja

def matcheador(T,word):
  Lista = Prefix(T,word)
  print(Lista)
  if len(Lista)==0:
      return False
  if len(word)>2 and len(word)<=4 and Lista[1]==100:
    Lista[2].cont += 1
    return True
  elif len(word)>4 and Lista[1]>=50:
    Lista[2].cont += 1
    return True
  else:
    return False

def CarcularParecido(palabra,prefijo,ListaPalabras,Children):
   if len(palabra)>=len(prefijo):
       multi = prefijo
       divisor = palabra
   else:
       multi = palabra
       divisor = prefijo


   if len(ListaPalabras)==0:
        ListaPalabras.append(palabra)
        ListaPalabras.append((len(multi)*100)/len(divisor))
        ListaPalabras.append(Children)
   else:
        if ListaPalabras[1]<(len(multi)*100)/len(divisor):
            ListaPalabras[0] = palabra
            ListaPalabras[1]= (len(multi)*100)/len(divisor)
            ListaPalabras[2]=(Children)
        else:
            return False   
      


T = Trie()
insert(T,"facundoe")
insert(T,"facu")
insert(T,"facundoelcapo")
print(PalabrasArbol(T))
print(matcheador(T,"facun"))

"""
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
"""




