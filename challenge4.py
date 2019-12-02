import urllib.parse
import urllib.request
# http://www.pythonchallenge.com/pc/def/linkedlist.php 

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"

parse = urllib.parse.urlparse(url)
print(parse)

request = urllib.request.urlopen(url)
print(request.read())

def nextNothing(url):
    request = urllib.request.urlopen(url)
    contents = (request.read()).decode()
    nothing = ''
    for x in contents:
        if x.isdigit():
            nothing+=x
    if nothing=='':
        print(url) 
    nexturl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothing
    return nexturl

def followTheChain(n,url):
    if n==0:
        return 'done'
    else:
        nexturl = nextNothing(url)
        #print(nexturl)
        followTheChain(n-1,nexturl)


