import pickle
import create
def search(text):
    try:
        with open('estructuras_pdf', 'rb') as f:
            lista_pdfs = pickle.load(f)
    except:
        quit("No database exists")
    
    str_main = create.create(text)
    print(str_main)
