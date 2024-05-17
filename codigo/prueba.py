class Trie:
  root = None
  nombre = None

class TrieNode:
  parent = None
  children = None 
  key = None
  isEndOfWord = False

class LinkedList:
  head = None

class PriorityNode:
  value = None
  priority = None
  nextNode = None
  
ListaTerminaPalabra = ["","(",")",".",",","?","¿","!","¡","-","''"]
C = LinkedList()

TextoPDF = "Esto es un texto prueba ¿Cual es el resultado?" # DSP DE USAR LA LIBRERIA DE JORGE NOS DA EL STRING (HAY QUE BUSCARLO EN LA MEMORIA Y GUARDA EL TRIE EN LA MEMORIA)
NormalizarTexto(TextoPDF,NombrePDF) # APARTIR DEL STRING FORMAREMOS PALABRAS(CONCATENANDO) Y BUSCAREMOS  EN UN HASH TABLE CON LAS PALABRAS A SKIPEAR, LUEGO SI LA PALABRA ES "VALIDA" LA NORMALIZAMOS (RAIZ) Y LA METEMOS EN UN TRIE
TextoDado = "Prueba de programa que resultado tira" #TEXTO DADO POR EL PROFESOR BUSCAR LAS PALABRAS EN EL TRIE Y VER CUANTO MATCHEAN
Matcheador(T,TextoDado) # DEPENDIENDO CUANTAS PALABRAS MATCHEAN AÑADIRA EL NOMBRE Y EL PORCENTAJE (T.root.value tendra la cantidad de palabras divido las matcheadas) A UNA COLA DE PRIORIDAD (PRIORIDAD=PORCENTAJE). 
# UNA VEZ HECHO ESTO CON TODOS LOS PDFS QUE TENGAMOS IMPRIMIMOS LA COLA
mostrar(C)
# FUNCIONES UTILIZADAS:
# 1) Search HashTable
# 2) Insert Trie
# FALTARIA AGREGAR:
# 1) HASH TABLE CON LAS PALABRAS A SKIPEAR. POSIBLES PALABRAS:
# ARTICULOS 
# PRONOMBRES
# PREPOSICIONES
# CONJUNCIONES
# NUMEROS
# 2) FUNCION MATCHEADOR
# 3) FUNCION RAIZ
# 4) CUANDO TERMINA EL COMPARADOR ¿COMO AGREGO EL NOMBRE DEL PDF?
# 5) APRENDER A LEER PDF Y GUARDAR TRIE EN MEMORIA PARA NO ESTAR LEYENDO CADA VEZ QUE ENTRAMOS


def Comparador(T,Texto):  # ARGUMENTO: T seria el trie de el pdf a analizar y Texto el texto que nos dio el profe
  n = len(Texto) # CANTIDAD DE CARACTERES DE N
  k = 0   
  Punto = 1   
  palabra = ""
  contador = 0
  contadorHash = 0
  Matchs = 0
  while k!=n:
    if Texto[k] in ListaTerminaPalabra:
      if contador!=0:
        contador = 0
        Punto = 1
        if Search(HashTablePalabras_a_Skipear,contadorHash)!=None:
          if Matcheador(T,palabra)==True:
            Matchs += 1
        contador = 0
        contadorHash = 0
        palabra = ""
    else:
      if Punto==1:
          Punto = 0
          a = str.lower(Texto[k])
          palabra = palabra + a
          contadorHash = contadorHash + ord(a)
      else:
        palabra = palabra + Texto[k]
        contadorHash = contadorHash + ord(Texto[k])
    k = k + 1
  if Matchs!=0:
    Porcentaje = Matchs/T.root.key
    NombrePDF = T.nombre
    AgregarCola(C,NombrePDF,Porcentaje) 


def Matcheador(T,palabra): #ARGUMENTO : Trie donde vamos a buscar y palabra con la que buscamos para matchear
  return True

  
def NormalizarTexto(Texto,NombrePDF): # TextoPDF que tengamos en nuestra base de datos
  T = Trie()
  T.nombre = NombrePDF
  Raiz = TrieNode()
  T.root = Raiz
  if n!=0:
    n = len(Texto)
  else:
    return None
  k = 0
  Punto = 1
  palabra = ""
  contador = 0
  contadorHash = 0
  while k!=n:
    if Texto[k] in ListaTerminaPalabra:
      Punto = 1
      if Search(HashTablePalabras_a_Skipear,contadorHash)!=None:
          palabraRaiz = Raiz(palabra)
          Insert(T,palabraRaiz)
      contador = 0
      contadorHash = 0
      palabra = ""
    else:
      if Punto==1:
        Punto = 0
        a = str.lower(Texto[k])
        palabra = palabra + a
        contadorHash = contadorHash + ord(a)
      else:
        palabra = palabra + Texto[k]
        contadorHash = contadorHash + ord(Texto[k])
    k = k + 1
  return(T)


def Raiz(palabra):
  return palabraRaiz


def search(D,key):
  h = FuncionHash(key)
  if D[h]==None:
    return None
  else:
    if D[h]==LinkedList:
      currentNode = D[h]
      while currentNode.nextnode!=None:
        if currentNode.key ==key:
          return currentNode.value
        else:
          currentNode = currentNode.nextnode
      return None
    else:
      if D[h].key==key:
        return D[h].value


def FuncionHash(key):
  return key%9


def Insert(T,element):
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
      T.root.key = T.root.key + 1
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
          T.root.key = T.root.key + 1
        else:
          if Children.children[i].key == element[k]:
            Children = Children.children[i]
            VoF = True
          else:
            i = i + 1
  
    k = k + 1
  Children.isEndOfWord = True


def AgregarCola(C,Nombre,Priority):
  NewNode = PriorityNode()
  NewNode.value = Nombre
  NewNode.priority = Priority
  currentNode = C.head
  Anterior = currentNode
  if currentNode==None:
    currentNode = NewNode
    return
  else:
    while currentNode.nextNode!=None:
      if NewNode.value>currentNode.value:
        if currentNode!=C.head:
          Anterior.nextNode = NewNode
          NewNode.nextNode = currentNode
          return
        else:
          C.head = NewNode
          NewNode.nextNode = currentNode
          return
      else:
        Anterior = currentNode
        currentNode = currentNode.nextNode
    currentNode.nextNode = NewNode


def mostrar(Q):
  currentNode = Q.head
  if currentNode==None:
    print("No se encontro ningun libro")
  else:
    print("Los libros que mas matchearon de mayor a menor son: ")
    while currentNode !=None:
      print(currentNode.value, end='º')
      print(currentNode.priority, end='%')
      currentNode = currentNode.nextNode
      print("")













