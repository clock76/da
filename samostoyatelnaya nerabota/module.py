def readFileName(name = 'text.txt'):
    f = open(name)
    r = f.read()
    f.close()

    return r

def writeFileName(name = 'text.txt', text = ''):
    f = open(name, 'a')
    f.write(text)
    f.close()

    return 0

def rewriteFileName(name = 'text.txt', text = ''):
    f = open(name, 'w')
    f.write(text)
    f.close()

    return 0