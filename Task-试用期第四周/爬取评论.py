import requests
from bs4 import BeautifulSoup
import re

def getHTMLText(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def fileComment(comments,html):
    soup=BeautifulSoup(html,"html.parser")
    for i in soup(class_="floor"):
        comment=str(i.td).replace(str(i.blockquote),"").replace(str(i.small),"").replace("\n","")
        comments.append([comment])
    
def printComment(comments):
    task=open("./comments.txt","w+")
    task.write('\n'.join('%s' %id for id in comments))
    task.close()

def main():
    comments=[]
    url="https://bbs.hupu.com/20415703.html"
    html=getHTMLText(url)
    fileComment(comments,html)
    printComment(comments)
main()
