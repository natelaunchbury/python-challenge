# http://www.pythonchallenge.com/pc/def/peak.html

import urllib.request
import pickle

# This is the url hinted at in the html source of the problem url
url = "http://www.pythonchallenge.com/pc/def/banner.p"

request = urllib.request.urlopen(url).read()
# A large amount of 'pickled' data
#print(request)


# unpickle the above data to turn it back into a python structure
data = pickle.loads(request)
# turns out it's a list of lists of tuples 
# print(data)

# takes a list of (Str,Int) and prints n-copies of each string 
def rowPrint(ts):
    string = ''
    for (s,n) in ts:
        string+=(n*s) 
    print(string)

def draw(xs):
    for x in xs:
        rowPrint(x)

print(draw(data))
