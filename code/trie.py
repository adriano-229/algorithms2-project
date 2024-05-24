class Trie:
	root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False 
    cont = 0
def findKey(D,c):
    if c in D:
        return D.get(c)
    return None

def insertR(node,cad):
    k=cad[0]
    cadAux=cad[1:]
    t=TrieNode()
    t.parent=node
    t.key=k
    if node.children is None:
        node.children={k:t}
    else:
        node.children[k]=t

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

        insertR(list(node.values())[0].parent,cad[n:])
        return T
    else:
        t=TrieNode()
        t.key=cad[0]
        t.parent=T.root
        T.root.children[cad[0]]=t
        insertR(t,cad[1:])
        return T
 
def leeTrie(lista, cad, endWord, cont):
    #print(lista)
    if endWord is True:
        print(cad, "+= ", cont)
    if lista is None:
        return  
    
    for i in range(len(lista)):    
        leeTrie(list(lista.values())[i].children, cad+list(lista.values())[i].key,  list(lista.values())[i].isEndOfWord, list(lista.values())[i].cont)
