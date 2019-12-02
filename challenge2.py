# http://www.pythonchallenge.com/pc/def/ocr.html


alphabet = "abcdefghijklmnopqrstuvwxyz"

def sift(x):
    mes = ''
    for c in x:
        if c in alphabet:
            mes += c
    return mes

inp = open("ch2.txt").read()


print(sift(inp))


# Turns out I misunderstood the problem but got it right 
