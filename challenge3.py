# http://www.pythonchallenge.com/pc/def/equality.html 

inp = open("ch3.txt").read()

def candidate(index):
   cand = inp[index:index+9]
   return cand 

def palindrome(x):
    return (x==x[::-1])

def hasBodyguards(x):
    return (x[0].islower() 
            and x[1].isupper() and x[2].isupper() and x[3].isupper() 
            and x[4].islower() 
            and x[5].isupper() and x[6].isupper() and x[7].isupper() 
            and x[8].islower()
           )

def search():
    for i in range(0,len(inp)):
        cand = candidate(i)
        if hasBodyguards(cand):
            print(cand)
    return ()
        





