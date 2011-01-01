class Picture():
    def doSomething(self, n):
        print("Devo fare qualcosa con il valore %d." % n)

    def setDescription(foo, text):
        foo.description=text

    def getDescription(bar):
        return bar.description

img1=Picture()

img1.doSomething(42)   # uso il nome dell'istanza
Picture.doSomething(img1, 42) 

img1.setDescription('nice picture of the sea')

print(img1.getDescription())

