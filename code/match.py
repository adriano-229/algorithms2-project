from trie import *
import math
def readBranch(lista, cad, endWord,cadList):
    if endWord is True:
        cadList.append(cad)
        #print(cad, "+= ", cadList)
    if lista is None:
        return  
    
    for i in range(len(lista)):    
        readBranch(list(lista.values())[i].children, cad+list(lista.values())[i].key,  list(lista.values())[i].isEndOfWord, cadList)

def matcher(T,cad):
    if T.root is None:
        return False
    return matcherR(T.root.children,cad,0,[],"",cad)

def matcherR(node,cad,contCad,cadList,palabra,cadOri):
    #print(cad)
    if node is not None:
        if len(cad)>0 and findKey(node,cad[0]) is not None:
            k=cad[0]
            Aux=cad[1:]
            node= findKey(node,k)
            palabra = palabra + k

            if node is not None:
                contCad+=1
                if node.isEndOfWord is True and contCad>=math.ceil(len(cadOri)/2):
                    #print("append(",palabra,")  ",contCad," >= " ,math.ceil(len(cadOri)/2))
                    cadList.append(palabra)
                        
                #print(cadList," : palabra ,", palabra , contCad)
            matcherR(node.children,Aux,contCad,cadList,palabra,cadOri)
        elif node is not None and contCad >= math.ceil(len(cadOri)/2):
            readBranch(list(node.values())[0].parent.children,palabra,False,cadList)
        
        #print(contCad,"+= ", cadList)
        return cadList
T=Trie()
palabras=['manzana', 'banana', 'cereza', 'dátil', 'arándano', 'frambuesa', 'kiwi', 'limón', 
    'mango', 'nectarina', 'naranja', 'papaya', 'pera', 'piña', 'plátano', 'sandía', 
    'toronja', 'uva',"uven","uval","uvalon","uvalones","uvalos","uvalosos","uvalesco", 'melón', 'pomelo', 'ciruela', 'fresa', 'coco', 'albaricoque', 
    'granada', 'higo', 'lichi', 'mandarina', 'maracuyá', 'mora']
for p in palabras:
     insert(T,p)
"""
l=matcher(T,"uvalon")
print(l)
"""
