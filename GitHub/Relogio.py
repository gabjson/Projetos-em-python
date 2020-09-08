''' cria um relogio ai '''

from time import sleep

for h in range(24) :
    for m in range(60) :
        for s in range(60) :
            print('%02d:%02d:%02d' % (h, m, s))
            sleep(0.001)
