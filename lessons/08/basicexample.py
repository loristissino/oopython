class Picture():
    pass
    # si usa la parola chiave "pass" quando
    # non c'è un corpo della funzione o della classe

img1=Picture()
img1.filename="gatto.jpg"
img1.filesize=12340
img1.width=320
img1.height=240
img1.filetype='JPEG'

print("Visualizzazione dell'intero dizionario:")
print(img1.__dict__)

img1.width=480
img1.__dict__['width']=480  # equivalente alla precedente
print("Visualizzazione dell'intero dizionario (un valore è cambiato):")

print(img1.__dict__)

print("Visualizzazione delle chiavi:")
for key in img1.__dict__.keys():
    print(key)
   
print("Visualizzazione dei valori:")
for value in img1.__dict__.values():
    print(value)

print("Visualizzazione delle coppie chiave/valore:")
for key, value in img1.__dict__.items():
    print(key, ' -->', value)
