import pickle
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

def Insert(T,element):
  if T.root==None:
     Raiz = TrieNode()
     T.root = Raiz
  Children = T.root
  n = len(element)
  k = 0
  while n!=k:
    if Children.children==None:
      Lista = []
      Children.children = Lista
      NewTrieNode = TrieNode()
      NewTrieNode.key = element[k]
      Lista.append(NewTrieNode)
      Padre = Children
      Children = NewTrieNode
      Children.parent = Padre
    else:
      VoF = False
      i = 0
      while VoF == False:
        if i==len(Children.children):
          NewTrieNode = TrieNode()
          NewTrieNode.key = element[k]
          Children.children.append(NewTrieNode)
          Padre = Children
          Children = NewTrieNode
          Children.parent = Padre
          VoF = True
        else: 
          if Children.children[i].key == element[k]:
            Children = Children.children[i]
            VoF = True
          else:
            i = i + 1
          
    k = k + 1
  Children.isEndOfWord = True
  Children.cont += 1
    
def leeTrie(lista, cad, endWord, cont):
    if endWord is True:
        print(cad, "+= ", cont)
    if lista is None:
        return  
    
    for i in range(len(lista)):    
        leeTrie(lista[i].children, cad+lista[i].key,  lista[i].isEndOfWord, lista[i].cont)

def matcheador(T,word):
  Lista = MatchsD(T,word)
  print(Lista)
  if len(Lista)==0:
      return False
  if len(word)>2 and Lista[1]>=50:
     Lista[2].cont += 1
     return True
  else:
    return False

def CarcularParecido(match,palabra,prefijo,ListaPalabras,Children):
   
   if len(palabra)<=len(prefijo):
      div = prefijo
   else:
      div = palabra

   if len(ListaPalabras)==0:
        ListaPalabras.append(palabra)
        ListaPalabras.append((match*100)/len(div))
        ListaPalabras.append(Children)
        ListaPalabras.append(prefijo)
   else:
        if ListaPalabras[1]<(match*100)/len(div):
            ListaPalabras[0] = palabra
            ListaPalabras[1]= (match*100)/len(div)
            ListaPalabras[2]=(Children)
            ListaPalabras[3]= prefijo
        else:
            return False  
   

def Matchs(T,prefijo):
    ListaPalabras = []
    Children = T.root
    k = 0
    matchs = 0
    i = 0
    palabra = ""
    while True:
        if Children.children==None:
            return ListaPalabras
        if i==len(Children.children):
            return ListaPalabras
        else:
            if Children.children[i].key==prefijo[k]:
                matchs = matchs + 1
                k = k + 1
                palabra = palabra + Children.children[i].key
                if Children.children[i].isEndOfWord==True:
                    if CarcularParecido(matchs,palabra,prefijo,ListaPalabras,Children.children[i])==False:
                        return ListaPalabras
                if k==len(prefijo):
                    if Children.isEndOfWord==False:
                        return(MatchsR(matchs,palabra,prefijo,ListaPalabras,Children.children[i]))
                    else:
                        break
                Children = Children.children[i]
                i = 0

            elif Children.children[i].key!=prefijo[k] and matchs!=0:
                return(MatchsR(matchs,palabra,prefijo,ListaPalabras,Children))
            else:
                i = i + 1
    return ListaPalabras

def MatchsR(matchs,palabra,prefijo,ListaPalabras,Children):
    if Children.children==None:
       q = 0
       if Children.isEndOfWord==True:
            if CarcularParecido(matchs,palabra,prefijo,ListaPalabras,Children)==False:
                return ListaPalabras
    else:
       q = len(Children.children)
    i = 0
    vieja = palabra
    while q!=i:
      if Children.isEndOfWord==True:
        if CarcularParecido(matchs,palabra,prefijo,ListaPalabras,Children)==False:
            return ListaPalabras
      palabra = palabra + Children.children[i].key
      MatchsR(matchs,palabra,prefijo,ListaPalabras,Children.children[i])
      i = i + 1
      palabra = vieja

    return ListaPalabras


def MatchsD(T,prefijo):
  ListaPalabras = []
  Children = T.root
  k = 0
  matchs = 0
  i = 0
  palabra = ""
  while True:
     if Children.children==None:
            return ListaPalabras
     if i==len(Children.children):
        if matchs!=0:
          return(MatchsR(matchs,palabra,prefijo,ListaPalabras,Children))
        else:
           return ListaPalabras
     else:
        if Children.children[i].key==prefijo[k]:
            matchs = matchs + 1
            k = k + 1
            palabra = palabra + Children.children[i].key
            if Children.children[i].isEndOfWord==True:
              if CarcularParecido(matchs,palabra,prefijo,ListaPalabras,Children.children[i])==False:
                return ListaPalabras
            if k==len(prefijo):
              if Children.isEndOfWord==False:
                return(MatchsR(matchs,palabra,prefijo,ListaPalabras,Children.children[i]))
              else:
                break
            Children = Children.children[i]
            i = 0
        else:
           i = i + 1

  return ListaPalabras


T = Trie()
Insert(T,"obra")
print(matcheador(T,"obreros"))




