class Trie:
	root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False 
    cont = 0



def InsertD(T,element):
  if T.root==None:
     Raiz = TrieNode()
     T.root = Raiz
  Children = T.root
  n = len(element)
  k = 0
  while n!=k:
    if Children.children==None:
      Lista = {}
      Children.children = Lista
      NewTrieNode = TrieNode()
      NewTrieNode.key = element[k]
      Lista[element[k]] = NewTrieNode
      Padre = Children
      Children = NewTrieNode
      Children.parent = Padre
    else:
      if element[k] in Children.children.keys():
         Children = Children.children[element[k]]
      else:
        NewTrieNode = TrieNode()
        NewTrieNode.key = element[k]
        Children.children[element[k]] = NewTrieNode
        Padre = Children
        Children = NewTrieNode
        Children.parent = Padre
    k = k + 1
  Children.isEndOfWord = True
  Children.cont += 1

def PalabrasArbolD(T):
  if T.root==None or T.root.children==None:
    return None
  else:
    Children = T.root
    ListaP = []
    PalabrasArbolRD(Children,"",ListaP)
    return ListaP

def PalabrasArbolRD(Children,palabra,ListaP):
  
  palabravieja = palabra
  for x,y in Children.children.items():
    palabra = palabra + x
    if y.isEndOfWord==True:
        ListaP.append(palabra)
    if y.children!=None:
      PalabrasArbolRD(y,palabra,ListaP)
    palabra = palabravieja

print("estoy en tried")
T = Trie()
InsertD(T,"facundo")
InsertD(T,"facundo")
InsertD(T,"aristoteles")
print(PalabrasArbolD(T))
