import sys

from sys import argv


    f1 = open(argv[1],'r')
    f2 = open(argv[2],'r')
    f3 = open(argv[3],'w')

    f1_text=f1.read()
    f2_text=f2.read()
    f3.write("...")

    #print (f1.read())
    f1.close()
    f2.close()
    f3.close()
